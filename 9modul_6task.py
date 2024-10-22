# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j+i+1]
    # for i in range(len(text) - 0): # для себя, чтобы потом цикл написать, выше...
    #     yield text[i:i+1]
    # for i in range(len(text) - 1):
    #     yield text[i:i+2]
    # for i in range(len(text) - 2):
    #     yield text[i:i+3]


# Пример работы функции:


a = all_variants("abc")
for i in a:
    print(i)
    # print(i) # примечание: работает только один раз, за то экономим время, память

