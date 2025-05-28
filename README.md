# 🎮 Dota-Stats: Public Match Analytics in Dota 2

A data analytics project exploring 20,000+ public Dota 2 matches to uncover player behavior, hero dynamics, and match outcome patterns using scalable **data processing**, **feature engineering**, and **visualization techniques**.

---

## 📌 Project Overview

This project analyzes publicly available Dota 2 match data to understand the influence of factors like party size, hero combinations, and game metrics (comeback, throw, stomp, loss) on team performance and win rates. It showcases a complete **end-to-end data analytics pipeline** from raw ingestion to rich visualization.

---

## ⚙️ Methodologies & Concepts Applied

- **Data Ingestion & Cleaning**: Efficient batch-wise processing of 20,000+ raw JSON files.
- **Data Normalization**: Structured large nested JSON into relational-like tables (matches, players, chat, objectives).
- **Exploratory Data Analysis (EDA)**:
  - Correlation of **party size** with **win rate** and match dynamics.
  - Aggregated stats such as **mean comeback**, **mean throw**, etc.
- **Hero Combination Analysis**: Identification of high-performing hero sets across thousands of games.
- **Chat Log & Objective Parsing**: Extraction and transformation of nested chat and map event logs.
- **Semantic Analysis** (TF-IDF): Applied on hero lore texts to cluster heroes based on thematic similarity.
- **Time Zone Adjustments**: Converting match start times based on regional servers.

---

## 🧰 Tools & Technologies Used

| Category              | Tools / Libraries Used                                                |
|-----------------------|------------------------------------------------------------------------|
| **Language**          | Python                                                                 |
| **Data Processing**   | `Pandas`, `NumPy`, `json`, `ast`                                       |
| **Scalability**       | `Batch Processing`, `Pickle`, `PySpark` for distributed computation    |
| **Visualization**     | `Matplotlib`, `Seaborn`                                                |
| **ML/NLP**            | `sklearn` (`TfidfVectorizer`, `KMeans`, `cosine_similarity`)           |
| **Storage Formats**   | CSV, Pickle, JSON                                                      |
| **Utilities**         | `os`, `collections`, `defaultdict`, `datetime`                         |

---

## 📊 Visual Insights

- **Line Charts**: Party size vs Win Rate, Comeback, Throw, Stomp
- **Heatmaps**: Hero lore semantic similarity using TF-IDF
- **Combination Analytics**: Most successful hero lineups across Radiant and Dire

