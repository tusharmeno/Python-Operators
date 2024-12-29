days = int(input("Enter number of days"))

years = days//365
print(days, "days =", years, "years")

months = (days%365)//30
print(days, "days =", months, "months")

weeks = ((days%365)%30)//7
print(days, "days =", weeks, "weeks")

days1 = ((days%365)%30)%7
print("=", days1, "days")