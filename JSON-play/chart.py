import matplotlib.pyplot as plt

# Sample data
vendors = ['ADP', 'Paychex', 'QuickBooks Payroll', 'Gusto', 'Zenefits', 'UKG']
market_shares = [30, 25, 20, 15, 10, 15]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(market_shares, labels=vendors, autopct='%1.1f%%', startangle=140)
plt.ColorType=[""]
plt.title('Market Share of Payroll Vendors')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
print ("here is the share calculaiton")
for int1 in market_shares:
        print((int1/100)*100)
for int2 in market_shares:
    resulut=(int2 / 115) * 100
    print(f"{resulut:.2f}%")

market_shares = [30, 25, 20, 15, 10]

# Loop 1: Percentage calculation out of 100
for int1 in market_shares:
    result = (int1 / 100) * 100
    print(f"{result:.2f}%")

# Loop 2: Percentage calculation out of 115
for int2 in market_shares:
    result = (int2 / 115) * 100
    print(f"{result:.2f}%")


