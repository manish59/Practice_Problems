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
        current.next=self.root
        self.root.prev=current
    def print_list(self):
        temp=self.root
        while(temp.next!=None):
            temp=temp.next
            if temp==self.root:
                break
            print(temp.data)
    def get_length(self):
        temp=self.root
        self.count=0
        while(temp.next!=None):
            temp=temp.next
            if temp==self.root:
                break
            self.count +=1
        return self.count
a=Double_Linked_List([1,2,3,4,5,6])
print("Print list")
a.print_list()
print(a.get_length())
