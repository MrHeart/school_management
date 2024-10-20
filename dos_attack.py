import time

def dos_attack(server_url):
    while True:
        try:
            print(f"Sending request to {server_url}")
            # Simulate server overload by continuously sending requests
            time.sleep(0.1)  # Adjust as needed for testing
        except KeyboardInterrupt:
            print("DoS attack stopped.")
            break

if __name__ == "__main__":
    server_url = "http://localhost:8000"
    dos_attack(server_url)
