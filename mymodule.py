
def getArray(): #Функция возвращает массив целых чисел, введенных с клав-ры
    
    data=None   #переменная для хранения введенного с клав-ры значения
    li=[]       #массив по умолчанию пуст; будет заполняться с клав-ры в цикле 

    while data != '': #выполнять, пока юзер не нажмет только Enter; 
                      #тогда data станет равна '' и цикл закончится
        data=input(f"Введено элементов - {len(li)}. Введите данные: ")
        
        if data != "" and str.isdigit(data): #если данные не пусты (только Enter) и все символы - цифры
           li.append(int(data))              #преобразует строку в число и добавляет его в массив              
           
    return li #возвращает заполненный массив


def revArray(li):
    i=0
    while i < len(li) // 2:
        li[i], li[len(li)-1-i], i = li[len(li)-1-i], li[i], i+1

    return li


def procArray():
    li= getArray()
    revli=revArray(li)

    print(revli)
    revli.reverse()
    print(revli)


"""
https://taskcode.ru/array/reverse
"""
