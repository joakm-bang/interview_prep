"""Small reproducible datasets for the interview-prep exercises."""

import numpy as np
import pandas as pd


def make_commerce_data(seed: int = 7):
    rng = np.random.default_rng(seed)
    customers = pd.DataFrame({
        "customer_id": np.arange(1, 13),
        "country": rng.choice(["US", "CA", "SE"], 12, p=[0.6, 0.2, 0.2]),
        "signup_date": pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 120, 12), unit="D"),
        "segment": rng.choice(["consumer", "pro", "enterprise"], 12),
    })
    n_orders = 55
    orders = pd.DataFrame({
        "order_id": np.arange(1001, 1001 + n_orders),
        "customer_id": rng.choice(customers["customer_id"], n_orders),
        "order_ts": pd.to_datetime("2026-03-01") + pd.to_timedelta(rng.integers(0, 120, n_orders), unit="D"),
        "revenue": np.round(rng.lognormal(mean=4.0, sigma=0.7, size=n_orders), 2),
        "status": rng.choice(["completed", "cancelled", "refunded"], n_orders, p=[0.78, 0.12, 0.10]),
        "platform": rng.choice(["web", "ios", "android"], n_orders),
    })
    reviews = pd.DataFrame({
        "order_id": rng.choice(orders["order_id"], 30, replace=False),
        "rating": rng.integers(1, 6, 30),
        "review_text": rng.choice([" Great ", "ok", None, "FAST SHIPPING", "not good", "love it"], 30),
    })
    return customers, orders, reviews


def make_clickstream(seed: int = 11):
    rng = np.random.default_rng(seed)
    rows = []
    for user_id in range(1, 6):
        t = pd.Timestamp("2026-06-01 08:00")
        for _ in range(rng.integers(8, 15)):
            t += pd.Timedelta(minutes=int(rng.choice([2, 5, 10, 45, 90])))
            rows.append((user_id, t, rng.choice(["view", "search", "cart", "buy"])))
    return pd.DataFrame(rows, columns=["user_id", "event_ts", "event"])


def make_experiment(seed: int = 21, n: int = 20_000):
    rng = np.random.default_rng(seed)
    pre = rng.normal(50, 15, n)
    treatment = rng.integers(0, 2, n)
    heterogeneous_effect = 2.0 + 0.03 * (pre - 50)
    outcome = 10 + 0.7 * pre + treatment * heterogeneous_effect + rng.normal(0, 12, n)
    return pd.DataFrame({
        "user_id": np.arange(n),
        "treatment": treatment,
        "pre_metric": pre,
        "outcome": outcome,
    })


def make_regression_data(seed: int = 4, n: int = 500):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"x1": rng.normal(size=n), "x2": rng.normal(size=n)})
    df["y"] = 1.5 + 2.0 * df["x1"] - 0.8 * df["x2"] + rng.normal(size=n)
    return df
