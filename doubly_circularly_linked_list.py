class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class CircularLinkedList: 
    def __init__(self):
        self.cursor = None        
        self.size = 0

    def add_after_cursor(self, v):
        #if the list is empty
        if self.cursor is None:
            self.cursor = Node(v)
            self.cursor.next = self.cursor
            self.cursor.prev = self.cursor
        else:
            new_node = Node(v)
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            new_node.next.prev = new_node

        self.size += 1

    def delete_cursor(self):
        pass

    def advance_cursor(self, n: int):
        pass

    def get_value(self):
        pass

    def is_empty(self):
        pass

    def get_size(self):
        pass

    #prints list as a string
    def __str__(self):
        if self.size == 0:
                return '[]'

        result = '[' + str(self.cursor) + " "
        temp = self.cursor.next
        while temp is not self.cursor:
            result += str(temp) + " "
            temp = temp.next
            
        return result +']'
    
def lab_driver():
    a_list = CircularLinkedList()
    try:
        a_list.add_after_cursor(3)
        a_list.add_after_cursor(7)
        print(a_list)
    except:
        if a_list.cursor == None:
            raise ValueError("There is no previous node.")
    
lab_driver()