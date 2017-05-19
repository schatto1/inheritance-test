class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color = "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        Parent.show_info(self)
        print("Number of toys - "+self.number_of_toys)

king_triton = Parent("Triton", "Blue")
king_triton.show_info()

ariel = Child("Triton", "Blue", "plenty!")
ariel.show_info()
