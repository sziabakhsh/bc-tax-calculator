# BC Tax Calculator

**A Python-based Personal Tax Simulation Engine for British Columbia, Canada.**

This project simulates personal income tax calculations for multiple taxpayers in **British Columbia**, taking into account:

- Federal and provincial tax brackets
- Self-employment income
- Deductible business expenses
- Tax paid and balance calculations
- Visualization of income, taxes, and expenses

---

## 🏗️ Project Structure
bc-tax-calculator/
│
├─ python-tax-engine/
│ ├─ src/
│ │ ├─ main.py # Entry point
│ │ ├─ tax_engine.py # Calculates total tax
│ │ ├─ tax_calculator.py # Tax bracket engine
│ │ ├─ expense_calculator.py # Deductible business expenses
│ │ ├─ data_processor.py # Processes T4 and expense CSVs
│ │ └─ visualization.py # Plots income, tax, and expenses
│ │
│ └─ data/
│ ├─ t4_sample.csv # Sample T4 income data
│ └─ expenses_sample.csv # Sample business expenses


---

## ⚡ Features

- **Federal and BC Tax Calculation:** Accurate tax calculation based on 2024 tax brackets.  
- **Self-Employment Expense Deduction:** Vehicle, fuel, insurance, phone, home office.  
- **Data Processing:** Combines T4 income and expenses for multiple taxpayers.  
- **Balance Calculation:** Shows overpaid or underpaid taxes.  
- **Visualization:** Bar charts for Income vs Tax and Business Expenses.  
- **Flexible & Extendable:** Can add more taxpayers, scenarios, or expenses easily.

---

## 📝 Sample Output


Tax Report:

name  total_income  business_expenses    tax  tax_paid  balance

0 John 65000 0 13243 9000 -4243
1 Sara 52500 4200 10300 5000 -5300
2 Ali 76000 6000 16500 11000 -5500


Visualization charts include:

- **Income vs Tax Paid**  
- **Business Expenses per Person**

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/bc-tax-calculator.git
cd bc-tax-calculator/python-tax-engine/src

Install dependencies:

pip install pandas matplotlib

Run the program:

python main.py
🔧 How it Works

Data Processing:
Reads t4_sample.csv and expenses_sample.csv, merges them by name.

Expense Deduction:
Calculates deductible expenses based on business use percentage.

Tax Calculation:
Adds T4 income + net self-employment income → calculates federal and BC tax.

Output:
Generates a table showing total_income, business_expenses, tax, tax_paid, and balance.

Visualization:
Plots Income vs Tax Paid and Business Expenses per Person using matplotlib.

⚙️ Future Improvements

Add interactive GUI or web dashboard

Allow dynamic scenario simulation (What-if: income increase, expense change)

Export results to Excel or PDF reports

Integrate with .NET Core API for external access

📌 Notes

Tax brackets are based on 2024 Federal and BC rates

Self-employment expenses assume a business use percentage

The project is intended for educational and simulation purposes only, not official tax filing.
