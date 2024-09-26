#here we are going to be given a stack and we will have to return several functions whioh create operability in it. The input will be a series of commands and you will need to perform an operation for each one.

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

class MinStack:
    #stacks nativly dont support min function. We are building that.

    def __int__(self):
        self.stack=[]
        self.minstack=[]

    def push(self,val:int) -> None:
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self)->int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
