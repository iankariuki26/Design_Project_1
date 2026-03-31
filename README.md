# **`DS 4320 Project 1: Beyond Blockbuster - The New "Hidden Gem" Discovery Engine"`**


## `Executive Summary`
#### This repository contains a full-stack data engineering and analytics pipeline designed to mitigate the ever-present popularity bias in modern media’s recommendation systems. Utilizing the MovieLens 25M dataset, the project implements a robust relational model within DuckDB for the purpose of isolating “Hidden Gems,” which are films with high user acclaim (Avg > 4.0) but low market saturation (50-500 ratings). The system transitions from a heavy SQL-based ETL process to a predictive modeling phase using Singular Value Decomposition (SVD) to map latent user preferences to niche content. The final deliverable includes a 4-table relational schema stored in Parquet format, a production-ready Python pipeline with integrated logging and error handling, and a comparative analysis of how matrix factorization outperforms standard popularity-weighted algorithms in surface-level discovery.

## Name - Ian Kariuki
## NetID - epj7rf
## DOI:
## Press Release
## Pipeline - analysis code
## Data - Link to [Data](https://myuva-my.sharepoint.com/:f:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/ml-25m?csf=1&web=1&e=ieV6WU)
## License - [MIT](https://github.com/iankariuki26/Design_Project_1?tab=MIT-1-ov-file#readme)



## `Problem Definition`

## **General and Specific Problem**
- General Problem: There is much user fatigue in deciding what digital recommended content to watch

- Specific Problem: Develop a relational database using the MoviewLens 25M dataset to devleop a robust recommendation engine. This engine will use SQL aggregations to identify "hidden gems" which represent high-rated, low-viewed content, ans well as SVD to predict user-specific preference scores, prioritizing niche content over mainstream hits.


## Rationale
There exists a need to solve "popularity bias" which is a prevelant failure in basic algorithms where popular content tends to drown out high-quiality niche content. My refining of this problem allows focus on "hidden gems" by requireing a relation schema that is able to perform sql aggregations before passing the data thorugh a SVD model. I will utilize the strengths of DuckDB for heavy data manipulation and scikit-learn for predictive modeling.

## Motivation
The primary motivation in this project stems from personal interest in high-quality cinmea and the subsequent frustration with the "paradox of choice" that is presented throughout


## Domain Exposition

| Term | Category | Definition | KPI / Importance |
| :--- | :--- | :--- | :--- |
| **Matrix Factorization** | Algorithm | A mathematical method of decomposing a large User-Item interaction matrix into lower-dimensional "latent" tables. | The core logic used to map complex user preferences to specific movie features. |
| **SVD (Singular Value Decomposition)** | Math | A specific linear algebra technique used to reduce the dimensionality of a dataset while preserving its most important features. | The primary model (from DS 4021) used to predict ratings and handle data "noise." |
| **Cold Start** | Domain | The difficulty in providing accurate recommendations for a brand-new movie or user due to a lack of historical interaction data. | A primary challenge that requires the integration of metadata (genres/tags) to solve. |
| **Latent Factors** | ML | Hidden variables such as "cinematic pacing" or "thematic grit" that the model learns to identify from user behavior patterns. | Explains the underlying "vibe" that connects a user to a specific niche movie. |
| **RMSE (Root Mean Square Error)** | KPI | A standard statistical metric that measures the average magnitude of error between the model's predicted rating and the actual user rating. | The lead metric for determining if the recommendation engine is mathematically accurate. |
| **DuckDB** | Engineering | An in-process SQL database management system optimized for fast, analytical queries on large datasets. | Essential for joining and aggregating the 1GB+ relational data files efficiently in Python. |
| **Popularity Bias** | Domain | The tendency for recommendation algorithms to favor mainstream, high-volume content over high-quality but lesser-known titles. | The specific market failure this "Hidden Gem" project is designed to correct. |


This project would operate within the domain of information retriveal and consumer analytics, specifically focusing on personalized recommender systems. In the modern attention economy, the primary challenge for digital platforsm is no longer simply storing the content, but efficiently filtering theroguh the massive datasets to lower and mitigate the choice overload of end users.


| Title | Brief Description | Link to File |
| :--- | :--- | :--- |
| **The Long Tail** | A foundational theory by Chris Anderson on why niche products (Hidden Gems) are becoming more economically viable than mainstream hits. | [Link to File](https://myuva-my.sharepoint.com/:b:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/Background%20Reading/2110.02686v1.pdf?csf=1&web=1&e=w4RA47) |
| **Matrix Factorization for Recommender Systems** | The definitive research paper by Yehuda Koren explaining how SVD functions in the context of the Netflix Prize. | [Link to File](https://myuva-my.sharepoint.com/:b:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/Background%20Reading/lecture25-mf.pdf?csf=1&web=1&e=0M2zSr) |
| **MovieLens 32M Dataset Documentation** | Official 2024 summary from GroupLens detailing the structure and provenance of the 32 million ratings. | [Link to File](https://myuva-my.sharepoint.com/:b:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/Background%20Reading/2504.01863v2.pdf?csf=1&web=1&e=HxOyom) |
| **Tackling the Cold Start Problem** | A technical overview of how metadata (genres/tags) can be used to recommend new items that have low initial ratings. | [Link to File](https://myuva-my.sharepoint.com/:b:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/Background%20Reading/lecture25-mf.pdf?csf=1&web=1&e=ZvQIR2) |