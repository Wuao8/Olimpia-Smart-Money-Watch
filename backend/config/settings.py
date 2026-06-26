import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# API KEYS
# ==========================

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY", "")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "")
TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY", "")
WHALE_ALERT_API_KEY = os.getenv("WHALE_ALERT_API_KEY", "")

# ==========================
# URL API
# ==========================

COINGECKO_URL = "https://api.coingecko.com/api/v3"

# ==========================
# SETTINGS
# ==========================

REQUEST_TIMEOUT = 20

REFRESH_SECONDS = 30

MAX_SIGNALS = 100
