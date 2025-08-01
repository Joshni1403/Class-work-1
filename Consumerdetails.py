# Define the Consumer class
class Consumer:
    def __init__(self, name, gender, income):
        self.name = name
        self.gender = gender
        self.income = income

    def display(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Income: ₹{self.income}")

# Create and display consumer objects
consumer1 = Consumer("Ravi", "Male", 45000)
consumer1.display()

consumer2 = Consumer("Anjali", "Female", 52000)
consumer2.display()

consumer3 = Consumer("Suresh", "Male", 61000)
consumer3.display()

consumer4 = Consumer("Divya", "Female", 58000)
consumer4.display()

consumer5 = Consumer("Arun", "Male", 47000)
consumer5.display()
