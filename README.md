# Data Science Interview Prep

A topic-organized collection of technical practice problems and worked solutions used while preparing for senior and staff data-science interviews.

The material emphasizes product data science: Python, pandas, statistics, experimentation, causal inference, machine learning, SQL, analytical debugging, and structured communication.

## Topics

- [Python fundamentals](python/README.md) ([solutions](python/solutions.md))
- [Sliding windows](sliding_windows/README.md) ([solutions](sliding_windows/solutions.md))
- [Intervals, scheduling, and heaps](intervals_heaps/README.md) ([solutions](intervals_heaps/solutions.md))
- [pandas](pandas/README.md) ([solutions](pandas/solutions.md))
- [Probability and statistics](statistics/README.md) ([solutions](statistics/solutions.md))
- [Experimentation and causal inference](experimentation/README.md) ([solutions](experimentation/solutions.md))
- [Regression and machine learning](machine_learning/README.md) ([solutions](machine_learning/solutions.md))
- [SQL](sql/README.md) ([solutions](sql/solutions.md))
- [Data intuition and debugging](data_debugging/README.md) ([solutions](data_debugging/solutions.md))
- [Communication drills](communication/README.md) ([solutions](communication/solutions.md))

## Reproducible example data

Reusable dataframe generators live in [`data/generators.py`](data/generators.py). They can be copied into a notebook or imported after cloning the repository.

```python
from data.generators import make_commerce_data, make_clickstream, make_experiment

customers, orders, reviews = make_commerce_data()
clicks = make_clickstream()
experiment = make_experiment()
```

## SQL preparation

The SQL portion of the preparation was primarily completing every free SQL question on [DataLemur](https://datalemur.com/sql-interview-questions). The SQL material in this repository consists of original companion exercises and reusable patterns; it does not reproduce DataLemur's proprietary prompts or solutions.

## Provenance and interview confidentiality

This is a deliberately conservative, public-safe subset of the preparation material. It includes only general exercises that were discussed as preparation before interviews or are standard companion exercises to those topics.

It excludes:

- actual interview questions or close paraphrases;
- company-specific scenarios;
- topics first introduced during post-interview debriefs;
- prompts whose timing or provenance was uncertain; and
- proprietary DataLemur questions or solutions.

Because public sharing creates a higher bar than private study notes, ambiguous items were removed rather than retained.
