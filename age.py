ageInYears = int(input("Enter your age in years\n"))
decades = ageInYears//10
years = ageInYears%10
message = "You are " + str(decades) + " decades and "+ str(years) + " year(s) old."
print("You are " + str(decades) + " decades and " + str(years) + " year(s) old.")
print("You are", decades, "decades and", years, "year(s) old.", sep=" ")