# SQL: Solutions

### Latest event per user

```sql
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY user_id ORDER BY event_ts DESC, event_type DESC
  ) AS rn
  FROM events
)
SELECT user_id, event_ts, event_type
FROM ranked
WHERE rn = 1;
```

### Top three products per category, including ties

```sql
WITH product_revenue AS (
  SELECT category, product_id, SUM(revenue) AS revenue
  FROM sales
  GROUP BY 1,2
), ranked AS (
  SELECT *, DENSE_RANK() OVER (
    PARTITION BY category ORDER BY revenue DESC
  ) AS rnk
  FROM product_revenue
)
SELECT * FROM ranked WHERE rnk <= 3;
```

### Longest active-day streak

```sql
WITH deduped AS (
  SELECT DISTINCT user_id, activity_date FROM activity
), grouped AS (
  SELECT *, activity_date - ROW_NUMBER() OVER (
    PARTITION BY user_id ORDER BY activity_date
  ) * INTERVAL '1 day' AS island
  FROM deduped
), streaks AS (
  SELECT user_id, island, COUNT(*) AS streak_length
  FROM grouped GROUP BY 1,2
)
SELECT user_id, MAX(streak_length) AS longest_streak
FROM streaks GROUP BY user_id;
```

### Sessionization

```sql
WITH gaps AS (
  SELECT user_id, event_ts,
    CASE WHEN LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) IS NULL
           OR event_ts - LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) > INTERVAL '30 minutes'
         THEN 1 ELSE 0 END AS new_session
  FROM clicks
), numbered AS (
  SELECT *, SUM(new_session) OVER (
    PARTITION BY user_id ORDER BY event_ts ROWS UNBOUNDED PRECEDING
  ) AS session_id
  FROM gaps
)
SELECT user_id, session_id, MIN(event_ts) AS session_start,
       MAX(event_ts) AS session_end, COUNT(*) AS event_count
FROM numbered GROUP BY 1,2;
```

### Seven-day rolling revenue

```sql
SELECT day, platform, revenue,
  SUM(revenue) OVER (
    PARTITION BY platform ORDER BY day
    RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW
  ) AS revenue_7d
FROM daily_revenue;
```

### Day-1 and day-7 retention

```sql
WITH user_activity AS (
  SELECT u.user_id, u.signup_date,
    MAX(CASE WHEN e.event_date = u.signup_date + INTERVAL '1 day' THEN 1 ELSE 0 END) AS d1,
    MAX(CASE WHEN e.event_date = u.signup_date + INTERVAL '7 days' THEN 1 ELSE 0 END) AS d7
  FROM users u LEFT JOIN events e USING (user_id)
  GROUP BY 1,2
)
SELECT signup_date, AVG(d1::numeric) AS d1_retention,
       AVG(d7::numeric) AS d7_retention
FROM user_activity GROUP BY signup_date ORDER BY signup_date;
```

### Ordered funnel

```sql
WITH stages AS (
  SELECT user_id,
    MIN(CASE WHEN event_name='view' THEN event_ts END) AS view_ts,
    MIN(CASE WHEN event_name='cart' THEN event_ts END) AS cart_ts,
    MIN(CASE WHEN event_name='purchase' THEN event_ts END) AS purchase_ts
  FROM events GROUP BY user_id
), flags AS (
  SELECT user_id,
    (view_ts IS NOT NULL)::int AS viewed,
    (cart_ts > view_ts)::int AS carted,
    (purchase_ts > cart_ts AND cart_ts > view_ts)::int AS purchased
  FROM stages
)
SELECT AVG(viewed::numeric) AS view_rate,
       SUM(carted)::numeric / NULLIF(SUM(viewed),0) AS view_to_cart,
       SUM(purchased)::numeric / NULLIF(SUM(carted),0) AS cart_to_purchase
FROM flags;
```

For fully correct ordering with repeated events, stage through the first cart after first view and first purchase after that cart.

### Friends of friends

```sql
SELECT f1.user_id, f2.friend_id AS recommended_user_id,
       COUNT(*) AS mutual_friends
FROM friendships f1
JOIN friendships f2 ON f1.friend_id = f2.user_id
LEFT JOIN friendships direct
  ON direct.user_id = f1.user_id AND direct.friend_id = f2.friend_id
WHERE f1.user_id <> f2.friend_id AND direct.friend_id IS NULL
GROUP BY 1,2
ORDER BY 1,3 DESC,2;
```

### Cancellation rate excluding banned users

```sql
SELECT t.request_date,
  AVG(CASE WHEN t.status IN ('cancelled_by_driver','cancelled_by_client')
           THEN 1.0 ELSE 0.0 END) AS cancellation_rate
FROM trips t
JOIN users c ON c.user_id=t.client_id
JOIN users d ON d.user_id=t.driver_id
WHERE c.banned=FALSE AND d.banned=FALSE
GROUP BY t.request_date ORDER BY t.request_date;
```

### Consecutive qualifying IDs

```sql
WITH eligible AS (
  SELECT *, id - ROW_NUMBER() OVER (ORDER BY id) AS grp
  FROM stadium WHERE people >= 100
), valid AS (
  SELECT grp FROM eligible GROUP BY grp HAVING COUNT(*) >= 3
)
SELECT e.* FROM eligible e JOIN valid USING (grp) ORDER BY id;
```
