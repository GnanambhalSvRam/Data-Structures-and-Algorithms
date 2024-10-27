class MinStack:

    def __init__(self):
        self.stack = deque()
        self.elements = 0

    def push(self, val: int) -> None:
        if self.elements == 0:
            self.stack.append(val)
            self.stack.append(val)
        else:
            minVal = self.getMin()
            self.stack.append(val)
            self.stack.append(min(val,minVal))
        self.elements += 1

    def pop(self) -> None:
        if self.elements != 0:
            self.stack.pop()
            self.stack.pop()
            self.elements -= 1
            
    def top(self) -> int:
        if self.elements != 0:
            val = self.stack.pop()
            ret = self.stack[-1]
            self.stack.append(val)
            return ret

    def getMin(self) -> int:
        if self.elements != 0:
            return self.stack[-1]
