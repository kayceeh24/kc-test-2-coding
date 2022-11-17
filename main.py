# Ask the user for the number of copies
copies = input("How many copies do you need? ")
copies = int(copies)

# Ask the user if they have a loyalty card and
# make the response all uppercase
has_card = input("Do you have loyalty card? [Y/N] ").upper()

# Calculate the total cost
if copies <= 49:
     total_cost = 0.18 * copies
elif copies <= 199:
     total_cost = 0.16 * copies
elif copies <= 999:
     total_cost = 0.14 * copies
elif copies >= 4999:
     total_cost = 0.12 * copies
elif copies >= 5000:
     total_cost = 0.10 * copies

#Print the total cost
discount = total_cost * 0.10
if copies >= 100 and has_card  == 'Y':
    discounted_cost = total_cost - discount

#Print the output 
print("")
if copies > 0 and has_card == 'N' or copies < 100 and has_card == 'Y':
    print(f"Your order costs ${total_cost:,.2f}.")
elif copies > 100 and has_card == 'Y':
    print(f"Your order costs ${discounted_cost:,.2f}.")
elif copies < 0:
    print("The number of copies must be positive!")