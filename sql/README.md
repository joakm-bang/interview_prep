# SQL: Practice problems

The main SQL preparation was every free question on [DataLemur](https://datalemur.com/sql-interview-questions). These original exercises reinforce the reusable patterns without reproducing DataLemur prompts.

1. Latest event per user with deterministic ties.
2. Top three products per category by revenue, including ties.
3. Longest consecutive active-day streak using gaps and islands.
4. Sessionization with a 30-minute inactivity gap.
5. Seven-calendar-day rolling revenue by platform.
6. Day-1 and day-7 retention by signup date.
7. Ordered `view -> cart -> purchase` funnel conversion.
8. Friends-of-friends recommendations ranked by mutual friends.
9. Daily trip cancellation rate excluding banned clients and drivers.
10. Runs of at least three consecutive IDs where a threshold condition holds.

Suggested schemas:

```sql
events(user_id, event_ts, event_type)
sales(order_id, product_id, category, revenue, order_date)
activity(user_id, activity_date)
clicks(user_id, event_ts)
daily_revenue(day, platform, revenue)
users(user_id, signup_date, banned)
friendships(user_id, friend_id)
trips(trip_id, client_id, driver_id, status, request_date)
stadium(id, visit_date, people)
```
