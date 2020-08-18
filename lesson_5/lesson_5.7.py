#Урок 5 Задание 7
import json
import codecs
profit = {}
profit_str = {}
prof = 0
aver_profit = 0
i = 0
with open('lesson_5.7.txt','r',encoding='utf-8') as my_file:
    for line in my_file:
        name, firm, margin, loss = line.split()
        profit[name] = int(margin) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        aver_profit = prof / i
    else:
        print(f'Все работают в убыток')
    profit_str = {'average_profit': round(aver_profit)}
    profit.update(profit_str)
    print(profit)

with open('profit_final.json', 'w',encoding='utf-8') as write_json:
    json.dump(profit, write_json)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
