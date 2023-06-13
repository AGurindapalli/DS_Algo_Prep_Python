class Node:
    def __init__(self,data):
        self.data=data
        self.next_element=None

class LinkedList:
    def __init__(self):
        self.head_node=None
        
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node
    
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data)
        return True
        
    def get_head(self):
        return self.head_node
    
    def insert_at_last(self,lst, data):
        new_node=Node(data)
    
        if lst.get_head() is None:
            self.head_node = new_node
            return
        temp = lst.get_head()
        
        while temp.next_element:
            temp = temp.next_element
        
        temp.next_element=new_node
        return

list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(0, 10):
    list.insert_at_head(i)
list.print_list()

list.insert_at_last(list,100)
list.print_list()

list.insert_at_last(list,101)
list.print_list()

