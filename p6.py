
item_prices = [2.5, 3.0, 1.75, 4.5]
quantities = [3, 2, 4, 1]
discount_rate = 10  
tax_rate = 8       

total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))

discount_amount = (discount_rate / 100) * total_cost_before_discount

total_cost_after_discount = total_cost_before_discount - discount_amount

tax_amount = (tax_rate / 100) * total_cost_after_discount

final_total_cost = total_cost_after_discount + tax_amount

print(f"Total Cost before Discount: ${total_cost_before_discount:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Total Cost after Discount: ${total_cost_after_discount:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Final Total Cost: ${final_total_cost:.2f}")
