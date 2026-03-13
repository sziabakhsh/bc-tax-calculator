import pandas as pd
from tax_engine import calculate_total_tax
from expense_calculator import calculate_deductible_expenses


def process_tax_files(t4_file, expense_file):

    t4_df = pd.read_csv(t4_file)
    exp_df = pd.read_csv(expense_file)

    df = pd.merge(t4_df, exp_df, on="name")

    results = []

    for _, row in df.iterrows():

        business_expenses = calculate_deductible_expenses(row)

        self_income = row["self_employment_income"]

        net_self_income = self_income - business_expenses

        total_income = row["t4_income"] + max(net_self_income, 0)

        tax_result = calculate_total_tax(total_income)

        results.append({
            "name": row["name"],
            "total_income": total_income,
            "business_expenses": business_expenses,
            "tax": tax_result["total_tax"],
            "tax_paid": row["tax_deducted"],
            "balance": row["tax_deducted"] - tax_result["total_tax"]
        })

    return pd.DataFrame(results)