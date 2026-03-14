# Secure Data Pipeline 

A Python-based ETL (Extract, Transform, Load) pipeline built with a **Security-First** mindset. This project demonstrates the ability to process data while strictly adhering to data privacy standards.

##  Overview
This pipeline fetches data from external APIs, processes it using **Pandas**, and implements automated **PII (Personally Identifiable Information) masking** to ensure sensitive user data is never stored in plain text.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, Requests
- **Security:** Data Masking, Environment Variable management, `.gitignore` protection

## 🔒 Key Security Features
- **PII Redaction:** Automatically masks emails and sensitive coordinates before local storage.
- **Environment Isolation:** Designed to use `.env` files for API credentials (preventing credential leakage).
- **Audit Logs:** Generates timestamps for every successful data ingestion.

## 📂 Project Structure
- `scripts/`: Core Python logic.
- `data/`: (Local only) Secure storage for processed files.
- `logs/`: Pipeline execution history.

---
*Created by D.O OTIENO - Data Engineering & Cybersecurity Specialist*
