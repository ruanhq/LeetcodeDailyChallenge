#1381. Design a stack with increment operation:
class CustomStack:
    def __init__(self, maxSize):
        self.stack = []
        self.size = maxSize

    def push(self, x):
        if len(self.stack) < self.size:
            self.stack.append(x)
    #pop
    def pop(self):
    	if self.stack:
    	    popElement = self.stack[-1]
    	    self.stack = self.stack[:-1]
    	    return popElement
        else:
            return -1
    #increment:
    def increment(self, k, val):
        for index in range(k):
            self.stack[index] = self.stack[index] + val
