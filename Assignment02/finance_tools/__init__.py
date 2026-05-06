from tax import *
from loan import *

def main():
    
    price = float(input("Enter your annual price: "))
    tax_amount = calculate_tax(price, tax_rate = 13)
    print(f"Estimated tax of 20%: Rs.{tax_amount}")
    
    print("\n --------Loan Calculator--------")
    
    p = float(input("Enter loan principal: "))
    r = float(input("Enter annual interest rate (%): "))
    y = float(input("Enter duration in year: "))
    
    emi = calculate_emi(p, r, y)
    print(f"Your monthly EMI: Rs.{emi:,.2f}")

if __name__ == "__main__":
    main()