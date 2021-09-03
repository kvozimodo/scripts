import re
from collections import Counter
regex = "([0-9]{1,3}[\.]){3}[0-9]{1,3}"
ip_list = []
with open ('apache_logs') as file:
    for line in file:
        adress = re.search(regex, line)
        ip_list.append(adress.group())
        print(adress.group())

count = Counter(ip_list)
print(count.most_common(10))
