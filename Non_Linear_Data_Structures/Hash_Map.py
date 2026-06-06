class Hashmap:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)] 

    def get_hash(self,key):
        sum=0
        for c in key:
            sum+=ord(c)
        return sum%self.max
    
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found =False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] ==key:
                self.arr[h][idx]=(key,value)
                found=True
        if found==False:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0]==key:
                return kv[1]
        return self.arr[h]
    
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,kv in enumerate(self.arr[h]):
            if kv[0]==key:
                print(f'Dleting index{index}')
                self.arr[h][index]=None

if __name__ == '__main__':
    h= Hashmap()
    h['march 6']=6
    h['march 7']=7
    h['march 11']=11
    h['march 12']=12
    h['march 13']=13
    h['march 17']=17
    h['march 17']=17
    print('\n\n\n',h.arr)
    h['march 17']=19
    h['march 6']=20
    print('\n\n\n\n',h.arr)
    del h['march 17']
    print('\n\n\n\n',h.arr)