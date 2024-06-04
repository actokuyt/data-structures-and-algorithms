from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
       
    
############ Exercise One ###########
print("")
print("############ Answers to Exercise One ################")
print("")    

def reverse_string (string) :
    stack = Stack() 
    reversed_string = ""
    for char in string:
        stack.push(char)

    for i in range(stack.size()):
        reversed_string +=  stack.pop()
        
    return reversed_string

print(reverse_string("We will conquere COVID-19"))    

############ Exercise Two ###########
print("")
print("############ Answers to Exercise Two ################")
print("")  

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_parenthesis_balanced (string) :
    stack = Stack()
    open_parenthesis = ["{", "[", "("]
    close_parenthesis = ["}", "]", ")"]
    for char in string:
        if char in open_parenthesis:
            stack.push(char)
        if char in close_parenthesis:
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False
    return stack.size()==0   

        
        
print(is_parenthesis_balanced("({a+b})"))
print(is_parenthesis_balanced("))((a+b}{"))
print(is_parenthesis_balanced("((a+b))"))
print(is_parenthesis_balanced("((a+g))"))
print(is_parenthesis_balanced("))"))
print(is_parenthesis_balanced("[a+b]*(x+2y)*{gg+kk}"))        