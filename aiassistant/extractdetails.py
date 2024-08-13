import re

def extractdetails(user_input):
    pattern = r'translate\s+(.*?)\s+to\s+(\w+)'
    match = re.search(pattern, user_input, re.IGNORECASE)
    
    if match:
        phrase = match.group(1).strip()
        target_language = match.group(2).strip()
        return phrase, target_language
    else:
        return None, None
