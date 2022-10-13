print("Welcome to the tip calculator.")
total_bill = float(input("What was the total? $"))
num_of_people = int(input("How many people are splitting the bill? "))
tip_percentage = float(input("What is the tip percentage? ")) / 100 + 1
total_bill *= tip_percentage
total_per_person = "{:.2f}".format(total_bill / num_of_people)

print(f"Each person should pay: ${total_per_person}.")