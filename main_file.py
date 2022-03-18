#Find the leap year
def is_leap(year):
  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        p=1
      else:
        p=0
    else:
      p=1
  else:
    p=0
  return p
#find the leap year with the selected month 
def days_in_month(year, month):
   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   if is_leap(year)==1:
     month_days[month-1]=29
     print(f"{year} , this year is a leap year.")
     return f"The month number {month}  is { month_days[1]} days"
   else:
     month_days[month-1]=28
     print(f"{year} , this year is not a leap year. The month number {month}  is { month_days[1]} days ")
     return f"The month number {month}  is { month_days[1]} days"
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)