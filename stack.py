# base class describing unlimited stack
class Stack:
    def __init__(self):
        self.stack: list[str] = []
        
    def push(self, value: str) -> None:
        if not self.is_full():
            self.stack.append(value)
        else:
            raise OverflowError("Stack is full")
        
    def pop(self) -> str:
        if not self.is_empty():
            return self.stack.pop()
    
    def clear(self) -> None:
        self.stack.clear()
        
    def seek(self) -> str:
        return None if self.is_empty() else self.stack[-1]
    
    def length(self) -> int:
        return len(self.stack)
        
    # unlimited stack can't be full
    def is_full(self) -> bool:
        return False
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def __str__(self) -> str:
        return self.stack.__str__()
    
    
# subclass for stack of defined size
class LimitedStack(Stack):
    def __init__(self, size: int):
        super().__init__()
        self.size: int = size
        
    def is_full(self) -> bool:
        return self.length() >= self.size
    
    
class RunStack:
    def __init__(self):
        self.stack: Stack = None
        
    def main(self):
        usr_size = int(input("Enter stack size (-1 for unlimited stack): "))
        self.stack = Stack() if usr_size < 0 else LimitedStack(usr_size)
        RunStack.show_menu()
        print("Select menu option")
        while True:
            usr_input = input(">")
            if usr_input == '-q':
                break
            self.run_user_command(usr_input)
            
    @staticmethod
    def show_menu() -> None:
        print("\n---MENU---")
        print("1. Push string to stack")
        print("2. Pop string from stack")
        print("3. Get stack length")
        print("4. Check if stack is empty")
        print("5. Check if stack is full")
        print("6. Clear stack")
        print("7. Get upper element")
        print("----------\n")
        
    def run_user_command(self, usr_input: str):
        match usr_input:
            case '-h':
                RunStack.show_menu()
            case '1':
                usr_str = input("Enter string: ")
                self.stack.push(usr_str)
            case '2':
                self.stack.pop()
            case '3':
                print(f"Stack length is {self.stack.length()}")
            case '4':
                print(f"Stack is empty: {self.stack.is_empty()}")
            case '5':
                print(f"Stack is full: {self.stack.is_full()}")
            case '6':
                self.stack.clear()
            case '7':
                print(self.stack.seek())
            case _:
                print(f"Unknown option '{usr_input}'")
                print("\n-h\tshow menu\n-q\tquit\n")
                
                
RunStack().main()