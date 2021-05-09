annual_salary = float(input("Enter your starting annual salary: "))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1_000_000
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

num_guesses = 0

epsilon = 100
low = 0
high = 10_000

saving_rates = (high + low) / 2.0
guess = total_cost
total_salary_and_investment = 0

for i in range(1, 37):  # 3 years
    if i % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)
    total_salary_and_investment += monthly_salary
    investments = total_salary_and_investment * r / 12
    total_salary_and_investment += investments

while abs(guess - down_payment) >= epsilon:
    guess = total_salary_and_investment * (saving_rates/100)

    if guess < down_payment:
        low = saving_rates
    else:
        high = saving_rates
    saving_rates = (high + low) // 2.0
    num_guesses += 1

print(f"Best savings rate: {saving_rates/100:.4f}")
print(f"Steps in bisection search: {num_guesses}")
