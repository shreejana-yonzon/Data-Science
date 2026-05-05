def calculate_tax(price, tax_rate):
    tax_amount = (price * tax_rate) / 100
    total_price = price + tax_amount
    return tax_amount, total_price