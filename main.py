def display_menu():
    print("\nWelcome to Elite Bank!")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Login selected (not built yet)")
        elif choice == '2':
            print("Create Account selected (not built yet)")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
