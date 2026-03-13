import matplotlib.pyplot as plt

def plot_income_vs_tax(df):
    plt.figure(figsize=(8,5))
    plt.bar(df["name"], df["total_income"], label="Total Income", alpha=0.7)
    plt.bar(df["name"], df["tax"], label="Tax Paid", alpha=0.7)
    plt.ylabel("CAD")
    plt.title("Income vs Tax Paid")
    plt.legend()
    plt.show()


def plot_expenses(df):
    plt.figure(figsize=(8,5))
    plt.bar(df["name"], df["business_expenses"], color="orange")
    plt.ylabel("CAD")
    plt.title("Business Expenses per Person")
    plt.show()