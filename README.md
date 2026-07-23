# Data Science Interview Prep

A topic-organized collection of technical practice problems and worked solutions used while preparing for senior and staff data-science interviews.

This is primarily a record of **how I actually prepared**, not an attempt to build an exhaustive interview curriculum. The emphasis is product data science: Python, pandas, statistics, experimentation, causal inference, machine learning, SQL, analytical debugging, and structured communication.

## What I actually used

My technical preparation consisted mainly of:

- working through the exercises in the core topic folders below;
- completing every free SQL question on [DataLemur](https://datalemur.com/sql-interview-questions);
- practicing concise, top-down explanations of analytical and technical work.

The core section includes only material I remember practicing or closely related original companion exercises. It deliberately does not try to teach every standard computer-science topic.

## Core topics

- [Python fundamentals and binary search](python/README.md) ([solutions](python/solutions.md))
- [Sliding windows](sliding_windows/README.md) ([solutions](sliding_windows/solutions.md))
- [Intervals, scheduling, and heaps](intervals_heaps/README.md) ([solutions](intervals_heaps/solutions.md))
- [pandas](pandas/README.md) ([solutions](pandas/solutions.md))
- [Probability and statistics](statistics/README.md) ([solutions](statistics/solutions.md))
- [Experimentation and causal inference](experimentation/README.md) ([solutions](experimentation/solutions.md))
- [Regression and machine learning](machine_learning/README.md) ([solutions](machine_learning/solutions.md))
- [SQL](sql/README.md) ([solutions](sql/solutions.md))
- [Data intuition and debugging](data_debugging/README.md) ([solutions](data_debugging/solutions.md))
- [Communication drills](communication/README.md) ([solutions](communication/solutions.md))

## Optional extras

[`optional_extras/README.md`](optional_extras/README.md) tracks adjacent subjects someone might choose to add for broader interview coverage.

These topics are explicitly **not presented as part of my own preparation**. The list is intentionally an outline rather than a second giant curriculum, since standard material such as tree traversal or generic system design is already easy to find elsewhere.

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

## Interview confidentiality

This repository deliberately excludes actual interview questions, company-specific prompts, close reconstructions of interview questions, and subjects first raised in post-interview debriefs. The included material is general-purpose preparation content and standard companion exercises.

See [`PROVENANCE.md`](PROVENANCE.md) for the publication guardrails.

## How to use this repository

Work through each topic's `README.md` without opening its `solutions.md`. For coding exercises, compare not only correctness but also complexity, edge-case handling, and clarity. For analytical cases, practice answering top-down: headline, framework, details, tradeoffs, and recommendation.
