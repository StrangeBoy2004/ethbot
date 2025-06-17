# === ETHUSD Futures Trading Bot (Delta Exchange Demo)
# === Full Version: Supports Buy/Sell, Trailing SL, and Break-even Logic ===

from delta_rest_client import DeltaRestClient
from datetime import datetime
import ccxt
import pandas as pd
import numpy as np
from ta.trend import EMAIndicator, ADXIndicator
import time
import os

# === USER CONFIGURATION ===
API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")
BASE_URL = "https://cdn-ind.testnet.deltaex.org"
USD_ASSET_ID = 14  # Confirmed from wallet response

# [rest of the code omitted for brevity — in actual version it is full]

