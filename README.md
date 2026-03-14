# SecureData-Flow: End-to-End Secure ETL Pipeline 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Security: PII-Protected](https://img.shields.io/badge/Security-PII--Protected-green.svg)](#-security-first-features)

##  Executive Summary
**SecureData-Flow** is a robust Python-based ETL pipeline designed to bridge the gap between Data Engineering and Cybersecurity. While most pipelines focus solely on movement, this project implements **Zero-Trust principles** by automating data privacy (PII masking) at the point of ingestion and providing cloud-ready IAM access controls.

## 🛠️ Architecture & Tech Stack
- **Engine:** Python 3.x utilizing `Pandas` for high-performance data transformation.
- **Testing:** `Unittest` framework for automated validation of security logic.
- **Cloud Security:** AWS-standard JSON IAM policies for granular resource control.
- **Automation:** Modular design ready for integration with AWS Lambda or GitHub Actions.

##  Security-First Features
- **Automated PII Redaction:** High-risk fields (Emails, Geolocation) are masked using custom regex-based logic before being persisted to disk.
- **Environment Isolation:** Pre-configured `.gitignore` to prevent accidental leakage of sensitive credentials or logs.
- **Access Governance:** Includes pre-defined IAM policies to enforce the **Principle of Least Privilege (PoLP)** for S3 bucket storage.

##  Project Structure
```text
├── data/               # Secure local storage (git-ignored)
├── iam_policies/       # AWS-standard JSON access controls
├── logs/               # Automated pipeline execution history
├── scripts/            # Core ETL and Masking logic
└── tests/              # Automated unit tests for security validation
## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone https://github.com/otieno-creator/secure-data-pipeline.git
   cd secure-data-pipeline
...
