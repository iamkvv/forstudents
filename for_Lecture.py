
def getArray(): #Функция возвращает массив целых чисел, введенных с клав-ры
    
    data=None   #переменная для хранения введенного с клав-ры значения
    li=[]       #массив по умолчанию пуст; будет заполняться с клав-ры в цикле 

    while data != '': #выполнять, пока юзер не нажмет только Enter; 
                      #тогда data станет равна '' и цикл закончится
        data=input(f"Введено элементов - {len(li)}. Введите данные: ")
        
        if data != "" and str.isdigit(data): #если данные не пусты (только Enter) и все символы - цифры
           li.append(int(data))              #преобразует строку в число и добавляет его в массив
        else:
            print(f"{data} не является числом")

        if len(li)==5:
            print(f"Введено {len(li)} элементов")
            break
           
    return li #возвращает заполненный массив


def doList():
    a = input("Ведите числа через пробел ")
    a = a.split() #a теперь строка, функция split превращает ее в list
    a = [int(i) for i in a] #приводим эл-ты списка к типу int
    
    for i in range(len(a)//2):
        b = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = b
        
    print(a)

def revArray(li):
    """Реверс массива
    """

    lng = len(li)-1
    
    for idx , el in enumerate(li[0:len(li)//2]):
         li[idx], li[lng-idx] =  li[lng-idx], el

    return li


def procArray():
    li= getArray()
    revli=revArray(li)
  
    print(revli)
   # revli.reverse()
    print("исходный массив",li)


procArray()
