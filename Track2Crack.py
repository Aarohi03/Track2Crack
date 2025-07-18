from studytracker import add_daily_entry
from weeklyanalysis import generate_weekly_report

def show_menu():
    while True:
        print("\n🎯 Welcome to Track2Crack")
        print("1. Add Daily Study Entry")
        print("2. View Weekly Analysis")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_daily_entry()
        elif choice == '2':
            generate_weekly_report()

        elif choice == '3':
            print("👋 Bye! Keep grinding, you got this!!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    show_menu()