main_dish = str(input())
time_of_day = int(input())
has_voucher =   bool(input())
is_card_payment = bool(input())

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit() 
total_cost = cost
if time_of_day >= 12 and time_of_day <= 15:
    total_cost = total_cost - total_cost*0.15  # Apply lunch discount'
    print("Lunch discount applied")
    print("total Cost is",total_cost)

if has_voucher:
    total_cost = total_cost - total_cost/10 # Apply voucher discount
    print("Voucher discount applied")
    print("total Cost is",total_cost)
if is_card_payment:  # service charge for card payments
    # service_charge =  total_cost*0.05
    total_cost = total_cost + total_cost*0.05
    print("Service charge applied")
    print("total Cost is",total_cost)
# print("total Cost is",total_cost)
print(f"{total_cost:.2f}")
