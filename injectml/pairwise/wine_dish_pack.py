"""
Built-in wine–dish knowledge pack for the PairWise demo.
"""

from __future__ import annotations

from ..knowledge_pack import KnowledgePack, KnowledgeEntry

_ENTRIES = [
    # White wines
    ("pw001", ["chardonnay", "white_wine", "fish", "chicken", "cream_sauce"],
     "Chardonnay pairs well with fish, chicken, and dishes featuring cream or butter sauces."),
    ("pw002", ["sauvignon_blanc", "white_wine", "seafood", "salad", "goat_cheese"],
     "Sauvignon Blanc is an excellent match for seafood, green salads, and goat cheese."),
    ("pw003", ["pinot_gris", "pinot_grigio", "white_wine", "salmon", "sushi", "light_pasta"],
     "Pinot Gris / Pinot Grigio complements salmon, sushi, and light pasta dishes."),
    ("pw004", ["riesling", "white_wine", "spicy", "asian", "pork", "duck"],
     "Riesling, especially off-dry styles, balances spicy Asian dishes and pairs with pork or duck."),
    ("pw005", ["viognier", "white_wine", "rich_seafood", "lobster", "crab", "aromatic"],
     "Viognier suits aromatic, rich seafood like lobster and crab."),

    # Red wines
    ("pw006", ["cabernet_sauvignon", "red_wine", "beef", "lamb", "aged_cheese"],
     "Cabernet Sauvignon is a classic with beef, lamb, and aged hard cheeses."),
    ("pw007", ["pinot_noir", "red_wine", "salmon", "duck", "mushroom", "earthy"],
     "Pinot Noir pairs beautifully with salmon, duck, and earthy mushroom-based dishes."),
    ("pw008", ["merlot", "red_wine", "pork", "chicken", "tomato_sauce", "soft_cheese"],
     "Merlot is versatile with pork, chicken in tomato sauce, and soft cheeses."),
    ("pw009", ["shiraz", "syrah", "red_wine", "grilled_meat", "barbecue", "spicy"],
     "Shiraz/Syrah shines with grilled meats, barbecue, and spicy preparations."),
    ("pw010", ["zinfandel", "red_wine", "barbecue", "pizza", "spicy", "hamburger"],
     "Zinfandel is an excellent partner for barbecue, pizza, and hearty American fare."),
    ("pw011", ["malbec", "red_wine", "beef", "lamb", "empanadas", "grilled"],
     "Malbec pairs perfectly with beef, lamb, and traditional Argentine grilled dishes."),

    # Sparkling wines
    ("pw012", ["champagne", "prosecco", "sparkling", "oyster", "caviar", "fried_food", "appetizer"],
     "Champagne and Prosecco cut through richness in fried foods and elevate oysters or caviar."),
    ("pw013", ["cava", "sparkling", "tapas", "seafood", "paella"],
     "Cava is a natural partner for Spanish tapas, seafood, and paella."),

    # Rosé
    ("pw014", ["rose", "rosé", "salmon", "salad", "summer", "light_appetizer"],
     "Rosé is a versatile all-rounder for salads, salmon, and light summer appetizers."),

    # Dessert wines
    ("pw015", ["sauternes", "dessert_wine", "foie_gras", "blue_cheese", "peach_dessert"],
     "Sauternes is a celebrated match for foie gras, blue cheese, and peach-based desserts."),
    ("pw016", ["port", "dessert_wine", "chocolate", "stilton", "walnut"],
     "Port, especially Tawny, pairs wonderfully with chocolate, Stilton, and walnuts."),

    # General pairing principles
    ("pw100", ["principle", "weight", "body"],
     "Match the weight of the wine to the weight of the dish: light wines with delicate foods."),
    ("pw101", ["principle", "acidity", "fatty", "fried"],
     "High-acid wines cut through fatty and fried foods, cleansing the palate."),
    ("pw102", ["principle", "sweet", "spicy", "heat"],
     "Off-dry or sweet wines tame the heat in spicy dishes by providing contrast."),
    ("pw103", ["principle", "tannin", "protein", "beef"],
     "Tannins in red wine soften against the protein in red meat, making the wine taste smoother."),
    ("pw104", ["principle", "regional", "local"],
     "Regional pairings often work naturally: drink local wines with local cuisine."),
]

_ALIASES = {
    "chard": "chardonnay",
    "sauv blanc": "sauvignon_blanc",
    "pinot grigio": "pinot_gris",
    "cab sav": "cabernet_sauvignon",
    "cab": "cabernet_sauvignon",
    "bubbly": "sparkling",
    "fizz": "sparkling",
    "steak": "beef",
    "shrimp": "seafood",
    "prawn": "seafood",
    "tuna": "fish",
    "cod": "fish",
    "halibut": "fish",
    "bbq": "barbecue",
    "veggie": "salad",
}


def build_wine_dish_pack() -> KnowledgePack:
    """Return the built-in wine–dish pairing :class:`~injectml.knowledge_pack.KnowledgePack`."""
    entries = [KnowledgeEntry(eid, tags, text) for eid, tags, text in _ENTRIES]
    return KnowledgePack(
        name="Wine–Dish Pairings",
        domain="wine_pairing",
        version="1.0",
        entries=entries,
        aliases=_ALIASES,
    )
