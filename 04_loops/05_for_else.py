staff = [("amit",15),("amit",13),("amit",13)]
for name, age in staff:
  if age >= 18:
    print(f"{name} is eligible to manage the staff")
    break
else:
 print(f"No one is eligible to manage the staff")