class Node:
    def __init__(self,data=None,next=None,pre=None):
        self.data = data
        self.next = next
        self.pre = pre
        

class Linklist:
    def __init__(self):
        self.head = None
    
    def insert_at_begigning(self,data):
        node = Node(data,self.head)
        if self.head:
            self.head.pre = node
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begigning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)
    
    def length(self):
        itr = self.head
        count=0
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise exception('Invalid Index..........')
        if index == 0:
            self.insert_at_begigning(data)
        count=0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next,itr)
                itr.next.pre = node
                itr.next = node
                break
            itr = itr.next
            count+=1

    def print_forward(self):
        if self.head == None:
            print('Link list has no value...............')
            pass
        itr = self.head
        value = ''
        while itr:
            suf = ''
            if itr.next:
                suf = '--->'  
            value += str(itr.data) + suf 
            itr = itr.next
        print(value)
    
    def print_backward(self):
        if self.head == None:
            print('Link list has no value...............')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        value = ''
        while itr:
            suf = ''
            if itr.pre:
                suf = '--->'  
            value += str(itr.data) + suf 
            itr = itr.pre
        print(value)

    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise exception('Invalid Index..........')
        if self.length() == 1:
            self.head = None
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.pre = None
                return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                itr.next.next.pre = itr
                break
            itr = itr.next
            count+=1

if __name__ == '__main__':
    li= Linklist()
    li.insert_at_begigning(5) 
    li.insert_at_begigning(6) 
    li.insert_at_begigning(7) 
    li.print_forward()
    li.print_backward()
    li.remove_at(0)
    li.print_forward()
    li.print_backward()
