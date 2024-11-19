class Animal:
    def __init__(self,birth_type="unknown",appearance="unknown",blooded = "unknown"):
        self.__birth_type = birth_type
        self.__appearance = appearance
        self.__blooded = blooded

        @property
        def birth_type(self):
            return self.__birth_type

        @birth_type.setter
        def birth_type(self,birth_type):
            self.__birthtype = birth_type

        @property
        def appearance(self):
            return self.__appearance

        @appearance.setter
        def appearance(self, appearance):
            self.__appearance = appearance

        @property
        def blooded(self):
            return self.blooded

        @birth_type.setter
        def blooded(self, blooded):
            self.__blooded= blooded

    def __str__(self):
        return "A is {}, it has {}, and it is {}".format(self.__birth_type,self.__appearance,self.__blooded)



class Mammals(Animal):
    def __init__(self,birth_type="born alive",appearance="hairy",blooded = "warm-blooded", nurse_young= True):
        Animal.__init__(self,birth_type,appearance,blooded)
        self.__nurse_young = nurse_young

        @property
        def nurse_young(self):
            return self.__nurse_young

        @nurse_young.setter

        def nurse_young(self,nurse_young):
            self.__nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + "and it has {}, they nnurse their young ones ". format(self.__nurse_young)

class Reptile(Animal):
    def __init__(self,birth_type= "born in an egg", appearance="scally", blooded="cold blooded"):
        Animal.__init__(self,birth_type,appearance,blooded)


def main():
    animal1 = Animal("Bornalive")
    print(animal1.birth_type)
    print(animal1)
    mammal1 = Mammals()
    print(mammal1)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurse_young)


    reptile1 = Reptile()
    print(reptile1.birth_type)
    print(reptile1.appearance)
    print(reptile1.blooded)


main()



