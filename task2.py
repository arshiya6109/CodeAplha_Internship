import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200,
    "META": 220
}

portfolio = []
total_investment = 0

print("=" * 60)
print("           STOCK PORTFOLIO TRACKER")
print("=" * 60)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock:<10} ${price}")

while True:

    stock = input(
        "\nEnter Stock Symbol "
        "(or type 'done' to finish): "
    ).upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Invalid Stock Symbol!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    price = stock_prices[stock]
    investment = price * quantity

    portfolio.append({
        "Stock": stock,
        "Quantity": quantity,
        "Price": price,
        "Value": investment
    })

    total_investment += investment

    print(f"✅ {stock} added successfully!")
    print(f"Investment Value: ${investment}")

print("\n")
print("=" * 60)
print("                PORTFOLIO SUMMARY")
print("=" * 60)

print(
    f"{'Stock':<10}"
    f"{'Qty':<10}"
    f"{'Price':<15}"
    f"{'Value':<15}"
)

print("-" * 60)

for item in portfolio:

    print(
        f"{item['Stock']:<10}"
        f"{item['Quantity']:<10}"
        f"${item['Price']:<14}"
        f"${item['Value']:<14}"
    )

print("-" * 60)
print(f"Total Investment Value: ${total_investment}")

with open("portfolio_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Stock", "Quantity", "Price", "Investment Value"]
    )

    for item in portfolio:

        writer.writerow([
            item["Stock"],
            item["Quantity"],
            item["Price"],
            item["Value"]
        ])

print("\n📁 Portfolio report saved as 'portfolio_report.csv'")
print("✅ Thank you for using Stock Portfolio Tracker!")
