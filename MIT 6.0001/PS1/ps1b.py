annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

months = 0
while current_savings < down_payment:
    monthly_saved = monthly_salary * portion_saved
    investments = current_savings * r / 12
    current_savings = current_savings + monthly_saved + investments
    months += 1
    if months % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)

print(f"Number of months: {months}")
