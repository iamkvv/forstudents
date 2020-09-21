
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
https://docs.google.com/presentation/d/e/2PACX-1vShT9L0JJLouWWMs3ZL8hAdu5vjtH4CPyuIh3pPMeFePvSPev0ZewVp8BMLtEXf7pzSKxZhduBnNvTn/pub?start=false&loop=false&delayms=3000
    ============
    
    https://docs.google.com/presentation/d/e/2PACX-1vQtPaFbUzBsBfIKCfR8Ao8BB8Q6eDq9N9TKjiEj3TEn_qE5eNRIYz21s5isZ2uuy-RcRTZgmJk82FfV/pub?start=false&loop=false&delayms=3000

        ============ COSCO ===================
https://www.sysnettechsolutions.com/en/download-cisco-packet-tracer/
