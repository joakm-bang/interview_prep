# pandas: Practice problems

Paste this generator into a notebook:

```python
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

customers, orders, reviews = make_commerce_data()
```

1. Completed-order summary per customer: count, total, mean, latest timestamp; include zero-order customers.
2. Top two customers per country by completed revenue, including ties.
3. Days from signup to first order; keep customers with no orders.
4. Daily completed revenue by platform plus 7-calendar-day rolling sum.
5. Days since previous order within customer.
6. Clean review text; create `has_review` and `positive_review`.
7. Add customer lifetime completed revenue to every order with both `transform` and aggregate-plus-merge; explain when each is preferable.
8. Sessionize clickstream events with a 30-minute inactivity threshold.

Clickstream generator:

```python
def make_clickstream(seed: int = 11):
    rng = np.random.default_rng(seed)
    rows = []
    for user_id in range(1, 6):
        t = pd.Timestamp("2026-06-01 08:00")
        for _ in range(rng.integers(8, 15)):
            t += pd.Timedelta(minutes=int(rng.choice([2, 5, 10, 45, 90])))
            rows.append((user_id, t, rng.choice(["view", "search", "cart", "buy"])))
    return pd.DataFrame(rows, columns=["user_id", "event_ts", "event"])

clicks = make_clickstream()
```
