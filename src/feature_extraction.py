import string

def message_length(text):
    """
    Function to calculate the length of a message.
    
    Parameters:
    text (str): The input message text.
    
    Returns:
    int: The length of the message.
    """
    length = len(text)
    return length

def word_count(text):
    words = text.split() #return the number of words in the message
    return len(words)

def has_money_sign(text):
    if "£" in text or "$" in text:
        return 1
    else:
        return 0

def has_url(text):
    text = text.lower()
    url_patterns = [
        "http", "www.", ".com",
        ".co.uk", ".net", ".org"
    ]
    for p in url_patterns:
        if p in text:
            return 1
    return 0

def has_uppercase(text):
    words = text.split() #split list of words in message
    for word in words:
        if word.isupper() and len(word) >= 3:
            return 1
    return 0

def spam_keyword_count(text):
    spam_keywords = [
        "free", "claim", "prize",
        "cash", "urgent", "win"
    ]
    count = 0
    words = text.lower()

    for char in string.punctuation:
        words = words.replace(char, " ")

    words = words.split()
    for word in words:
        if word in spam_keywords:
            count += 1
    return count

def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

def extract_features(text):
    results = [
        message_length(text),
        word_count(text),
        has_money_sign(text),
        has_url(text),
        has_uppercase(text),
        spam_keyword_count(text),
        count_digits(text)
    ]
    return results 
if __name__ == "__main__":
    sms = ""
    print(extract_features(sms))