
class Node:

    def __init__(Self,Data):
        Self.Data = Data
        Self.Next = None

class LinkedList:

    def __init__(self):
        self.Head = None
    
    # To insert Element At the Begining of Node
    def push(self,Data):
        New_Node = Node(Data)
        if self.Head == None:
            self.Head = New_Node
        else:
            New_Node.Next = self.Head
            self.Head = New_Node

     # To insert ELement at end   
    def append(self,Data):
        New_Node = Node(Data)
        if self.Head == None:
            self.Head = New_Node
        else:
            temp = self.Head
            while temp:
                last = temp
                temp = temp.Next
            last.Next = New_Node

    def insertAt(self,position,Data):
        New_Node = Node(Data)
        if position == 0 or position == 1:
            if self.Head == None:
                self.Head = New_Node
            else:
                New_Node.Next = self.Head
                self.Head = New_Node
        else:
            temp = self.Head
            for i in range(1,position):
                tail = temp
                temp = temp.Next
            New_Node.Next = tail.Next
            tail.Next = New_Node

        

    # To Display the Elements in LinkedList
    def display(self):
        temp = self.Head
        while(temp):
            print(temp.Data,end=" --> ")
            temp = temp.Next
            

    

def main():
    lst = LinkedList()
    for i in range(0,10,+2):
        lst.append(i)
    lst.display()

main()