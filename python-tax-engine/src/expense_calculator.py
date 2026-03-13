def calculate_deductible_expenses(expense_row):

    percent = expense_row["business_use_percent"] / 100

    vehicle = expense_row["vehicle_cost"] * percent
    fuel = expense_row["fuel"] * percent
    insurance = expense_row["insurance"] * percent
    phone = expense_row["phone"] * percent
    home_office = expense_row["home_office"] * percent

    total_expenses = vehicle + fuel + insurance + phone + home_office

    return round(total_expenses, 2)
