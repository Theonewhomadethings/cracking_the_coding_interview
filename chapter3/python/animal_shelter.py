import time
from queue import Node, LinkedList

class Animal:
    def __init__(self, name):
        '''
        Initializes a new animal object.

        Args:
            name: eThe name of the animal
        '''
        #Record the time of admission
        self.time_admitted = time.time() 
        #Set the name of the animal
        self.name = name

    
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class AnimalShelter(LinkedList):
    '''
    Enqueues an animal in the shelter

    Args:
        animal: The animal object to be enqueued
    '''
    def enQueue(self, animal):
        #Creates a node for the animal
        animal_node = Node(animal)
        #Insert the node at the end of the shelter
        self.insert(animal_node)

    def deQueueAny(self):
        '''
        Dequeues the oldest animal (any type) from the animal shelter

        Returns:
            The oldest animal object that has been dequeued, or none if the shelter is empty
        '''
        #Remove and return the head node of the shelter
        return super().pop_head()
    
    def deQueueCat(self):
        '''
        Dequeues the oldest cat from the animal shelter

        Returns:
            The oldest cat object that has been dequeued or None if there are no cats in the shelter.
        '''
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            #Check if the current node contains a cat
            if isinstance(curr_node.data, Cat):
                #Remove the current node from the shelter
                prev_node.next_node  = curr_node.next_node
                #Returns the dequeued cat objects
                return curr_node.data
            prev_node = curr_node
            curr_node = curr_node.next_node
        #No cats found in the shelter
        return None
    
    def deQueueDog(self):
        '''
        Dequeues the oldest dog from the animal shelter.

        Returns:
            The oldest dog object that has been dequeued or None if there are no dogs in the shelter.
        '''
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            #Check if the current node contains a dog
            if isinstance(curr_node, Dog):
                #remove the current node from the shelter 
                prev_node.next_node = curr_node.next_node
                #return the dequeued dog object
                return curr_node.data
            prev_node = curr_node
            curr_node = curr_node.next_node
            #no dogs found in the shelter
        return None
    
def test_enQueue():
    '''
    Test function to valdiate the enQueue operation.
    '''
    animal_shelter = AnimalShelter()
    animal_shelter.enQueue(Cat("Fluffy"))
    animal_shelter.enQueue(Dog("Sparky"))
    animal_shelter.enQueue(Cat("Sneezy"))
    assert animal_shelter.size() == 3

test_enQueue()
