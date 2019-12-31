class Head:
    def __int__(self,next=None,prev=None):
        self.next=None
        self.prev=None
class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
class Double_Linked_List:
    def __init__(self,data):
        self.root=Head()
        self.root.prev=None
        current=self.root
        self.data=data
        for i in self.data:
            temp=Node(i)
            current.next=temp
            temp.prev=current
            current=temp
    def print_list(self):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
            print(temp.data)
    def print_reverse_list(self):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
            #print(temp.data)
        #print(temp.data)
        while(temp.prev!=None):
            print(temp.data)
            temp=temp.prev
    def get_length(self):
        temp=self.root
        self.count=0
        while(temp.next!=None):
            self.count +=1
            temp=temp.next
        return self.count
    def insert_at_end(self,value):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
        last_node=Node(value)
        Node.prev=temp
        temp.next=last_node
    def insert_at_first(self,value):
        second_node=self.root.next
        first_node=Node(value)
        self.root.next=first_node
        first_node.prev=self.root
        first_node.next=second_node
        second_node.prev=first_node
a=Double_Linked_List([1,2,3,4,5,6])
print("Print list")
a.print_list()
print("Print list in reverse order")
a.print_reverse_list()
print('total list of elements %d' % a.get_length())
print("Inserting 101 at first of the list")
a.insert_at_first(101)
a.print_list()
print("Inserting 1001 at last")
a.insert_at_end(1001)
a.print_list()