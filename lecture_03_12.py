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

def one_more_solution(target, str):
    '''Ишем target в str до тех пор, пока поиск успешен.
       После каждого успешного поиска сдвигаем позицию
       начала поиска вправо.
       Вызов: res = one_more_solution('fo','ddfo fo fo fof')
       '''
    
    fnd_index=0
    pos=0
    res=[]

    while fnd_index != -1:
        fnd_index = str.find(target, pos)
        
        if fnd_index >= 0:
            res.append(fnd_index)
            pos = fnd_index + 1

    return res

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

def summa(n):
    if n == 1:
        return 1
    else:
        return n + summa(n - 1)

######################################


def ff(a,b,c):
    print(a,b,c)

def ff1(a,*arg):
    print(a)
    print(arg)
    for i in arg:
        print(i)

def ff2(a,*arg,**kwarg):
    print(a)
    print(arg)
    print(kwarg)
    
def ff3(a,*,b,c):
    print(a,b,c)
    #ff3(1,b=3,c=4) !!!OK
    #ff3(1,3,4) !!!BAD
