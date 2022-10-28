# Ask the user for the number of copies
copies = input("How many copies do you need? ")
copies = int(copies)

# Ask the user if they have a loyalty card and
# make the response all uppercase
has_card = input("Do you have loyalty card? [Y/N] ")

# Calculate the total cost
if copies <= 49:
     total_costs = 0.18 * copies
elif copies <= 199:
     per_copy = 0.16
elif copies <= 999:
     per_copy = 0.14
elif copies >= 5000:
     per_copy = 0.12
elif copies >= 5000:
     total_costs = 0.10 * copies
# Print the total cost
if copies <=0:
    print()
    print("The number of copies must be positive! ")

else:
    print("")
    print(f"Your order costs ${total_costs:.2f}.")

