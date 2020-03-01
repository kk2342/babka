import os
import time
from threading import Thread
try:
    from jojo3_files import *

except Exception as ex:
    print("Произошла ошибка с библеотекой.")
    print("Продробнее:" + str(ex))
    input(">")
    exit(0)
    
def check_death():
    pass

men = man()
jojo = man()
home = house()


class scenes:

    def clear(self):
        global programm
        programm.clear()
    def load(self,name):
        global programm
        programm.load_scene(name)

    def load_scenes_particle(self,name,func):
        global programm
        sc = scene(name,func)
        programm.add_scene(sc)

    def load_scenes(self):
        self.load_scenes_particle("street",self.street)
        self.load_scenes_particle("home",self.home)
        self.load_scenes_particle("shop5",self.shop)
    def cd(self):
        check_death()

    def street(self):
        self.cd()
        while True:
            self.cd()
            self.clear()
            print("Улица:")
            print("1.Пятёрочка")
            print("2.Дом")
            enter = input(">")
            if(enter == ""):
                self.cd()
                continue
            
            elif enter == "2":
                time.sleep(0.3)
                print("Вы идёте домой...")
                time.sleep(1)
                self.load("home")

            elif enter == "1":
                time.sleep(0.3)
                
                time.sleep(1.5)
                self.load("shop5")

    def in_it(self,elem,mass):
        id = -1
        for i in range(len(mass)):
            if mass[i] == elem:
                id = i
                break
        return id

    def how_much_in_it(self,elem,mass):
        how = 0
        for i in range(len(mass)):
            if mass[i] == elem:
                how += 1
        return how


    def shop(self):

        self.cd()
        bag = []
        milk = ["Сметана", "Творог", "Молоко", "Йогурт", "Детский творожок", "Питьевой йогурт", "Молочный коктейль","Кефир", "Ряженка", "Масло", "Сливки","Сыр"]
        milk_count = [60,45,65,35,50,70,110,67,59,160,140,100]
        milk_drink = [false,false,true,false,false,true,true,true,true,false,true,false]

        bread = ["Хлеб", "Булка", "Баранки", "Бублик", "Пончик", "Сочень", "Батон", "Лаваш", "Лепёшка"]
        bread_count = [50,65,43,56,85,70,60,79,45]
        bread_drink=[false,false,false,false,false,false,false,false,false]

        drunk = ["Водка", "Пиво", "Ром", "Коньяк", "Шампанское", "Абсент", "Овечья водка", "Красное вино", "Белое вино", "Энергетик"]
        drunk_count = [1200,140,2000,1900,900,3500,2600,2950,1400,85]
        drunk_drink = [true,true,true,true,true,true,true,true,true,true]

        sweets = ["Печенье", "Шоколадное печенье", "Чупа-чупс", "Конфета", "Шоколадка Альпун Гилд", "Шоколад Малка", "Чизкейк", "Торт", "Фруктовое желе", "Мармелад"]
        sweets_count = [65,79,14,6,49,80,230,340,85,59]
        sweets_drink = [false,false,false,false,false,false,false,false,false,false]
        
        muka = ["Мука", "Кофе", "Какао", "Сахар", "Соль", "Маргарин", "Подсолнечное Масло", "Яйцо", "Дрожжи", "Желатин", "Овсяные хлопья", "Гречневая крупа", "Рисовая крупа", "Хлопья", "Кетчуп", "Сырный соус"]
        muka_count = [60,95,75,45,30,30,65,20,25,30,40,45,40,67,95,80]
        muka_drink = [false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]

        meat = ["Говядина", "Свинина", "Сосиска", "Колбаса", "Оленина", "Курятина", "Баранина"]
        meat_count = [350,320,30,55,500,300,450]
        meat_drink = [false,false,false,false,false,false,false]

        veg = ["Яблоко", "Банан", "Апельсин", "Грейпфрут","Слива", "Груша", "Памела", "Укроп", "Чеснок", "Морковь", "Картошка", "Репа", "Лук", "Зелёный лук", "Помидор","Огурец", "Болгарский перец", "Свёкла", "Капуста"]
        veg_count = [20,30,25,45,20,35,100,25,65,35,30,70,40,30,30,25,50,40,40]
        veg_drink = [false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]

        drink = ["Кока-кола", "Пепси-кола", "Спрайт", "Фанта", "Вода 0.5л", "Холодный чай", "Фруктовый сок", "Дюшес", "Морс", "Миринда", "Минеральная вода"]
        drink_count = [70,55,60,66,35,40,45,40,30,50,45]
        drink_drink = [true,true,true,true,true,true,true,true,true,true,true]

        men.money = 1000;
        time.sleep(0.5)
        print("Вы вошли в пятёрочку...")
        time.sleep(1.5)
        print("Взяли корзину.")
        time.sleep(1.5)
        while True:
            self.clear()
            self.cd()
            print("Пятёрочка:")
            print("1.Молочка")
            print("2.Хлебный отдел")
            print("3.Винный отдел")
            print("4.Отдел сладостей")
            print("5.Мучной отдел")
            print("6.Мясной отдел")
            print("7.Овощной отдел")
            print("8.Напитки")
            print("9.Корзина")
            print("10.Выйти")
            enter = input(">")
            if(enter == ""):
                self.cd()
                continue
            elif enter == "1":
                time.sleep(0.5)
                print("Вы идёте в молочный отдел...")
                time.sleep(1.4)
                while True:
                    self.cd()
                    self.clear()
                    print("Молочка:")
                    for i in range(len(milk)):
                        print(str(i+1) + "." + milk[i] + "(" + str(milk_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(milk[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(milk[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.4)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(milk)):
                                time.sleep(0.3)
                                print("Вы положили " + milk[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(milk[id])
                        except:
                            pass

            elif enter == "2":
                time.sleep(0.5)
                print("Вы идёте в хлебный отдел...")
                time.sleep(1.7)
                while True:
                    self.cd()
                    self.clear()
                    print("Хлебный отдел:")
                    for i in range(len(bread)):
                        print(str(i+1) + "." + bread[i] + "(" + str(bread_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(bread[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(bread[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.6)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(bread)):
                                time.sleep(0.3)
                                print("Вы положили " + bread[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(bread[id])
                        except:
                            pass

            elif enter == "3":
                time.sleep(0.5)
                print("Вы идёте в винный отдел...")
                time.sleep(1.2)
                while True:
                    self.cd()
                    self.clear()
                    print("Винный отдел:")
                    for i in range(len(drunk)):
                        print(str(i+1) + "." + drunk[i] + "(" + str(drunk_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(drunk[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(drunk[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.1)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(drunk)):
                                time.sleep(0.3)
                                print("Вы положили " + drunk[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(drunk[id])
                        except:
                            pass

            elif enter == "4":
                time.sleep(0.5)
                print("Вы идёте в отдел сладостей...")
                time.sleep(1.4)
                while True:
                    self.cd()
                    self.clear()
                    print("Отдел сладостей:")
                    for i in range(len(sweets)):
                        print(str(i+1) + "." + sweets[i] + "(" + str(sweets_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(sweets[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(sweets[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.3)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(sweets)):
                                time.sleep(0.3)
                                print("Вы положили " + sweets[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(sweets[id])
                        except:
                            pass

            elif enter == "5":
                time.sleep(0.5)
                print("Вы идёте в мучной отдел...")
                time.sleep(1.4)
                while True:
                    self.cd()
                    self.clear()
                    print("Мучной отдел:")
                    for i in range(len(muka)):
                        print(str(i+1) + "." + muka[i] + "(" + str(muka_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(muka[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(muka[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.3)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(muka)):
                                time.sleep(0.3)
                                print("Вы положили " + muka[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(muka[id])
                        except:
                            pass

            elif enter == "6":
                time.sleep(0.5)
                print("Вы идёте в мясной отдел...")
                time.sleep(2)
                while True:
                    self.cd()
                    self.clear()
                    print("Мясной отдел:")
                    for i in range(len(meat)):
                        print(str(i+1) + "." + meat[i] + "(" + str(meat_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(meat[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(meat[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.9)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(meat)):
                                time.sleep(0.3)
                                print("Вы положили " + meat[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(meat[id])
                        except:
                            pass

            elif enter == "7":
                time.sleep(0.5)
                print("Вы идёте в овощной отдел...")
                time.sleep(2)
                while True:
                    self.cd()
                    self.clear()
                    print("Овощной отдел:")
                    for i in range(len(veg)):
                        print(str(i+1) + "." + veg[i] + "(" + str(veg_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(veg[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(veg[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.9)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(veg)):
                                time.sleep(0.3)
                                print("Вы положили " + veg[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(veg[id])
                        except:
                            pass

            elif enter == "8":
                time.sleep(0.5)
                print("Вы идёте в отдел напитков...")
                time.sleep(1.6)
                while True:
                    self.cd()
                    self.clear()
                    print("Отдел напитков:")
                    for i in range(len(drink)):
                        print(str(i+1) + "." + drink[i] + "(" + str(drink_count[i]) + "руб)",end='')
                        if(self.how_much_in_it(drink[i],bag) > 0):
                            print("(" + str(self.how_much_in_it(drink[i],bag)) + " у Вас в корзине)")
                        else:
                            print("")

                    print('e.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd()
                        continue
                    elif enter == "e":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы идёте назад...")
                        time.sleep(1.5)
                        break

                    else:
                        self.cd()
                        try:
                            id = int(enter) - 1
                            if(id >= 0 and id <len(drink)):
                                time.sleep(0.3)
                                print("Вы положили " + drink[id] + " в корзину.")
                                time.sleep(1.3)
                                bag.append(drink[id])
                        except:
                            pass

            elif enter == "9":
                while True:
                    self.cd()
                    self.clear()
                    print("Корзина:")
                    print("#####")
                    if(len(bag) < 1):
                        print("Здесь ничего нет.")
                    for i in range(len(bag)):
                        print(str(i+1)+"." + bag[i])

                    print("#####")
                    print("d.Выложить")
                    print("p.Оплатить")
                    print("b.Назад")
                    enter = input(">")
                    if enter == "":
                        self.cd()
                        continue
                    elif enter == "d":
                        try:
                            id = int(input("Введите номер товара:")) - 1
                            if id>= 0 and id < len(bag):
                                time.sleep(0.3)
                                bag.pop(id)
                                print("Удалено.")
                                time.sleep(1.2)
                        except:
                            pass

                    elif enter == "b":
                        self.cd()
                        break

                    elif enter == "p":
                        if(len(bag) < 1):
                            time.sleep(0.3)
                            print("У Вас в корзине ничего нет!")
                            time.sleep(1.2)

                        else:
                            summ = 0
                            summs = []
                            for i in bag:
                                su = 0
                                if i in milk:
                                    su = milk_count[self.in_it(i,milk)]
                                elif i in bread:
                                    su= bread_count[self.in_it(i,bread)]
                                elif i in muka:
                                    su= muka_count[self.in_it(i,muka)]
                                elif i in drunk:
                                    su= drunk_count[self.in_it(i,drunk)]
                                elif i in veg:
                                    su= veg_count[self.in_it(i,veg)]
                                elif i in drink:
                                    su= drink_count[self.in_it(i,drink)]
                                elif i in sweets:
                                    su= sweets_count[self.in_it(i,sweets)]
                                elif i in meat:
                                    su= meat_count[self.in_it(i,meat)]
                                summ += su
                                summs.append(su)
                            ispacket = false
                            time.sleep(0.4)
                            print("Вы стоите в очереди.")
                            time.sleep(random.randint(60,200) / 10)
                            print("Ваша очередь!")
                            time.sleep(1)
                            while True:
                                print("Пакет нужен?(y/n)")
                                y = input(">")
                                if(y == "y"):
                                    ispacket = true
                                    summ += 10
                                    break
                                elif y == "n":
                                    ispacket = false
                                    break
                            time.sleep(1)
                            for i in bag:
                                print("Пип!(" + i + ")")
                                time.sleep(1.2)

                            time.sleep(0.4)
                            print("Итого к оплате - " + str(summ) + " рублей.")
                            time.sleep(1.5)

                            if(men.money >= summ):
                                print("*Вы оплатили покупку*")
                                men.money -= summ
                                time.sleep(1.4)
                                free = men.bag_level - len(men.items)
                                print("*Вы укладываете всё в сумку*")
                                if free < len(bag):
                                    if(ispacket):
                                        for i in range(free):
                                            men.items.append(bag[0])
                                            bag.pop(0)

                                        for i in bag:
                                            home.fridge.append(i)
                                    else:
                                        time.sleep(0.5)
                                        print("Вам пришлось купить пакет, так как всё не влезло в сумку.")
                                        men.money -= 10
                                        
                                        for i in range(free):
                                            men.items.append(bag[0])
                                            bag.pop(0)

                                        for i in bag:
                                            home.fridge.append(i)
                                else:
                                    for i in bag:
                                        men.items.append(i)

                                time.sleep(1.5)
                                print("Вы всё уложили и идёте на выход.")                                      
                                time.sleep(2)
                                self.load("street")

                            else:
                                print("У Вас нет столько денег!")
                                time.sleep(1.2)
                                break



    def home(self):
        while True:
            self.cd()
            self.clear()
            print("Ваш дом:")
            print("1.Спальня")
            print("2.Гостинная")
            print("3.Кухня")
            print("4.Ванная")
            print("5.Выйти на улицу")
            enter = input(">")
            if(enter == ""):
                self.cd()
                continue
            elif enter == "5":
                self.cd()
                time.sleep(0.5)
                print("Вы выходите на улицу...")
                time.sleep(2)
                self.load("street")
                return
            
            elif enter == "1":
                while True:
                    self.cd()
                    self.clear()
                    print("Спальня:")
                    print("1.Кровать")
                    print('2.Книжная полка')
                    print("3.Мои вещи")
                    print('4.Назад')
                    enter = input(">")
                    if(enter == ""):
                        self.cd();
                        continue
                    elif enter == "1":
                        while True:
                            self.cd()
                            self.clear()
                            print("Вы легли на кровать.")
                            print("Поспать?")
                            print("1.Да")
                            print("2.Пожалуй, откажусь.")
                            enter = input(">")
                            if enter == "1":
                                self.cd()
                                if(men.sleepness >= 85):
                                    time.sleep(0.3)
                                    print("Вы не хотите спать!")
                                    time.sleep(1.3)
                                    print("Вы встали с кровати.")
                                    time.sleep(1.3)
                                    break
                                else:
                                    self.cd()
                                    time.sleep(0.5)
                                    otr = 100 - men.sleepness
                                    time_to_sleep = otr / 5
                                    print("Вы улеглись поудобнее...")
                                    time.sleep(1.5)
                                    print("Ваши глаза закрываются...")
                                    time.sleep(1.5)
                                    print("Вы спите.")
                                    time.sleep(2)
                                    if(random.randint(1,4) == 1):
                                        print("Вы видите сон...")
                                        time.sleep(1.5)
                                        dreams = [""]
                                        self.load(random.choice(dreams))

                                    else:
                                        time.sleep(time_to_sleep)
                                    men.hunger -= time_to_sleep / 2
                                    self.cd()
                                    time.sleep(1)
                                    print("Вы проснулись.")
                                    time.sleep(1.4)
                                    print("Вы встали с кровати.")
                                    time.sleep(1.2)
                                    break

                            elif enter == "2":
                                self.cd()
                                time.sleep(0.5)
                                print("Вы встали с кровати.")
                                time.sleep(1.4)
                                break

                    elif enter == "4":
                        self.cd()
                        time.sleep(0.3)
                        print("Вы вышли из спальни.")
                        time.sleep(1)



SceneManager = scenes()
programm = prg("DW_Engine")
SceneManager.load_scenes()
SceneManager.load("street")





