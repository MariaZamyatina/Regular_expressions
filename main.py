from pprint import pprint
import csv
import re
import itertools
from heapq import merge

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    dict1 = {'lastname': [], 'firstname': [], 'surname': [], 'organization': [], 'position': [], 'phone': [],
             'email': []}


    list2 = []
    pattern = r"(8|\+7)\s*[(]*(\d{3})*([)])*([-\s]*)(\d{3})([-\s*])*(\d+)([-\s*])*(\d{2})([\s(])*(\w+\.)*(\s)*(\d+)*([)])*"
    for i in contacts_list:
        result = re.sub(pattern, r'+7(\2)\5-\7-\9 \11\13', i[5])

        i[5] = result.strip()





        lastname, firstname, surname = i[0], i[1], i[2]
        list1 = (lastname + ' ' + firstname + " " + surname).split()
        print(list1)

        i[0],i[1],i[2] = list1
        list2.append(list1)

