import pandas as pd
import json
import urllib.request
from datetime import datetime, timezone

API_URL = "http://136.64.123.205/predict"

df = pd.read_csv("results/random_100.csv")

results = []

for i, row in df.iterrows():
    payload = row.to_dict()

    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode())

        results.append({
            "row_id": i,
            "prediction": result["prediction"],
            "timestamp": result["timestamp"],
            "status": "success"
        })

        print(f"{i+1}/100 -> {result['prediction']}")

    except Exception as e:
        results.append({
            "row_id": i,
            "prediction": None,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": f"error: {e}"
        })

        print(f"{i+1}/100 -> ERROR: {e}")

pd.DataFrame(results).to_csv(
    "results/predictions_100.csv",
    index=False
)

print("\nSaved results/predictions_100.csv")
print("Successful:", sum(r["status"] == "success" for r in results))
