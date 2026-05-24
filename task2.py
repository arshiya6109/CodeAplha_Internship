import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200,
    "META": 220
}

portfolio = []


def display_stocks():
    print("\nAvailable Stocks")
    print("-" * 40)

    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<10} ${price}")

    print("-" * 40)


def add_stock():
    stock = input("Enter Stock Symbol: ").upper()

    if stock not in STOCK_PRICES:
        print("Invalid Stock Symbol!")
        return

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    price = STOCK_PRICES[stock]
    value = price * quantity

    portfolio.append({
        "Stock": stock,
        "Quantity": quantity,
        "Price": price,
        "Value": value
    })

    print(f"{stock} added successfully.")


def view_portfolio():

    if not portfolio:
        print("\nPortfolio is empty.")
        return

    print("\nPORTFOLIO SUMMARY")
    print("-" * 70)

    print(
        f"{'Stock':<10}"
        f"{'Qty':<10}"
        f"{'Price':<15}"
        f"{'Value':<15}"
    )

    print("-" * 70)

    total = 0

    for item in portfolio:

        print(
            f"{item['Stock']:<10}"
            f"{item['Quantity']:<10}"
            f"${item['Price']:<14}"
            f"${item['Value']:<14}"
        )

        total += item["Value"]

    print("-" * 70)
    print(f"Total Investment Value: ${total}")


def save_report():

    if not portfolio:
        print("No data to save.")
        return

    with open(
        "portfolio_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Value"]
        )

        for item in portfolio:
            writer.writerow([
                item["Stock"],
                item["Quantity"],
                item["Price"],
                item["Value"]
            ])

    print("Report saved as portfolio_report.csv")


def main():

    while True:

        print("\n" + "=" * 45)
        print("   STOCK PORTFOLIO TRACKER")
        print("=" * 45)

        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Save Report")
        print("5. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            view_portfolio()

        elif choice == "4":
            save_report()

        elif choice == "5":
            print("\nThank you for using the tracker!")
            break

        else:
            print("Invalid choice.")


main()