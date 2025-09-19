from Car import Car
from Node import Node
class SinglyLinkedListCar:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def isEmpty(self):
        return self.head==None
    
    def addFirst(self, _id, _name, _price):
        x = Car(_id, _name, _price)
        newNode = Node(x)
        if _price >= 30000:
            if self.isEmpty():
                self.head=self.tail=newNode
            else:
                newNode.next=self.head
                self.head=newNode
            
    def displayCar(self):
        cur=self.head        
        print(f"{'ID':<5} {'Name':<20} {'Price':^8}")
        print(f"{'--':<5} {'----':<20} {'--------':^8}")
        while cur:
            print(cur.info)
            cur=cur.next
        print("\n")
        
    #If CarName contain a string "K" then do nothing, otherwise addLast.        
    def addLast(self, _id, _name, _price):
        x = Car(_id, _name, _price)
        newNode = Node(x)
        if "K".lower() not in _name.lower():
            if self.isEmpty():
                self.head=self.tail=newNode
            else:
                self.tail.next=newNode
                self.tail=newNode

    def editCarInfoById(self, _id):
        pass
    
    def removeCarById(self, _id):
        pass
    
    #Insert a new car in front of a car with ID as _id
    def insertPrev(self, newId, newName, newPrice, _id):
        pass
    
    #Insert a new car right after a car with ID as _id
    def insertAfter(self, newId, newName, newPrice, _id):
        pass

    #Display the car list if its name contain nameKeyword
    def searchCarByID(self, _id):
        pass
    
    #Display the car list if its name contain nameKeyword
    def filterCarByName(self, nameKeyword):
        pass
    
    #Display the car list if its price between [price1 and price2]
    def filterCarByPrice(self, price1, price2):
        pass
    
    def sortCarListByPriceAsc(self):
        pass
    
    def sortCarListByPriceDesc(self):
        pass
    
    def displayTheMostExpensiveCar(self):
        pass
    
    def displayTheCheapestCar(self):
        pass
