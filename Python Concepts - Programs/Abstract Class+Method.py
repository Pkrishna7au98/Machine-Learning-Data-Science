from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("New method working")

class Whiteboard:
    def write(self):
        print("its writing")

class Program:
    def work(self,any):
        print("Its processing")
        any.process()

pc1 = Laptop()

lp1 = Program()
lp1.work(pc1)
