import string,random


def demoColumns(letterCount=5, wordCount=50):
    '''
    Демонстрация возможностей List Comprehension и f-строк
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
                      for m in models ]

    print(f'Всего комбинаций: {len(cross)}', end='\n\n')
    
    for product in cross:
        for item in product:
            print(f'{item: <10}', end='')
        print()
    
    #return cross
















######################################


def ff(a,*arg,**kw):
    print(a)
    print(arg)
    if kw: print(kw)

    
