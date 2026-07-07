print("=" * 50)
print("WELCOME TO AI & DATA SCIENCE CAREER GUIDE BOT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}!")
print("I am your Career Guide Chatbot.\n")

while True:
    print("\nChoose an option:")
    print("1. What is AI?")
    print("2. What is Data Science?")
    print("3. Programming Roadmap")
    print("4. Study Motivation")
    print("5. Career Advice")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\nArtificial Intelligence enables machines to learn and make decisions.")

    elif choice == "2":
        print("\nData Science focuses on analyzing data to gain insights.")

    elif choice == "3":
        print("\nRoadmap:")
        print("Python → Data Structures → SQL → Machine Learning → Projects")

    elif choice == "4":
        print("\nSuccess comes from consistent effort every day.")

    elif choice == "5":
        print("\nPractice coding daily, build projects, and keep learning.")

    elif choice == "6":
        print(f"\nThank you, {name}! Best wishes for your career.")
        break

    else:
        print("\nInvalid choice. Please try again.")