# Total Loan Amount = 10,00,000
# rate of interest = 8.40
# monthly rate of interest = 8.40/12

totalLoanAmount = float(input("What is the total loan amount? "))
rateOfInterest = float(input("What is the yearly rate of interest? "))
monthlyPayment = float(input("What will be your monthly payment? "))
noOfMonths = int(input("For how many months you want to see the data? "))
monthlyRateOfInterest = rateOfInterest/100/12

for month in range(noOfMonths):
  monthlyInterest = totalLoanAmount*monthlyRateOfInterest
  moneyOwed = totalLoanAmount + monthlyInterest
  totalLoanAmount = totalLoanAmount - monthlyPayment
  print("Money owed at the start of month", month, "is", moneyOwed)
  print("Interest paid for month", month, "is", monthlyInterest)
  print("Loan remaining at the end of month", month, "is", totalLoanAmount)
  if(totalLoanAmount < 0):
    print("Loan completed in", month, "months.")
    break

