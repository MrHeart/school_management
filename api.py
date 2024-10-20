from insecure_api import run_insecure_api
from secure_api import run_secure_api

def main():
    while True:
        print("1. Run Insecure API")
        print("2. Run Secure API")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            run_insecure_api()
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            if username == "admin" and password == "adminpass":
                run_secure_api()
            else:
                print("Access denied. Administrator privileges required.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
