# implimenting Stack using LinkedList


class Node:
    def __init__(self,Data):
        self.next = None
        self.Data = Data

class Stack:
    def __init__(self):
        self.Top = None
    
    def push(self,Data):
        if self.Top == None:
            self.Top = Node(Data)
        else:
            NewNode = Node(Data)
            NewNode.next=self.Top
            self.Top = NewNode
    
    def pop(self):
        if self.Top != None:
            Data = self.Top.Data
            self.Top = self.Top.next
            return Data
        return 'Stack is Empty'

    def isEmpty(self):
        if self.Top == None:
            return True
        return False
    
    def peek(self,index):
        temp = self.Top
        for i in range(index):
            if temp.next != None:
                temp = temp.next
            else: return 'Index OUT of Bound'
        return temp.Data


    def display(self):
        temp = self.Top
        while temp:
            print(temp.Data)
            temp=temp.next
    
def main():
    st = Stack()
    for i in range(4):
        st.push(i)
    # st.push(22)
    # print(st.isEmpty())
    st.display()
    print('peeked at',st.peek(0))
    # print()






if __name__ == '__main__':
    main()

