annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

months = 0
while current_savings < down_payment:
    investments = current_savings * r / 12
    current_savings = current_savings + monthly_saved + investments
    months += 1

print(f"Number of months: {months}")
