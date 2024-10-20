def run_insecure_api():
    print("Insecure API is running...")
    # Simulate running an insecure server
    # Ensure passwords and MFA tokens are not hashed (for demonstration purposes)
    username = "user"
    password = "password"
    mfa_token = "123456"
    print(f"Username: {username}, Password: {password}, MFA Token: {mfa_token}")

if __name__ == "__main__":
    run_insecure_api()
