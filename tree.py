#Luke's code
#DO NOT ALTER THIS CODE

#IF YOU WANT TO MAKE ANY CHANGES, CONTACT ALINE
#THANKS
#THIS IS NOT QUESTIONING ANYONE'S COMPETENCE, THIS IS ABOUT 
#MAKING SURE EVERYONE HAS THE SAME CODE SO THAT MODULES
#FIT TOGETHER
#!/usr/bin/python
#TODO
#
#   Add an else statement within the go_--- so that I check wether the next
#       node is a question or person and then to display person/question
#       
#

#Where I found the code for the stack http://python-algorithms.readthedocs.org/en/latest/_modules/python_algorithms/basic/stack.html

TOTAL_TRIES = 3

class _Node(object):
    """An internal class that represents a node with a single item
    and a link to the next node.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack(object):
    """An implementation of a simple stack with linked list."""

    def __init__(self):
        """Initialize an empty stack."""
        self._head = None
        self._size = 0

    @property
    def size(self):
        """The number of items in the stack."""
        return self._size

    def isEmpty(self):
        """Check if the stack is empty.

        Returns:
            True if the stack is empty.
            False otherwise.
        """
        return self._size == 0

    def push(self, item):
        """Insert an item to the stack."""
        n = _Node(item)
        n.next = self._head
        self._head = n
        self._size += 1

    def pop(self):
        """Remove and return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        n = self._head
        self._head = self._head.next
        self._size -= 1
        return n.item

    def flush(self):
        while(not self.isEmpty()):
            node = self.pop()

    def peek(self):
        """Return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self._head.item

    def __iter__(self):
        """Return iterator for the stack."""
        current = self._head
        while current:
            yield current.item
            current = current.next

    def __str__(self):
        """String representation of the stack."""
        return " ".join(reversed([str(item) for item in self]))

    def __repr__(self):
        """Representation of the stack."""
        return "Stack(" + str(self) + ")"

class Node:
    def __init__(self, val, question):
        self.yes = None
        self.no = None
        self.dna = None
        self.value = val
        self.question = question
        self.location = ""

class Tree:

    my_stack = Stack()
    direction = ""
    filename = ""
    numberOfTries = 0

    def flush_stack(self):
        self.my_stack.flush()

    def set_filename(self, name):
        self.filename = name

    #Take the entire tree created and write the contents of the tree to a file
    def store_tree(self): 
        if(self.filename == ""):
            print("Invalide file name")
            return

        if(self.root != None):
            f = open(self.filename, 'w')
            self.__store_tree("", self.root, f)

    #Helper function for store_tree function
    def __store_tree(self, path, node, f):
        if(node != None):
            if(path == ""):
                f.write('Root\n')
                f.write(str(node.value) + '\n')
                f.write(str(node.question) + '\n')
            else:
                f.write(path + '\n')
                f.write(str(node.value) + '\n')
                f.write(str(node.question) + '\n')
                
            self.__store_tree(path + "y", node.yes, f)
            self.__store_tree(path + "d", node.dna, f)
            self.__store_tree(path + "n", node.no, f)

    #Append a given node to the the storage file
    def store_node(self, node):
        f = open(self.filename, 'a')
        f.write(node.location + '\n')
        f.write(str(node.value) + '\n')
        f.write(str(node.question) + '\n')

    #Append the node the tree is currently on to the storage file
    def store_current_node(self):
        curr_direction = self.get_direction()
        current_node = self.return_data(curr_direction)

        if(current_node == None):
            print("Cannot append an empty node")
        else:
            self.store_node(current_node)

        print("Value = " + current_node.value)
        print("Question = " + str(current_node.question))
        print("Location = " + current_node.location)

        
    #Takes a file from the user and convert that file to be a tree
    def make_tree_from_file(self):
        f = open(self.filename, 'r')
        counter = 0
        temp_direction = ""
        temp_question = 0
        temp_value = ""

        


        for line in f:
            new_line = line[0:(len(line) - 1)]

            if(counter == 0):
                temp_direction = new_line
                if(temp_direction == "Root"):
                    temp_direction = ""
            elif(counter == 1):
                temp_value = new_line
            elif(counter == 2):
                temp_question = int(new_line)
                if(temp_question == 1):
                    self.add_question(temp_value, temp_direction)
                else:
                    self.add_person(temp_value, temp_direction)
                    
                
            counter = counter + 1
            counter = counter % 3
            #print line[0:(len(line) - 1)]
        
    
    def __init__(self): #Initialization
        self.root = None

    def getRoot(self): #Function to get the root of the tree
        return self.root

    def print_something(self): #Printing function for debugging purpose
        print("something")


    def add_question(self, question, path): #Function that adds a qustion
        if(self.root == None): #If there is no root node, add a qustion there first
            self.root = Node(question, 1) #Add a question to the root
        else:
            self.__add_question(question,path, self.root, path) #Call the __add_question helper function to traverse the tree and then add the question


    def __add_question(self, question, path, node, new_location): #helper function
        if(len(path) == 1):
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    node.yes = Node(question, 1)
                    node.yes.location = new_location
                    #print("location of yes node = " + node.yes.location)
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    node.no = Node(question, 1)
                    node.no.location = new_location
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    node.dna = Node(question, 1)
                    node.dna.location = new_location
        else:
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    #print("yes direction")
                    self.__add_question(question, path[1:len(path) + 1], node.yes, new_location)
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    #print("no direction")
                    self.__add_question(question, path[1:len(path) + 1], node.no, new_location)
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    #print("dna direction")
                    self.__add_question(question, path[1:len(path) + 1], node.dna, new_location)
        
        
    
    def add_person(self, person, path): #Add a person to the tree
        if(self.root == None):
            print("Error. Cannot put character as root")
        else:
            self.__add_person(person, path, self.root, path)

    def __add_person(self, person, path, node, new_location):
        if(len(path) == 1):
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    node.yes = Node(person, 0)
                    node.yes.location = new_location
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    node.no = Node(person, 0)
                    node.no.location = new_location
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    node.dna = Node(person, 0)
                    node.dna.location = new_location
        else:
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    #print("yes direction")
                    self.__add_person(person, path[1:len(path) + 1], node.yes, new_location)
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    #print("no direction")
                    self.__add_person(person, path[1:len(path) + 1], node.no, new_location)
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    #print("dna direction")
                    self.__add_person(person, path[1:len(path) + 1], node.dna, new_location)
        
            
                

    def go_yes(self): #Traverse the tree to the node of the yes parameter
        self.direction = self.direction + "y" #Add a yes to the path taken

        new_node = self.return_data(self.get_direction())

        if(new_node == None):
            return None,None

        return(new_node.value, new_node.question)
        #print("go yes")
        

    def go_no(self): #Traverse the tree to the node of the no parameter
        self.direction = self.direction + "n" #Add a no to the path taken
        new_node = self.return_data(self.direction)

        if(new_node == None):
            return None,None

        return(new_node.value, new_node.question)
        #print("go no")

    def go_dna(self): #Traverse the tree to the node of the dna parameter
        self.direction = self.direction + "d" #Add a dna to the path taken
        new_node = self.return_data(self.direction)

        if(new_node == None):
            return None,None

        return(new_node.value, new_node.question)

    def go_parent(self): #Traverse the tree to the parent of the current node
        if(self.get_direction() == ""):
            return None

        self.direction = self.direction[0:(self.total_moves_left() - 1)]
        new_node = self.return_data(self.direction)

        if(new_node == None):
            return None

        return(new_node.value, new_node.question, new_node.yes, new_node.no, new_node.dna)

    def go_maybe_yes(self): #Go in the yes direction but store the current position in case we need to come back later
        self.my_stack.push(self.get_direction())
        self.my_stack.push("yes")
        return (self.go_yes())

    def go_maybe_no(self): #Go in the no direction but store the current position in case we need to come back later
        self.my_stack.push(self.get_direction())
        self.my_stack.push("no")
        return (self.go_no())

        #This function pops off the top information for the next spot to return to.  It then goes to the oposite of the
        #last direction taken.  It will then reuturn the contents of the next node if there is one.  If there is no next
        #node then it will return None

    def pop_maybe(self):
        self.numberOfTries = self.numberOfTries + 1
        if(self.is_empty() or self.numberOfTries > TOTAL_TRIES):
            #print "3"
            return None, None
        
        last_direction = self.my_stack.pop()
        last_path = self.my_stack.pop()

        #print("Last direction = " + last_direction)
        #print("Last path = " + last_path)

        self.set_direction(last_path)

        if(last_direction == "yes"): #If we went yes last time, we go no the second time
            self.set_direction(self.direction + "n")
        else:
            self.set_direction(self.direction + "y")

        #print self.direction

        new_node = self.return_data(self.direction)

        if(new_node == None):
            #print "2"
            return None,2
        #print "1"
        return(new_node.value, new_node.question)
            


    def is_empty(self):
        return self.my_stack.isEmpty()

    def print_stack(self): #Print the contents of the stack     
        print("Elements in stack : " + str(self.my_stack))

    def print_direction(self): #Print the direction that has been taken
        print("Direction : " + self.direction)

    def total_moves_left(self): #Return the number of moves that the user has traveled
        return len(self.direction)

    def moves_left(self, path): #Return the number of moves left to travel to get to the specific empty node
        return len(self.path)

    def print_tree(self): #Print the tree along with its current position in the tree
        if(self.root != None):
            self.__print_tree("", self.root)

    #Print all of the contents of the tree
    #Data includes nodes current position, Person/Question string, and where it is a question or not (1 =  Question / 0 = Person)       
    def __print_tree(self, path, node):
        if(node != None):

            if(path == ""):
                print("Root : " + node.value + " : " + str(node.question))
            else:
                print(path + " : " + node.value + " : " + str(node.question))
            self.__print_tree(path + "y", node.yes)
            self.__print_tree(path + "d", node.dna)
            self.__print_tree(path + "n", node.no)

    
    def add_person_yes(self, person): #Adds a person to the yes child
        self.go_yes()
        self.add_person(person, self.direction)  

    def add_person_no(self, person): #Adds a person to the yes child
        self.go_no()
        self.add_person(person, self.direction) 

    def add_person_dna(self, person): #Adds a person to the dna child
        self.go_dna()
        self.add_person(person, self.direction) 

    #promt_for_question() should only be called if you hit a location that does not have a node   
    def prompt_for_question(self): #Call this when you want to prompt the user to add a qustion
        print("I want a question") #Debugging print statement 
        question = "This question" #Change this so that what the user inputted is put in here
        self.add_question(question, self.direction) #Add the question to the spot that next empty node
        self.prompt_for_person() #After asking for a question, ask for an answer to that question

    def prompt_for_person(self):
        person = "This person"
        next_spot = "Spot to add the next person (yes/no/dna)"

        if(next_spot == "y"):
            add_person_yes(person)
        if(next_spot == "n"):
            add_person_no(person)
        if(next_spot == "d"):
            add_person_dna(person)

        self.restart_game()

    def restart_game(self): #Restart the position by resetting the direction variable
        self.set_direction("")
        self.flush_stack()

    def set_direction(self, path): #Set the direction variable in the tree
        self.direction = path;

    def get_direction(self): #Get the direction variable in the tree
        return(self.direction)

    #Given the path to a node, this function returns the node at that location if one exists
    def return_data(self, path): 
        if(self.root == None):
             print("Error.  Cannot Access an empty tree")
        if(self.get_direction() == ""):
            return self.getRoot()
        return(self.__return_data(path, self.root))

    #Helper function for return_data
    def __return_data(self, path, node):
        if(len(path) == 1):
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    node = node.yes
                    if(node == None):
                        return None
                    #print("Step 1")
                    return node
            elif(node == None):
                print("What your are trying to access is not a valid position for a leaf")
                return None
            
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    node = node.no
                    if(node == None):
                        return None

                    return node
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    node = node.dna

                    return node
        else:
            if(path[0] == "y"): #If yes, go into the yes parameter of the node
                    #print("yes direction")
                    return(self.__return_data(path[1:len(path) + 1], node.yes))
            elif(path[0] == "n"): #If no, go into the no parameter of the node
                    #print("no direction")
                    return(self.__return_data(path[1:len(path) + 1], node.no))
            elif(path[0] == "d"): #If no, go into the no parameter of the node
                    #print("dna direction")
                    return(self.__return_data(path[1:len(path) + 1], node.dna))
