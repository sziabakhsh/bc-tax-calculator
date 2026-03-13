from data_processor import process_tax_files
from visualization import plot_income_vs_tax, plot_expenses

if __name__ == "__main__":

    t4_file = "../data/t4_sample.csv"
    expense_file = "../data/expenses_sample.csv"

    result_df = process_tax_files(t4_file, expense_file)

    print("\nTax Report:\n")
    print(result_df)

    # Visualization
    plot_income_vs_tax(result_df)
    plot_expenses(result_df)