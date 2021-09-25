class Critter:
    """фудболист"""
    total = 0

    def status():
        print("Общее число фудболистов", Critter.total)

    def __init__(self, name, hunger=0, boredom=0):
        self.__name = name
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans

    def name(self):
        return self.__name

    def name(self, new_name):
        if new_name == "":
            print("Имя фудболиста не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")


def main():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main2():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main3():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main4():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main5():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main6():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main7():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main8():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main9():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main10():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


def main11():
    crit_name = input("Как вы назовете фудболиста?: ")
    crit = Critter(crit_name)


main()
