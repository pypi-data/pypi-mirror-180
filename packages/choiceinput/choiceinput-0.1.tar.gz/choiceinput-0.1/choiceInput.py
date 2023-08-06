import sys
from pynput import keyboard
from pynput.keyboard import Key
from colorama import Fore,init,Back
init();
class ChoiceInput:
    def __init__(self,choices:"list[str]",colored:bool=False,color=Back.CYAN) -> None:
        self.lines=len(choices);
        self.index=0;
        self.choices=choices;
        self.colored=colored;
        self.color=color;
        self.focuses=[False for i in choices]
        self.focuses.insert(self.index,not self.focuses.pop(self.index))
        self.update()
        with keyboard.Listener(on_release=self.on_release,daemon=False) as listener:
            listener.join()
        if len(input(f"\033[A"))>0:
            print(f"\033[A{choices[-1][0]}") if self.index!=(self.lines-1) else (print(f"\033[A({choices[-1][0]}") if not self.colored else print(f"\033[A{self.color}{choices[-1][0]}{Back.RESET}"))
        
    def get(self):
        return self.choices[self.index]
    def update(self):
        for a,b in zip(self.choices,self.focuses):
            if b:
                if self.colored:
                    sys.stdout.write(f"{self.color}{a}\n{Back.RESET}")
                else:
                    sys.stdout.write(f"({a})\n")
            else:sys.stdout.write(f"{a}  \n")
            sys.stdout.flush()
    def on_release(self,key):
        if key == Key.up:
            self.index-=1
            if self.index<0:
                self.index=0;
                return
            sys.stdout.write("\033[A"*self.lines)
            self.focuses.insert(self.index,self.focuses.pop(self.index+1))
            self.update()
            return None

        elif key == Key.down:
            if self.index == self.lines-1:
                self.index=0
            else:self.index+=1
            sys.stdout.write("\033[A"*self.lines)
            self.focuses.insert(self.index,self.focuses.pop(self.index-1))
            self.update()
            return None
        elif key==Key.enter:
            return False
        elif key == Key.esc or key==Key.end or key==Key.right: 
            keyboard.Controller().press(Key.enter)
            return False

if __name__=="__main__":
    print(ChoiceInput(["1 - select something","2 - delete something else","3 - create something"]).get())