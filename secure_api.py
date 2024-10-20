import hashlib

def hash_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def run_secure_api():
    print("Secure API is running...")
    # Simulate running a secure server
    username = "user"
    password = "password"
    mfa_token = "123456"
    print(f"Username: {username}, Password: {hash_value(password)}, MFA Token: {hash_value(mfa_token)}")

if __name__ == "__main__":
    run_secure_api()
