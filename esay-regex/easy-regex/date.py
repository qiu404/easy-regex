'''
 # @ Author: Yiming Qiu
 # @ Description: Pre-defined regex module
 # @ Email: yiming404@gmail.com
 '''

import re
import sys
import os

def find(text):
    rules = [
        '(\d{1,2} (?:Jan(?:urary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(?:Nov|Dec)(?:ember)?) \d{4})',
    ]
    return re.match(''.join(rules),text).group(0)

print(find('12 Jan 2012'))