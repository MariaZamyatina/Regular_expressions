import csv
import re


def read_file(file):
    with open(file, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        pattern = r"(8|\+7)\s*[(]*(\d{3})*([)])*([-\s]*)(\d{3})([-\s*])*(\d+)([-\s*])*(\d{2})([\s(])*(\w+\.)*(\s)*(\d+)*([)])*"
        for i in contacts_list:
            result = re.sub(pattern, r'+7(\2)\5-\7-\9 \11\13', i[5])
            i[5] = result.strip()
            lastname, firstname, surname = i[0], i[1], i[2]
            list1 = (lastname + " " + firstname + " " + surname).split()
            if len(list1) == 3:
                i[0], i[1], i[2] = list1[0], list1[1], list1[2]
            else:
                i[0], i[1] = list1[0], list1[1]
        double_contacts_list = contacts_list[1:]
        temporary_list2 = []
        for i in double_contacts_list:
            zip_list = []
            temporary_list = []
            for j in contacts_list:
                if i[0] == j[0] and i[1] == j[1]:
                    zip_list.append(list(zip(i, j)))
                for element in zip_list:
                    temporary_list.append(list(map(lambda x: max(x), [x for x in element])))
            temporary_list2.append(tuple(max(temporary_list)))
    phonebook_list = [contacts_list[0]] + list(set(temporary_list2))
    return phonebook_list


def write_to_file(file, list):
    with open(file, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list)

if __name__ == '__main__':
    list = read_file("phonebook_raw.csv")
    write_to_file("phonebook.csv", list)


