import math
print('\n\t\t |','-'*10,"CALCULATOR",'-'*10,'|')
print('\n\t\t |','_'*7,"Done by UVARAJAN",'_'*7,'|\n')
def get_num1_operation():
    while(True):
        try:
            global num1
            num1=float(input("\t\tenter the number one: "))
            a='all_correct'
            if a=='all_correct':
                break
        except ValueError:
            print("\t\tplz enter the value")
        except KeyboardInterrupt:
            end=input("\n\t\t Do you want to exit (y/n):")
            try:
                if end=='y':
                    print('\n\t\t','#'*10,"Thank You!!",'#'*10,'\n')
                    exit(0)
                else:
                    pass
            except ValueError:
                print("\t\tplz enter the value")
    while(True):
        try:
            global num2
            num2=float(input("\t\tenter the number two: "))
            b='all_correct'
            if b=='all_correct':
                break
        except ValueError:
            print("\t\tplz enter the value")
        except KeyboardInterrupt:
            end=input("\n\t\tDo you want to exit (y/n):")
            try:
                if end=='y':
                    print('\n\t\t','#'*10,"Thank You!!",'#'*10,'\n')
                    exit(0)
                else:
                    pass
            except ValueError:
                print("\t\tplz enter the value")
    a=int(input("\n\t\t 1|-- Addition\n\t\t 2|-- Subtraction\n\t\t 3|-- Multiplication\n\t\t 4|-- division\n\n\t\t Enter your choise: "))
    design()
    if a==1:
        add(num1,num2)
    elif a==2:
        sub(num1,num2)
    elif a==3:
        mul(num1,num2)
    elif a==4:
        div(num1,num2)
    else:
        print("\t\tNone of the above!")
    design()
    dead=input("\t\tDo you want to run again (y/n): ")
    if dead=='y':
        print('\n')
        pass
    else:
        print('\n\t\t','#'*10,"Thank You!!",'#'*10,'\n')
        return -1
def design():
    print('\t\t','-'*20)
def model(i):
    frac, whole=math.modf(i)
    if frac==0.0:
        result=round(i)
    else:
        result=round(i,3)
    return result
def add(a,b):
    c=a+b
    print("\t\t Addition: ",model(c))
def sub(a,b):
    c=a-b
    print("\t\t Subtraction: ",model(c))
def mul(a,b):
    c=a*b
    print("\t\t Multiplication: ",model(c))
def div(a,b):
    try:
        c=a/b
        print("\t\t Division: ",model(c))
    except ZeroDivisionError:
        print("\t\tzeroerror")
def main():
    while(True):
        a=get_num1_operation()
        if a==-1:
            break
main()