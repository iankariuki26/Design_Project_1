# **`DS 4320 Project 1: Beyond Blockbuster - The New "Hidden Gem" Discovery Engine"`**

#### This repository contains a full-stack data engineering and analytics pipeline designed to mitigate the ever-present popularity bias in modern media’s recommendation systems. Utilizing the MovieLens 25M dataset, the project implements a robust relational model within DuckDB for the purpose of isolating “Hidden Gems,” which are films with high user acclaim (Avg > 4.0) but low market saturation (50-500 ratings). The system transitions from a heavy SQL-based ETL process to a predictive modeling phase using Singular Value Decomposition (SVD) to map latent user preferences to niche content. The final deliverable includes a 4-table relational schema stored in Parquet format, a production-ready Python pipeline with integrated logging and error handling, and a comparative analysis of how matrix factorization outperforms standard popularity-weighted algorithms in surface-level discovery.

## Name: Ian Kariuki
## Computing ID: epj7rf
## DOI:
## Press Release:
## [Data](https://myuva-my.sharepoint.com/:f:/r/personal/epj7rf_virginia_edu/Documents/Design%20Project%201/ml-25m?csf=1&web=1&e=ieV6WU)
## [MIT License](https://github.com/iankariuki26/Design_Project_1?tab=MIT-1-ov-file#readme)
