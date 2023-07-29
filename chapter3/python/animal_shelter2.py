'''
The Problem: Animal Shelter
___________________________
An animal shelter, which holds only dogs and cats, operates on strictly first in first out basis.
People must adopt either the oldest(based on arrival time) of all animals at the shelter, 
or they can select whether they would prefer a dog or cat (and will recieve the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to mantain this system
and implement operations such as enQueue, deQueue, deQueueDog, deQueueCat. You may use linked list data structure.
pg 110

pg 672
Hints:

22 - We could consider keeping a single linked list for dogs and cats, and then itreating through it to find the 
first dog or cat. What is the impact of doing this?

56 - Let's suppose we kept seperate lists for dogs and cats. How would we find the oldest animal of any type.


63 -  Think about you would do it in real life. You have a list of dogs in chronological order and a 
list of cats in chrono order. What data would you need to find the oldest animal. How would you mantain this data.
'''
from datetime import datetime
from queue import Queue2, Node

class AnimalShelter:
    def __init__(self):
         #Seperate Queue for dogs
        self.dogQueue = Queue2()
        #Seperate  queue for cats
        self.catQueue = Queue2()

    def enQueue(self, animal, animalType):
        if animalType == "Dog" or animalType == "dog":
            #Enqueue the animal into dogqueue
            self.dogQueue.enQueue(animal)
        elif animalType == "Cat" or animalType == "cat":
            #enqueue the animal into catqueue
            self.catQueue.enQueue(animal)
        else:
            #raise an error if something other than cat or dog is inputted
            raise ValueError("Invalid animal type")
        
    def deQueue(self):
        #Check if both queues are empty
        if self.dogQueue.isEmpty() and self.catQueue.isEmpty():
            return None
        
        #If either dog que or cat queue is empty , dequeue from the non empty queue
        if self.dogQueue.isEmpty():
            return self.catQueue.deQueue()
        elif self.catQueue.isEmpty():
            return self.dogQueue.deQueue()
        
        #if both queues are non empty, dequeue from the animal that arrived first 
        dogFront = self.dogQueue.peek() # get the oldest dog from the dog queue 
        catFront = self.catQueue.peek() #get the oldest cat from the cat queue
        if dogFront < catFront:
            return self.dogQueue.deQueue()
        else:
            return self.catQueue.deQueue()
        
    def deQueueDog(self):
        return self.dogQueue.deQueue()
    
    def deQueueCat(self):
        return self.catQueue.deQueue()
    

class AnimalShelter2:
    def __init__(self):
        self.dogQueue = Queue2()
        self.catQueue = Queue2()

    def enQueue(self, animal, animalType):
        timestamp = datetime.now() # get the current timestamp
        if animalType == "Dog":
            self.dogQueue.enQueue((animal, timestamp)) #enqeue animal
        elif animalType == "Cat":
            self.catQueue.enQueue((animal, timestamp)) #enqueue animal 
        else:
            raise ValueError("Invalid animal type")
        
    '''def deQueue(self):
        #Checl if both queues are empty
        if self.dogQueue.isEmpty() and self.catQueue.isEmpty():
            return None
        
        #If either dog queue or cat queue is empty, dequeue from the non empty queue
        if self.dogQueue.isEmpty():
            return self.catQueue.deQueue()[0] # return the animal without the time stamp
        elif self.catQueue.isEmpty():
            return self.dogQueue.deQueue()[0] # return the animal without the time stamp
    
        dogFront, dogTimestamp = self.dogQueue.peek() if not self.dogQueue.isEmpty() else (None, None)
        catFront, catTimestamp = self.catQueue.peek() if not self.catQueue.isEmpty() else (None, None)

        
        #if both queues are non-empty, dequeue the animal that ariive last
        if dogTimestamp is not None and (catTimestamp is None or dogTimestamp < catTimestamp):
            return self.dogQueue.deQueue()[0]
        else:
            return self.catQueue.deQueue()[0]'''
    def deQueue(self):
        # Check if both queues are empty
        if self.dogQueue.isEmpty() and self.catQueue.isEmpty():
            return None

        # If either dog queue or cat queue is empty, dequeue from the non-empty queue
        if self.dogQueue.isEmpty():
            return self.catQueue.deQueue()[0]  # return the animal without the timestamp
        elif self.catQueue.isEmpty():
            return self.dogQueue.deQueue()[0]  # return the animal without the timestamp

        dogFront, dogTimestamp = self.dogQueue.peek() if not self.dogQueue.isEmpty() else (None, None)
        catFront, catTimestamp = self.catQueue.peek() if not self.catQueue.isEmpty() else (None, None)

        # if both queues are non-empty, dequeue the animal that arrived first
        if dogFront is not None and (catFront is None or dogTimestamp < catTimestamp):
            return self.dogQueue.deQueue()[0]
        else:
            return self.catQueue.deQueue()[0]

        
    def deQueueDog(self):
        return self.dogQueue.deQueue()[0] if self.dogQueue.peek() else None
    
    def deQueueCat(self):
        return self.catQueue.deQueue()[0] if self.catQueue.peek() else None
    

'''
# Test the animal shelter
shelter = AnimalShelter()  # Create an instance of the AnimalShelter class

shelter.enQueue("Dog1", "Dog")  # Enqueue a dog with name "Dog1" into the animal shelter
shelter.enQueue("Cat1", "Cat")  # Enqueue a cat with name "Cat1" into the animal shelter
shelter.enQueue("Dog2", "Dog")  # Enqueue another dog with name "Dog2" into the animal shelter

print(shelter.deQueue())  # Output: "Dog1" - Dequeue the oldest animal from the animal shelter
print(shelter.deQueueCat())  # Output: "Cat1" - Dequeue the oldest cat from the animal shelter
print(shelter.deQueue())  # Output: "Dog2" - Dequeue the oldest animal from the animal shelter
'''

# Test the animal shelter
shelter = AnimalShelter2()

shelter.enQueue("Dog1", "Dog")
shelter.enQueue("Cat1", "Cat")
shelter.enQueue("Dog2", "Dog")

print(shelter.deQueue())        # Output: "Dog1"
print(shelter.deQueueCat())     # Output: "Cat1"
print(shelter.deQueue())        # Output: "Dog2"