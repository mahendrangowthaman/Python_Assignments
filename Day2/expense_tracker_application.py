expenses = []

n = int(input("Enter number of days: "))

for i in range(n):
    amount = float(input(f"Enter expense for day {i+1}: "))
    expenses.append(amount)

total = 0
for e in expenses:
    total += e

average = total / n

expenses.sort()
minimum = expenses[0]
maximum = expenses[-1]

print("\n----- Expense Report -----")
print("Total Expense   :", total)
print("Average Expense :", average)
print("Minimum Expense :", minimum)
print("Maximum Expense :", maximum)
