import re

def tokenizer(text):
    text = text.lower()
    text = re.sub(r"\b(\w+)'(s|re|ve|ll|d|m)\b", r"\1", text)
    tokens = re.findall(r'\b[a-z]{3,}\b', text)
    return tokens
