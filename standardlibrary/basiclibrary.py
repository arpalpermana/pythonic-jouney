from datetime import datetime

date_now = datetime.now()
print(f"date & time : {date_now}")
print(f"day : {date_now.strftime('%A')}")
print(f"month : {date_now.strftime('%B')}")
print(f"year : {date_now.year}")

from collections import Counter

letter = [x for x in "abccdeaaadsaadsa"]
print(Counter(letter))

import io

file_text = open("standardlibrary/text_file.txt", "r")

print(file_text.read())
