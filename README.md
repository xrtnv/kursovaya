Была реализована функция, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

Были написаны тесты, покрывающие 98% кода.

Из json файла получаются данные об операциях, сортируются по времени, отсеиваются отмененные операции и на экран выводятся последние 5 операций пользователя
