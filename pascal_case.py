import re
def to_underscore(string):
    string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return string