class Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1
    def push(self,ele):
        if self.isfull():
            raise ("出栈")
        else:
            self.stack.append(ele)
            self.top=self.top+1
    def pop(self):
        if self.isempty():
            raise ("栈已满")
        else:
            self.top=self.top-1
            return self.stack.pop()
    def isfull(self):
        return self.top+1==self.size
    def isempty(self):
        return self.top==-1