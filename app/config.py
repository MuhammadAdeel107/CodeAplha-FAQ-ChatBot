from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

FAQ_FILE = BASE_DIR / "data" / "faqs.json"

SIMILARITY_THRESHOLD = 0.25