# implimented LinkedList in Python


class Node:
    def __init__(self,Data):
        self.Data = Data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    # @return Length of LinkedList
    def length(self):
        length = 0
        temp = self.first
        while(temp):
            length += 1
            temp = temp.next
        return length
    
    # @parm List to create new LinkedList
    def create(self,lst,):
        self.first = Node(lst[0])
        last = self.first
        for i in range(1,len(lst)):
            New_node = Node(lst[i])
            last.next = New_node
            last = last.next
    
    # @parm To insert element at first Position
    def push(self,Data):
        NewNode = Node(Data)
        if self.first:
            NewNode.next = self.first
            self.first = NewNode
        self.first = NewNode
    
    # @parm to append elment to existing LinkedList
    def append(self,Data):
        NewNode = Node(Data)
        temp = self.first
        if temp:
            while(temp):
                if temp.next != None:
                    temp = temp.next
                else: break
            temp.next = NewNode
        else: self.first = NewNode
    
    # @parm to insert element at given index Note index start from 1 
    def insert(self,index,Data):
        NewNode = Node(Data)
        if index>0 and index <= self.length():
            if index==1:
                self.push(Data)
            else:
                temp = self.first
                for i in range(1,index-1):
                    temp = temp.next
                NewNode.next = temp.next
                temp.next =NewNode
        raise IndexError
    
    # To remove an elenment from LinkedList
    def remove(self,Data):
        temp = self.first
        if self.first.Data == Data:
            self.first = temp.next
            del temp
            return
        else:
            while(temp):
                tail = temp
                temp = temp.next
                if temp != None:
                    if Data == temp.Data:
                        tail.next = temp.next
                        del temp
                        return


    # To Display LinkedList
    def display(self):
        temp = self.first
        while(temp):
            print(temp.Data,end=' ')
            temp = temp.next
        print()

def main():
    lst = [2,4,6,8,10,12,14,16]
    ll = LinkedList()
    # ll.create(lst)
    # ll.display()
    # print(ll.length())
    # ll.push(100)
    ll.create(lst)
    ll.remove(1)
    ll.display()



if __name__ == '__main__':
    main()
