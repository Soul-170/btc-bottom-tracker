import json, urllib.request, datetime

ATH_PRICE = 108800.0
ATH_DATE = "2025-10-06"
REALIZED_PRICE = 53000.0

def fetch_data():
    price, sma_200w, fng = 57760.0, 58900.0, 25
    try:
        req = urllib.request.Request("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            price = float(json.loads(r.read().decode())['price'])
    except Exception:
        pass

    try:
        req = urllib.request.Request("https://api.alternative.me/fng/?limit=1", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            fng = int(json.loads(r.read().decode())['data'][0]['value'])
    except Exception:
        pass

    diff_days = max(1, (datetime.datetime.utcnow() - datetime.datetime.strptime(ATH_DATE, "%Y-%m-%d")).days)
    payload = {
        "btcPrice": round(price),
        "athPrice": round(ATH_PRICE),
        "athDays": diff_days,
        "athDropPct": round(((price - ATH_PRICE) / ATH_PRICE) * 100, 1),
        "sma200wPrice": round(sma_200w),
        "fearAndGreed": fng,
        "lastUpdated": datetime.datetime.now().strftime("%d %b %Y, %H:%M UTC")
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    fetch_data()
