class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

king_triton = Parent("Triton", "Blue")
print(king_triton.last_name)

ariel = Child("Triton", "Blue", "plenty!")
print(ariel.last_name)
print(ariel.number_of_toys)
