def brute_force_attack(username, password_list):
    correct_username = "admin"
    correct_password = "adminpass"
    for password in password_list:
        if username == correct_username and password == correct_password:
            print(f"Credentials found: Username: {username}, Password: {password}")
            return True
    print("Brute force attack failed.")
    return False

if __name__ == "__main__":
    passwords = ["1234", "password", "adminpass", "qwerty"]
    brute_force_attack("admin", passwords)
