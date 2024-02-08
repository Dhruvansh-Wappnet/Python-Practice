# String Format
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# Output: The price is 49 dollars

txt = "The price is {:.2f} dollars"
print(txt.format(price))
# Output: The price is 49.00 dollars

quantity = 3
itemno = 567
print(f"I want {quantity} pieces of item number {itemno} for {price} dollars.")
# Output: I want 3 pieces of item number 567 for 49 dollars.

myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49 dollars.

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49 dollars.

