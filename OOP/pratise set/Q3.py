class animal:
    def sound(self):
        print("some sound.")

class dog(animal):
    def sound(self):
        print("barks!.")

obj=dog()
obj.sound()