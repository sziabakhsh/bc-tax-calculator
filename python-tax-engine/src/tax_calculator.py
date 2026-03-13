def calculate_tax(income, brackets):

    tax = 0
    previous_limit = 0

    for limit, rate in brackets:

        if income > limit:
            taxable_amount = limit - previous_limit
        else:
            taxable_amount = income - previous_limit

        tax += taxable_amount * rate

        previous_limit = limit

        if income <= limit:
            break

    return round(tax, 2)
