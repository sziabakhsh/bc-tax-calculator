from tax_rules import FEDERAL_TAX_BRACKETS, BC_TAX_BRACKETS
from tax_calculator import calculate_tax


def calculate_total_tax(income):

    federal_tax = calculate_tax(income, FEDERAL_TAX_BRACKETS)
    bc_tax = calculate_tax(income, BC_TAX_BRACKETS)

    total_tax = federal_tax + bc_tax

    return {
        "income": income,
        "federal_tax": federal_tax,
        "bc_tax": bc_tax,
        "total_tax": total_tax
    }


if __name__ == "__main__":

    income = 56000

    result = calculate_total_tax(income)

    print(result)