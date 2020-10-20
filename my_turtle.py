from random import randint,choice
import turtle

def race(turtles):
    '''
    Главная функция. Создает объекты черепахи и окна (Turtle и Screen)
    и выполняет остальные функции
    '''
    if turtles > 15:
        print('Черепах должно быть не больше 10')
        return

    turtle.mode("logo")
    trt= turtle.Turtle()
    scr= turtle.Screen()

    g_width,g_height= setgame(turtles,scr,trt)
    
    trts = setturtles(turtles,g_width,g_height)
    
    run(trts,trt,g_width)

    scr.mainloop() #предотвращает закрытие окна после окончания работы программы

    '''
    Задания:
    1. Количество черепах по умолчанию должно быть 5
    2. Если параметр turtles (т.е. кол-во черепах) будет больше 15, приравнять его к 15
    '''

#-------------------------------------

def setgame(turtles, scr, trt):
    '''
    Разметка игрового пространства
    '''
    scr.setup(900, 450 if turtles <=3 else turtles * 60)
    
    game_width, game_height = scr.window_width() * 0.8, scr.window_height() * 0.8

    trt.speed(0)
    trt.penup()
    trt.goto(-game_width / 2, game_height / 2) 
    trt.pendown()
    trt.color('silver')
    for i in range(2): #прямоугольная площадка
        trt.right(90)
        trt.forward(game_width)
        trt.right(90)
        trt.forward(game_height)

    trt.right(180)
    
    for i in range(11): #вертикальные пунктир. линии
        for num in range(10):
            trt.penup()
            trt.forward(game_height / 20)
            trt.pendown()
            trt.forward(game_height / 20)
            
        trt.penup()
        trt.backward(game_height)
        trt.pendown()
        trt.left(90)
        
        trt.forward(game_width / 11)
        trt.write(i*10, align='center')
        
        trt.right(90)

    trt.penup()
    
    return game_width, game_height
    '''
    Задания:
    1.  Сделать пунктир более частым (мелким)
    2. Напишите здесь, какой тип данных возвращает эта функция
    '''

#-------------------------------------

def setturtles(turtles,g_width,g_height):
    '''
        Создание и размещение черепах
    '''
    trts=[]
    colors=['blue', 'red', 'green', 'orange','black', 'yellow','darkblue', 'indigo','seagreen', 'lime','aqua']

    interval = g_height / turtles
    topPos = g_height / 2 - interval / 2

    for i in range(turtles):
        t=turtle.Turtle()
        t.speed(8)
        t.color(choice(colors))
        t.shape('turtle')

        t.goto(-g_width / 2 + 30, topPos - interval * i)
        t.setheading(90)
        t.clear()
        trts.append(t)
 
    return trts
    '''
    Задания:
    1. Установите стартовую позицию черепах точно на первую вертикальную линию с меткой "0"
    '''

#-------------------------------------

def run(trts,trt,game_width):
    #Запуск гонки
    
    win =False
    while not win:
        for idx, t in enumerate(trts):
            t.forward(randint(1,10))

            if t.position()[0] >= game_width / 2 :
                t.turtlesize(2,2,0)
                trt.home()
                trt.write(f'Победила черепaха  {idx +1}', align='center',font=("Arial", 28, "normal"))
                win=True
                break    
    result(trts)
    '''
    Задание:
    1. Напишите здесь, в чем необходимость инспользования функции enumerate
    
    '''
    

#-------------------------------------
def result(trts):
    '''
    Вывод результатов в файл
    '''
    #Генерация списка [(№ черепахи, позиция перепахи по оси Х),...]
    poslist= [(idx+1,tr.position()[0]) for idx, tr in  enumerate(trts)]

    #сортировка списка по убыванию по х-позиции
    res= sorted(poslist,key=lambda t:t[1],reverse=True)

    #создание файлa для записи
    hnd=open('results.txt',"w")
    hnd.write("№"+ "\t" +"Позиция" + '\n')

    #запись в файл
    for t in res:
        hnd.write(str(t[0]) +'\t' + str(t[1]) +'\n')  
    
    hnd.close()

    '''
    Задания:
    1. Вывести в файл только черепах, занявших первые 3 места
    2. Добавить в конец файла запись с номером победившей черепахи - "Победила 1 черепаха"
    3. Добавить в начало файла дату и время подведения итогов
    4. Новые результаты должны не перезаписывать предыдущие, а добавляться к ним 
    '''

#-------------------------------------            

if __name__ == "__main__":
    race(4)

