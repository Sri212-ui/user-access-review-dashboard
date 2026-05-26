"""
Users Access Review - Analysis Script
======================================
This script analyzes employee access review data to identify:
- High-risk access entries
- Inactive users with approved/active access
- Pending reviews that need attention
- Access patterns by department and application
"""

import pandas as pd
import os

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
FILE_PATH = "data/Users_Access_Review.xlsx"

print("=" * 60)
print("  USERS ACCESS REVIEW — ANALYSIS REPORT")
print("=" * 60)

employees = pd.read_excel(FILE_PATH, sheet_name="Employees")
reviews   = pd.read_excel(FILE_PATH, sheet_name="Access_Reviews")

print(f"\n✅ Loaded {len(employees)} employee records")
print(f"✅ Loaded {len(reviews)} access review records")

# ─────────────────────────────────────────────
# 2. MERGE DATASETS
# ─────────────────────────────────────────────
df = reviews.merge(employees, on="User_ID", how="left")

# ─────────────────────────────────────────────
# 3. SUMMARY STATISTICS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("📊  SUMMARY")
print("─" * 60)
print(f"Total Reviews       : {len(reviews)}")
print(f"Unique Users        : {reviews['User_ID'].nunique()}")
print(f"Unique Applications : {reviews['Application_Name'].nunique()}")

print("\nReview Status Breakdown:")
print(reviews['Review_Status'].value_counts().to_string())

print("\nRisk Level Breakdown:")
print(reviews['Risk_Level'].value_counts().to_string())

# ─────────────────────────────────────────────
# 4. HIGH-RISK ACCESS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("🔴  HIGH-RISK ACCESS ENTRIES")
print("─" * 60)
high_risk = df[df['Risk_Level'] == 'High']
print(f"Total High-Risk Records: {len(high_risk)}\n")

hr_summary = (
    high_risk.groupby(['Application_Name', 'Review_Status'])
    .size()
    .unstack(fill_value=0)
)
print(hr_summary.to_string())

# ─────────────────────────────────────────────
# 5. INACTIVE USERS WITH APPROVED ACCESS  ⚠️
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("⚠️   INACTIVE USERS WITH APPROVED ACCESS (Risk!)")
print("─" * 60)
inactive_approved = df[
    (df['Employment_Status'] == 'Inactive') &
    (df['Review_Status'] == 'Approved')
]
print(f"Count: {len(inactive_approved)}\n")
if not inactive_approved.empty:
    print(
        inactive_approved[
            ['User_ID', 'Employee_Name', 'Department',
             'Application_Name', 'Access_Level', 'Risk_Level']
        ]
        .sort_values('Risk_Level', ascending=False)
        .to_string(index=False)
    )

# ─────────────────────────────────────────────
# 6. PENDING REVIEWS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("⏳  PENDING REVIEWS")
print("─" * 60)
pending = df[df['Review_Status'] == 'Pending']
print(f"Total Pending: {len(pending)}\n")

print("Pending by Application:")
print(pending['Application_Name'].value_counts().to_string())

print("\nHigh-Risk Pending Reviews:")
high_pending = pending[pending['Risk_Level'] == 'High']
if not high_pending.empty:
    print(
        high_pending[
            ['Review_ID', 'User_ID', 'Employee_Name',
             'Application_Name', 'Access_Level', 'Reviewer_Name']
        ].to_string(index=False)
    )
else:
    print("None found.")

# ─────────────────────────────────────────────
# 7. DEPARTMENT-WISE ACCESS REVIEW STATUS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("🏢  DEPARTMENT-WISE REVIEW STATUS")
print("─" * 60)
dept_summary = (
    df.groupby(['Department', 'Review_Status'])
    .size()
    .unstack(fill_value=0)
)
print(dept_summary.to_string())

# ─────────────────────────────────────────────
# 8. ADMIN ACCESS AUDIT
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("🔑  ADMIN ACCESS AUDIT")
print("─" * 60)
admin_access = df[df['Access_Level'] == 'Admin']
print(f"Total Admin-Level Access Records: {len(admin_access)}")
print("\nAdmin Access by Application:")
print(admin_access['Application_Name'].value_counts().to_string())
print("\nAdmin Access by Review Status:")
print(admin_access['Review_Status'].value_counts().to_string())

# ─────────────────────────────────────────────
# 9. EXPORT REPORTS
# ─────────────────────────────────────────────
os.makedirs("reports", exist_ok=True)

# Report 1: Inactive users with approved access
inactive_approved.to_csv(
    "reports/inactive_users_approved_access.csv", index=False
)

# Report 2: All high-risk access
high_risk.to_csv(
    "reports/high_risk_access.csv", index=False
)

# Report 3: Pending reviews
pending.to_csv(
    "reports/pending_reviews.csv", index=False
)

print("\n" + "─" * 60)
print("📁  REPORTS EXPORTED TO /reports/")
print("─" * 60)
print("  → reports/inactive_users_approved_access.csv")
print("  → reports/high_risk_access.csv")
print("  → reports/pending_reviews.csv")
print("\n✅  Analysis complete!")
