
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_data.csv")

print("CUSTOMER CHURN ANALYSIS")
print("-----------------------")

# Basic information
print("\nDataset Overview:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate churn percentage
churn_count = (df["Churn"] == "Yes").sum()
total_customers = len(df)

churn_rate = (churn_count / total_customers) * 100

print("\nTotal Customers:", total_customers)
print("Churned Customers:", churn_count)
print("Churn Rate:", round(churn_rate, 2), "%")

# Analyze churn by contract
print("\nChurn by Contract:")
print(pd.crosstab(df["Contract"], df["Churn"]))

# Average usage analysis
print("\nAverage Usage:")
print(df.groupby("Churn")["UsageHours"].mean())

# Support calls analysis
print("\nAverage Support Calls:")
print(df.groupby("Churn")["SupportCalls"].mean())

# Monthly charges analysis
print("\nAverage Monthly Charges:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# Visualization 1: Churn distribution
df["Churn"].value_counts().plot(
    kind="bar",
    color=["green", "red"]
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.show()

# Visualization 2: Churn by contract
pd.crosstab(
    df["Contract"], df["Churn"]
).plot(kind="bar", color=["green", "red"])

plt.title("Churn by Contract Type")
plt.xlabel("Contract")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("churn_by_contract.png")
plt.show()

# Save analysis report
report = df.groupby("Churn")[
    ["UsageHours", "SupportCalls", "MonthlyCharges"]
].mean()

report.to_csv("churn_analysis_report.csv")

print("\nAnalysis completed successfully!")
print("Reports and charts generated.")
