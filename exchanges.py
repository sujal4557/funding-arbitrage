import requests, time

BINANCE = "https://fapi.binance.com/fapi/v1/premiumIndex"
BYBIT = "https://api.bybit.com/v5/market/tickers?category=linear"
DELTA = "https://api.india.delta.exchange/v2/tickers?contract_types=perpetual_futures"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_binance():
    url = "https://fapi.binance.com/fapi/v1/premiumIndex"
    r = requests.get(url, timeout=10)

    try:
        data = r.json()
    except Exception:
        return {}

    # ❗ Binance error protection
    if not isinstance(data, list):
        print("Binance API error:", data)
        return {}

    return {
        d["symbol"]: float(d["lastFundingRate"]) * 100
        for d in data
        if "lastFundingRate" in d
    }


def fetch_bybit():
    res = requests.get(BYBIT, headers=HEADERS, timeout=10).json()
    out = {}
    for r in res["result"]["list"]:
        if r["fundingRate"]:
            out[r["symbol"]] = float(r["fundingRate"]) * 100
    return out

def fetch_delta():
    res = requests.get(DELTA, headers=HEADERS, timeout=10).json()["result"]
    return {r["symbol"]: float(r["funding_rate"]) for r in res}

