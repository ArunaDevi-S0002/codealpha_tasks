import csv
import matplotlib.pyplot as plt


class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self):
        name = input("Stock Name: ").upper()
        qty = int(input("Quantity: "))
        buy_price = float(input("Buy Price: "))
        current_price = float(input("Current Price: "))

        self.stocks[name] = [qty, buy_price, current_price]
        self.save_to_file()

        print(f"{name} added successfully!\n")

    def remove_stock(self):
        name = input("Enter stock name to remove: ").upper()

        if name in self.stocks:
            del self.stocks[name]
            self.save_to_file()
            print("Stock removed successfully!\n")
        else:
            print("Stock not found!\n")

    def search_stock(self):
        name = input("Enter stock name to search: ").upper()

        if name in self.stocks:
            qty, buy, current = self.stocks[name]

            investment = qty * buy
            current_value = qty * current
            profit_loss = current_value - investment

            print("\n===== STOCK DETAILS =====")
            print(f"Stock: {name}")
            print(f"Quantity: {qty}")
            print(f"Buy Price: ₹{buy}")
            print(f"Current Price: ₹{current}")
            print(f"Investment: ₹{investment:.2f}")
            print(f"Current Value: ₹{current_value:.2f}")
            print(f"Profit/Loss: ₹{profit_loss:.2f}\n")
        else:
            print("Stock not found!\n")

    def show_report(self):
        if not self.stocks:
            print("Portfolio is empty!\n")
            return

        print("\n========== PORTFOLIO REPORT ==========")

        total_investment = 0
        total_current = 0

        for name, data in self.stocks.items():
            qty, buy, current = data

            investment = qty * buy
            current_value = qty * current
            profit_loss = current_value - investment

            percentage = (
                (profit_loss / investment) * 100
                if investment != 0 else 0
            )

            total_investment += investment
            total_current += current_value

            status = "PROFIT" if profit_loss >= 0 else "LOSS"

            print(f"\n{name}")
            print(f"Quantity       : {qty}")
            print(f"Buy Price      : ₹{buy}")
            print(f"Current Price  : ₹{current}")
            print(f"Investment     : ₹{investment:.2f}")
            print(f"Current Value  : ₹{current_value:.2f}")
            print(f"{status}         : ₹{profit_loss:.2f}")
            print(f"Change         : {percentage:.2f}%")

        overall_profit = total_current - total_investment

        overall_percentage = (
            (overall_profit / total_investment) * 100
            if total_investment != 0 else 0
        )

        print("\n========== SUMMARY ==========")
        print(f"Total Investment : ₹{total_investment:.2f}")
        print(f"Current Value    : ₹{total_current:.2f}")
        print(f"Overall P/L      : ₹{overall_profit:.2f}")
        print(f"Overall Change   : {overall_percentage:.2f}%\n")

    def show_graph(self):
        if not self.stocks:
            print("Portfolio is empty!")
            return

        stock_names = []
        profits = []

        for name, data in self.stocks.items():
            qty, buy, current = data
            profit = (current - buy) * qty

            stock_names.append(name)
            profits.append(profit)

        plt.figure(figsize=(8, 5))
        plt.bar(stock_names, profits)

        plt.title("Stock Profit/Loss Analysis")
        plt.xlabel("Stock Name")
        plt.ylabel("Profit / Loss (₹)")

        plt.show()

    def save_to_file(self, filename="portfolio.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["Stock", "Quantity", "Buy Price", "Current Price"]
            )

            for name, data in self.stocks.items():
                writer.writerow(
                    [name, data[0], data[1], data[2]]
                )

    def load_from_file(self, filename="portfolio.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                next(reader)

                for row in reader:
                    name = row[0]
                    qty = int(row[1])
                    buy = float(row[2])
                    current = float(row[3])

                    self.stocks[name] = [qty, buy, current]

        except FileNotFoundError:
            pass


def main():
    portfolio = Portfolio()

    portfolio.load_from_file()

    while True:
        print("\n===== SMART PORTFOLIO ANALYZER =====")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Report")
        print("4. Search Stock")
        print("5. Save Portfolio")
        print("6. Load Portfolio")
        print("7. Show Graph")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            portfolio.add_stock()

        elif choice == "2":
            portfolio.remove_stock()

        elif choice == "3":
            portfolio.show_report()

        elif choice == "4":
            portfolio.search_stock()

        elif choice == "5":
            portfolio.save_to_file()
            print("Portfolio saved successfully!\n")

        elif choice == "6":
            portfolio.load_from_file()
            print("Portfolio loaded successfully!\n")

        elif choice == "7":
            portfolio.show_graph()

        elif choice == "8":
            portfolio.save_to_file()
            print("Thank you for using Smart Portfolio Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
