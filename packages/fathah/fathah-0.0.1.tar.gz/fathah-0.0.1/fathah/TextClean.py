import re


def remove_diacritics(text):
        return re.sub(r'[\u064B-\u0652]', '', text)