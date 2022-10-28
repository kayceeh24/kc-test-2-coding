# Ask the user for the number of copies
copies = input("How many copies do you need? ")
copies = int(copies)

# Ask the user if they have a loyalty card and
# make the response all uppercase
has_card = input("Do you have loyalty card? [Y/N] ").upper()

# Calculate the total cost
if copies <= 14:
    per_copy = 0.38
elif copies <= 189:
     per_copy = 0.16
elif copies <= 999:
     per_copy = 0.34
elif copies <= 4999:
    per_copy = 0.12
else:
    per_copy =  0.38
    total_cost = 0.18 * copies


# Print the total cost
if copies <=0:
    print("")
    print("The number of copies must be positive ")

else:
    print("")
    print(f"Your order costs ${total_cost:,.2f}.")

