#Creating a stack
def create_stack():
    stack = []
    return stack

#Creating an empty stack
#return boolean value eg:true or false
def check_empty(stack):
    return len(stack) ==0

#Adding items into the stack
def push(stack,item):
    stack.append(item)
    print("Pushed Item: "+item)

#Removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "Stack is empty"
    return stack.pop()

if __name__ == '__main__':
    my_stack = create_stack()
    push(my_stack,str(1))
    push(my_stack, str(2))
    push(my_stack, str(3))
    push(my_stack, str(4))
    push(my_stack, str(5))

    print("Popped Item: "+pop(my_stack))
    print("Popped Item: " + pop(my_stack))
    print("Popped Item: " + pop(my_stack))
    print("Popped Item: " + pop(my_stack))
    print("Popped Item: " + pop(my_stack))
    print("Popped Item: " + pop(my_stack))
    print("My stack after popping an element: "+str(my_stack))

