fixed_cost = float(input("Enter fixed cost:"))
variable_cost = float(input("Enter variable cost per tiffin:"))
selling_price = float(input("Enter selling price per tiffin:"))
print("\n step1: FORMULA FOR NUMBER OF TIFFINS")
print("n = fixed cost/(selling price - variable cost)")

# step 1: calculate n
n = fixed_cost/(selling_price - variable_cost)
print(f"n = {fixed_cost}/ {selling_price} - {variable_cost}")
print(f"n = {fixed_cost}/ {selling_price - variable_cost}")
print(f"n = {n}")

print("\n step 2:FORMULA FOR PROFIT")
print("profit = n*selling price - [ fixed cost + n*variable cost]")

#step 2: calculate profit 
profit = n*selling_price - (fixed_cost + n*variable_cost)
print(f"profit = ({n}*{selling_price}) - [ {fixed_cost} + ({n}*{variable_cost})]")
print(f"profit = {n}*{selling_price} - [ {fixed_cost} + {n}*{variable_cost}]")
print(f"profit = {n*selling_price} - {fixed_cost + n*variable_cost}")
print(f"profit = {profit}")

#final output
print("\n FINAL RESULTS ")
print(f"Number of tiffins (n) : {n}")
print(f"profit = {profit}")




