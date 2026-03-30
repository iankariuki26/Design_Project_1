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
The primary motivation in this project stems from personal interest in high-quality cinmea and the subsequent frustration with the "paradox of choice" that is presentsed throughout