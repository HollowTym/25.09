class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger=0, boredom=0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
            self.__pass_time()
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
            self.__pass_time()
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
            self.__pass_time()
        else:
            m = "ужасно"
            self.__pass_time()
        return m

    def talk(self):
        print("Меня зовут", self.name,
              ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food=4):
        x1 = input('Сколько вы хотите корма дать?')
        if x1 <= 10 and x1 > 0:
            print("Мррр...  Спасибо!")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger -= x1
            self.__pass_time()
        elif x1 <= 0:
            print('Это слишком мало... Зверюшка недовольна')
            self.__pass_time()
        elif x1 > 10:
            print('Остановитесь!')
            self.__pass_time()

    def play(self, fun=4):
        x2 = input('Сколько времени вы хотите поиграть?')
        if x2 <= 10 and x2 > 0:
            print("Уиии!")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom -= x2
            self.__pass_time()
        elif x2 == 0:
            print('Вы не любите свою зверюшку???')
            self.boredom -= x2
            self.__pass_time()
            self.__pass_time()
        elif x2 >= 11:
            print('Зверюшка устала')
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom -= x2
            self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)
    x1 = input('Сколько вы хотите корма дать?')
    x2 = input('Сколько времени вы хотите поиграть?')
    choice = None
    while choice != "0":
        print("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()

        # кормление зверюшки
        elif choice == "2":
            crit.eat()

        # игра со зверюшкой
        elif choice == "3":
            crit.play()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
