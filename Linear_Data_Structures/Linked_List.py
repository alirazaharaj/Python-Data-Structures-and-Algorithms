class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        

class Linklist:
    def __init__(self):
        self.head = None
    
    def insert_at_begigning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        itr = self.head
        value = ''
        while itr:
            suf = ''
            if itr.next:
                suf = '--->'  
            value += str(itr.data) + suf 
            itr = itr.next
        print(value)

    def length(self):
        itr = self.head
        count=0
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begigning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise exception('Invalid Index..........')
        if index == 0:
            self.insert_at_begigning(data)
        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next
            count+=1
            
    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise exception('Invalid Index..........')
        if index == 0:
            self.head = self.head.next
            pass
        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    def insert_list(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def insert_after_value(self,value,data):
        count=0
        itr = self.head
        while itr:
            if itr.data == value:
                self.insert_at(count+1,data)
                break
            itr = itr.next
            count+=1

    def remove_by_value(self,value):
        count=0
        itr = self.head
        while itr:
            if itr.data == value:
                self.remove_at(count)
                break
            itr = itr.next
            count+=1
        

        
    
if __name__ == '__main__':
    li= Linklist()
    li.insert_at_begigning(5)
    li.insert_at_begigning(8) 
    li.insert_at_begigning(9)
    li.insert_at_end(4)
    li.insert_at(2,6)  
    li.insert_at(2,7)  
    li.insert_at(2,12)  
    li.print()
    li.remove_at(2)
    li.print()
    li.insert_list(['Ali','Haraj'])
    li.insert_after_value('Ali','Raza')
    li.remove_by_value('Haraj')
    li.print()
