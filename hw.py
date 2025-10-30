
gmail_count = 0
filename = "emails.txt"

print("--- Gmail Addresses Found ---")

try:
    with open(filename, "r") as f:
        
        for line in f:
            
            if "@gmail.com" in line:
                
                print(line.strip())
                
                gmail_count += 1

    print(f"Total Gmail addresses found: {gmail_count}")
    print("Solution by: sajjad kadhim kareem")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    