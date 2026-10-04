class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Animal makes sound.")

class dog(animal):
    def speak(self):
        super().speak()
        print("Dog barks.")

# obj2=animal("cat")
# obj2.speak()

obj=dog("Tomey")
obj.speak()

#supper() is used to call instance or methods of parent class for example
