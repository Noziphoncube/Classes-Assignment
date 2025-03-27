import re

def extract_emails(text):
    # Regular expression for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses
    emails = re.findall(email_pattern, text)
    
    return emails

# Example usage
text = str(input("Enter text for email extraction \n"))
emails = extract_emails(text)
print("Extracted emails:", emails)


def validate_date(date):
    # Regular expression to match date in YYYY-MM-DD format
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    
    # Validate the date
    if re.match(date_pattern, date):
        return True
    else:
        return False

# Example usage
date = input("Enter date in the format YYYY-MM-DD \n")
is_valid = validate_date(date)
print(f"Is the date valid? {is_valid}")


def replace_word(text, old_word, new_word):
    # Replace all occurrences of old_word with new_word
    updated_text = re.sub(rf'\b{re.escape(old_word)}\b', new_word, text)
    return updated_text

# Example usage
text = "I love programming. Programming is fun."
print(text)
a=input("Enter Word To Be Replaced: ")
b=input("Enter Word For The Replacement: ")
print("")
updated_text = replace_word(text, a, b)
print("Updated text:", updated_text)


def split_by_non_alphanumeric(text):
    # Split the string by all non-alphanumeric characters
    parts = re.split(r'\W+', text)
    return parts

# Example usage
text = input("Enter A Text You Want To Split Word For Word \n")
split_text = split_by_non_alphanumeric(text)
print("Split text:", split_text)





