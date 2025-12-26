from exchanges import fetch_binance, fetch_bybit, fetch_delta

def scan(threshold=0.2):
    b = fetch_binance()
    y = fetch_bybit()
    d = fetch_delta()

    rows = []

    for sym in set(b) & set(y):
        d_sym = sym.replace("USDT", "USD")
        if d_sym not in d:
            continue

        rates = {
            "Binance": b[sym],
            "Bybit": y[sym],
            "Delta": d[d_sym]
        }

        low = min(rates, key=rates.get)
        high = max(rates, key=rates.get)
        diff = abs(rates[high] - rates[low])

        if diff >= threshold:
            rows.append({
                "symbol": sym,
                "long": low,
                "short": high,
                "diff": round(diff, 3),
                "rates": rates
            })

    return sorted(rows, key=lambda x: x["diff"], reverse=True)
