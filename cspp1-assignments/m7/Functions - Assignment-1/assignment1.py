"""# Functions | Assignment-1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year if a
person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy -
so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
# So your program only prints out one thing: the remaining balance at the
end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) +
(Monthly interest rate x Monthly unpaid balance
"""
def paying_debtoffinayear(balance, annual_interestrate, monthly_paymentrate):
    """
    This function is to calculate the remainning balance
    """
    i = 1
    monthly_interestrate = annual_interestrate/12
    minimum_monthlypayment = monthly_paymentrate*balance
    monthly_unpaidbalance = balance - minimum_monthlypayment
    updated_balanceeachmonth = monthly_unpaidbalance + (monthly_interestrate*monthly_unpaidbalance)
    i = i+1
    while(i <= 12 and i != 1):
        balance = updated_balanceeachmonth
        monthly_interestrate = annual_interestrate/12
        minimum_monthlypayment = monthly_paymentrate*balance
        monthly_unpaidbalance = balance - minimum_monthlypayment
        updated_balanceeachmonth = monthly_unpaidbalance + (monthly_interestrate*monthly_unpaidbalance)
        i = i+1
    print("Remaining balance: "+str(round(updated_balanceeachmonth, 2)))    
def main():
    """
    This is to call the main function
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debtoffinayear(data[0], data[1], data[2])
main()
