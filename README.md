# 🔐 Users Access Review

A data analysis project to audit employee system access, identify security risks, and track review status across applications.

---

## 📁 Project Structure

```
users-access-review/
│
├── data/
│   └── Users_Access_Review.xlsx     # Source data (Employees + Access Reviews)
│
├── scripts/
│   └── analysis.py                  # Main analysis script
│
├── reports/                         # Auto-generated output reports
│   ├── inactive_users_approved_access.csv
│   ├── high_risk_access.csv
│   └── pending_reviews.csv
│
└── README.md
```

---

## 📊 Data Overview

The Excel file contains two sheets:

### Sheet 1: `Employees`
| Column | Description |
|---|---|
| User_ID | Unique employee identifier |
| Employee_Name | Full name |
| Employee_Email | Work email |
| Department | e.g., IT, Finance, HR, Sales |
| Manager_Name | Reporting manager |
| Employment_Status | Active / Inactive |
| Location | Office city (Mumbai, Bangalore, etc.) |
| Joining_Date | Date of joining |

### Sheet 2: `Access_Reviews`
| Column | Description |
|---|---|
| Review_ID | Unique review record ID |
| User_ID | Links to Employees sheet |
| Application_Name | e.g., Salesforce, SAP, Workday |
| Access_Type | Application / Database / Role Access |
| Access_Level | Admin / Editor / User / Read Only |
| Risk_Level | High / Medium / Low |
| Reviewer_Name | Person who reviewed access |
| Review_Status | Approved / Revoked / Pending |
| Review_Date | Date of review |
| Comments | Notes from reviewer |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/users-access-review.git
cd users-access-review
```

### 2. Install dependencies
```bash
pip install pandas openpyxl
```

### 3. Run the analysis
```bash
python scripts/analysis.py
```

Reports will be saved in the `/reports/` folder.

---

## 🔍 Key Analysis Areas

| # | Analysis | Why It Matters |
|---|---|---|
| 1 | **High-Risk Access** | Identifies entries flagged as high risk across all apps |
| 2 | **Inactive Users with Approved Access** ⚠️ | Ex-employees who still have active system access — security risk |
| 3 | **Pending Reviews** | Access not yet reviewed — may be overdue |
| 4 | **Admin Access Audit** | Who has the highest privilege level and in which apps |
| 5 | **Department-wise Breakdown** | Access review status across all departments |

---

## 📌 Applications Covered

- Salesforce
- SAP
- Workday
- Oracle ERP
- ServiceNow

---

## ⚠️ Security Note

This repository contains **simulated employee and access data**. If you are using real organizational data:
- Keep the repository **Private**
- Never commit real emails, names, or PII to a public repo
- Add `reports/` and `data/` to `.gitignore` if needed

---

## 📋 GitHub Issues (Suggested Tasks)

Use the Issues tab to track work items:

- [ ] Analyze inactive users with approved access
- [ ] Follow up on all Pending + High-Risk reviews
- [ ] Review Admin-level access in Salesforce and SAP
- [ ] Automate monthly review with GitHub Actions

---

## 🛠️ Tech Stack

- **Python 3.x**
- **pandas** — data manipulation
- **openpyxl** — Excel file reading

---

## 📬 Contact

Maintained by: `Your Name`  
Department: `Your Team`  
Last Updated: May 2026
