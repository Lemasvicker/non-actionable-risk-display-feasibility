from __future__ import annotations
import argparse
import json
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Path to feasibility log JSON")
    args = p.parse_args()

    path = Path(args.input)
    data = json.loads(path.read_text(encoding="utf-8"))

    # Minimal sanity checks (v0.1.0). We keep it dependency-free.
    required_top = ["session_id", "created_utc", "system", "metrics"]
    missing = [k for k in required_top if k not in data]
    if missing:
        raise SystemExit(f"Missing required fields: {missing}")

    m = data["metrics"]
    for k in ["uptime_fraction", "data_yield_fraction"]:
        if not (0.0 <= float(m[k]) <= 1.0):
            raise SystemExit(f"{k} must be in [0,1]")

    if float(m["median_latency_ms"]) < 0:
        raise SystemExit("median_latency_ms must be >= 0")

    print("OK: feasibility log passes v0.1.0 checks")

if __name__ == "__main__":
    main()
