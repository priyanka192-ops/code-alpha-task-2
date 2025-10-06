# CodeAlpha Internship Project
# Task 2: Stock Portfolio Tracker
# Author: <Your Name>
# Date: <Insert Date>

import csv

# Dictionary of stock symbols with their prices per share (you can add more)
prices = {
    "AAPL": 180,     # Apple
    "TSLA": 250,     # Tesla
    "GOOGL": 140,    # Google
    "AMZN": 175,     # Amazon
    "MSFT": 330      # Microsoft
}

# Initialize total investment and portfolio list
total = 0
portfolio = []

print("📊 Welcome to the Stock Portfolio Tracker!")
print("Available Stocks:", ", ".join(prices.keys()))
print("Type 'done' when you are finished.\n")

# Loop to take user input
while True:
    sym = input("Enter stock symbol (or 'done' to finish): ").upper()
    if sym == "DONE":
        break
    if sym not in prices:
        print("❌ Unknown symbol. Please choose from:", ", ".join(prices.keys()))
        continue

    try:
        qty = int(input(f"Enter quantity for {sym}: "))
    except ValueError:
        print("⚠️ Please enter a valid number for quantity.")
        continue

    value = prices[sym] * qty
    portfolio.append((sym, qty, prices[sym], value))
    total += value
    print(f"✅ Added {qty} shares of {sym} worth ${value}\n")

# Display portfolio summary
print("\n========== Portfolio Summary ==========")
print("{:<10} {:<10} {:<10} {:<10}".format("Symbol", "Qty", "Price", "Value"))
print("---------------------------------------")

for sym, qty, price, value in portfolio:
    print("{:<10} {:<10} {:<10} {:<10}".format(sym, qty, price, value))

print("---------------------------------------")
print(f"💰 Total Investment Value: ${total}")

# Save results to CSV file
if portfolio:
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        writer.writerows(portfolio)
    print("\n📁 Data has been saved to 'portfolio.csv' successfully!")

print("\n✅ Thank you for using the Stock Portfolio Tracker!")
