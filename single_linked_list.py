class Head:
    def __init__(self):
        self.next=None
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Single_Linked_List:
    def __init__(self,data):
        self.data=data
        self.root=Head()
        current=self.root
        for i in self.data:
            #print(i)
            temp=Node(i)
            current.next=temp
            current=temp
            #print(current)
    def print_list(self):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
            print(temp.data)
    def search_list(self,value):
        temp=self.root
        self.value=value
        while(temp.next!=None):
            temp=temp.next
            if temp.data==self.value:
                return "Found"
        return "Not Found"
    def get_length(self):
        self.count=0
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
            self.count=self.count+1
        return self.count
    def insert_at_first(self,value):
        temp=Node(value)
        first_node=self.root.next
        self.root.next=temp
        temp.next=first_node
    def insert_at_end(self,value):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(value)
a=Single_Linked_List([1,2,3,4,5,6])
a.print_list()
#print(a.search_list(15))
print(a.get_length())
a.insert_at_first(100)
a.print_list()
a.insert_at_end(2001)
a.print_list()