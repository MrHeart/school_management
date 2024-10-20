def api_injection_attack(file_content):
    if len(file_content) > 1000:  # Example of no validation
        print("Error: File content too large")
    else:
        print("File uploaded successfully")

if __name__ == "__main__":
    malicious_file = "A" * 1001
    api_injection_attack(malicious_file)
