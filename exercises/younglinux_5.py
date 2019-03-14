year = input("pls enter the year ")
year = int(year)

visoc_days = year / 4
nevisoc_days = year // 400
total_days = (year * 365) + visoc_days - nevisoc_days

print(total_days)
