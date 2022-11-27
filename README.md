### Домашняя работа по лекции «Регулярные выражения»

[Задание](https://github.com/netology-code/py-homeworks-advanced/tree/master/5.Regexp)

------------ 
Есть файл с адресной книгой, в которой совершенно невозможно кого-то нормально найти: мешает множество дублей и разная запись одних и тех же имен.

Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/

Задача: починить адресную книгу, используя регулярные выражения.

Структура данных будет всегда:
lastname,firstname,surname,organization,position,phone,email
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:

поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
объединить все дублирующиеся записи о человеке в одну.