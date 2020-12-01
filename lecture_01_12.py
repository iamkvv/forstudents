import string,random,re

'''Поиск подстроки'''

'''Задача в pythontutor.ru
Найдите в строке второе вхождение буквы f,
и выведите индекс этого вхождения. 
'''
def tutor_solution():
    '''Решение разработчиков'''
    s = 'ofofofofofofofofo'
    
    if s.count('f') == 1:
        print(-1)
    elif s.count('f') < 1:
        print(-2)
    else:
        print(s.find('f', s.find('f') + 1))

    #А если потребуется вывести индекс 5-го вхождения???
#================================================

'''Альтернативное решение'''
def alter_solution(target, str):
    '''Используем генератор списков с фильтром по искомой подстроке (target)
    Проходим в цикле полученный список, функция enumerate формирует
    tuple, содержащий индекс вхождения и само вхождение
    Вызов: res=alter_solution('f','fofofofofo')
    '''
    
    result=[(i,v) for i,v in enumerate(str) if v == target]
    return result
#================================================

'''Лучшее решение - использование регулярных выражений'''
def re_solution(target, str):
    '''Поиск с использованием регулярных выражений - re.finditer.
    Возврашает список, включающий индекс (номер) найденной подстроки
    и начальный и конечный индексы вхождения).
    Вызов: res=re_solution('fa','qwefaaasdfa123fa')
    '''
    result=[]
    iter = re.finditer(target, str) #ищем target в str

    for i, v in enumerate(iter):
        print(i, v.span())
        result.append((i, v.span()))

    return result
#================================================


def demoColumns(letterCount=5, wordCount=50):
    '''
    List Comprehension и f-строки
    '''
    letters = string.ascii_letters
    wordList =  [''.join([random.choice(letters) for i in range(letterCount)] )
                                                 for i in range(wordCount)]

    for i, w in enumerate(wordList, start = 1):
        if i % 3 == 1: print('|', end = "")

        print(f"{w: ^10}", sep='', end = "|")
        
        if i % 3 == 0: print()

######################################

def crossProduct():
    '''
    Произведение списков
    '''
    colours = [ "red", "green", "yellow", "blue" ]
    models = ['light', 'regular', 'premium']
    things = ['bike', 'ski', 'kite']
    
    cross = [ [t,c,m] for t in things
                      for c in  colours
                      for m in models  ]

    print(f'Всего комбинаций: {len(cross)}', end='\n\n')
    
    for product in cross:
        for item in product:
            print(f'{item:.<10}', end='')
        print()
    
    #return cross

######################################


def ff(a,b,c):
    print(a,b,c)

def ff1(a,*arg):
    print(a)
    print(arg)

def ff2(*arg,**kwarg):
    print(arg)
    print(kwarg)
    
def ff3(a,*,b,c):
    print(a)
    #ff3(1,b=3,c=4) !!!OK
    #ff3(1,3,4) !!!BAD

#============================
#python  get-pip.py
#pip -V
def excel():
    import xlsxwriter
    # открываем новый файл на запись
    workbook = xlsxwriter.Workbook('hello.xlsx')
    # создаем там "лист"
    worksheet = workbook.add_worksheet()
    # в ячейку A1 пишем текст
    worksheet.write('A1', 'Hello world')
    # сохраняем и закрываем
    workbook.close()
    
    
    ''' Пишем в файл в цикле
    for item in content :     
        sheet.write(row, column, item)     
        row += 1  
    ''''
    
    
    


    
