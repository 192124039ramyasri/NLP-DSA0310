import re

def main():
    # Sample text
    text = "The email addresses are john.doe@example.com and jane_smith@email.org. Please contact support@example.net."

    # Define a pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches of the pattern in the text
    matches = re.findall(email_pattern, text)

    # Display the matched email addresses
    print("Matched Email Addresses:")
    for match in matches:
        print(match)

    # Use re.search to find the first occurrence of the pattern in the text
    first_match = re.search(email_pattern, text)
    
    # Display the first matched email address
    if first_match:
        print("\nFirst Matched Email Address:")
        print(first_match.group())

if __name__ == "__main__":
    main()
