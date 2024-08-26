class Bird:
    wings = True
    beak = True
    plumage = True

    def fly(self):
        print("Машу крыльями, лечу")

    def walk(self):
        pass


class Sparrow(Bird):
    size = 'small'

    def walk(self):
        print("Прыг-прыг")


class Duck(Bird):
    def walk(self):
        print("шагаю")


chizhik = Sparrow()
pyzhik = Sparrow()
utka = Duck()
pyzhik.size = 'medium'

print(chizhik.size)
print(pyzhik.size)
pyzhik.walk()

print(utka.s)