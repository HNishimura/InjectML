import json
import sys
from pathlib import Path

import requests
from transformers import AutoTokenizer


MODEL = "llama3:8b"
TOKENIZER = "NousResearch/Meta-Llama-3-8B"
BOS_ID = 128000
BOUNDARY_ID = 128009
INPUT_PATH = Path("pairwise_rules_normalized.txt")
PACK_PATH = Path("pairwise_tokens.json")


def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER, local_files_only=True, use_fast=True)
    if tokenizer.bos_token_id != BOS_ID:
        raise ValueError("ERROR_TOKENIZER_BOS_MISMATCH")
    if tokenizer.convert_tokens_to_ids("<|eot_id|>") != BOUNDARY_ID:
        raise ValueError("ERROR_TOKENIZER_BOUNDARY_MISMATCH")
    return tokenizer


def read_rules():
    if not INPUT_PATH.is_file():
        raise FileNotFoundError("ERROR_INPUT_NOT_READABLE")
    lines = INPUT_PATH.read_text(encoding="ascii").splitlines()
    if len(lines) % 4:
        raise ValueError("ERROR_INPUT_INVALID_STRUCTURE")
    rules = []
    for offset in range(0, len(lines), 4):
        block = lines[offset : offset + 3]
        if lines[offset + 3] != "":
            raise ValueError("ERROR_INPUT_MISSING_RULE_SEPARATOR")
        if not block[0].startswith("Dish: ") or not block[1].startswith("Wine: ") or not block[2].startswith("Reason: "):
            raise ValueError("ERROR_INPUT_INVALID_KEYS")
        if any(not line.split(": ", 1)[1] for line in block):
            raise ValueError("ERROR_INPUT_EMPTY_VALUE")
        if any(any(ord(character) > 127 for character in line) for line in block):
            raise ValueError("ERROR_INPUT_NON_ASCII")
        rules.append("\n".join(block))
    return rules


def create_pack(tokenizer, rules):
    blocks = [tokenizer.encode(rule, add_special_tokens=False) for rule in rules]
    if any(not block for block in blocks):
        raise ValueError("ERROR_EMPTY_TOKEN_BLOCK")
    PACK_PATH.write_text(json.dumps(blocks, separators=(",", ":")) + "\n", encoding="ascii")
    return blocks


def read_pack():
    if not PACK_PATH.is_file():
        raise FileNotFoundError("ERROR_PACK_NOT_READABLE")
    try:
        blocks = json.loads(PACK_PATH.read_text(encoding="ascii"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("ERROR_PACK_MALFORMED_JSON") from error
    if not isinstance(blocks, list) or not blocks:
        raise ValueError("ERROR_PACK_INVALID_ROOT")
    if any(not isinstance(block, list) or not block or any(type(token) is not int for token in block) for block in blocks):
        raise ValueError("ERROR_PACK_INVALID_TOKEN_BLOCK")
    return blocks


def assemble_context(tokenizer, blocks, user_prompt):
    prompt_tokens = tokenizer.encode(user_prompt, add_special_tokens=False)
    if not prompt_tokens:
        raise ValueError("ERROR_EMPTY_USER_PROMPT")
    context = [BOS_ID]
    for index, block in enumerate(blocks):
        if index:
            context.append(BOUNDARY_ID)
        context.extend(block)
    context.extend(prompt_tokens)
    return context


def run_inference(tokenizer, context):
    prompt = tokenizer.decode(context, skip_special_tokens=False)
    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False, "options": {"temperature": 0, "top_p": 1, "top_k": 1, "seed": 0}},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["response"]


def main():
    tokenizer = load_tokenizer()
    rules = read_rules()
    create_pack(tokenizer, rules)
    first = read_pack()
    second = json.loads(PACK_PATH.read_text(encoding="ascii"))
    if first != second:
        raise ValueError("ERROR_PACK_NOT_DETERMINISTIC")
    context = assemble_context(tokenizer, first, sys.argv[1] if len(sys.argv) > 1 else "Recommend a wine for sushi.")
    if not context or context[0] != BOS_ID:
        raise ValueError("ERROR_CONTEXT_INVALID")
    print(f"PASS_RULE_BLOCKS={len(first)}")
    print(f"PASS_CONTEXT_TOKENS={len(context)}")
    print("INFERENCE=" + run_inference(tokenizer, context))


if __name__ == "__main__":
    main()