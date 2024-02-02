import random
import pyperclip as pc
generate_pass='abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()~,<>;":'
generate_pass_list=[]
generated_pass_list=[]
for char in generate_pass:
    generate_pass_list.append(char)
random.shuffle(generate_pass_list)
random.shuffle(generate_pass_list)
print('\n\t\t |','-'*10,"PASSWORD GENERATOR",'-'*10,'|')
print('\n\t\t |','_'*11,"Done by UVARAJAN",'_'*11,'|\n')
def design():
    print('\t\t','-'*40)
def restart():
        while(True):
            try:
                dead=input("\t\t Do you want to run it again(y/n): ")
                if dead=='n' or dead=='y':
                    if dead=='n':
                        print('\n\t\t','#'*10,"Thank You!!",'#'*10,'\n')
                        exit(0)
                    else:
                        print('\t\t','-'*20,'X','-'*20)
                        break
                else:
                    print("\t\t Enter 'y' for yes or 'n' for no")
            except ValueError:
                print("\t\t plz enter the number!")
            except KeyboardInterrupt:
                print("\n\t\t\t BYE")
                exit(0)
def get_input():
    while(True):
        try:
            get=int(input('\n\t\t Enter the length of the password: '))
            return get
        except ValueError:
            print("\t\t Plz enter the number!")
        except KeyboardInterrupt:
                print("\n\t\t\t BYE")
                exit(0)
def clipboard(clip):
        while(True):
            try:
                dead=input("\t\t Do you want to copy the password to clipboard(y/n): ")
                if dead=='n' or dead=='y':
                    if dead=='y':
                        pc.copy(clip)
                        print("\t\t Password copied to clipboard.")
                        break
                    else:
                        break
                else:
                    print("\t\t Enter 'y' for yes or 'n' for no")
            except ValueError:
                print("\t\t Plz enter the number!")  
            except KeyboardInterrupt:
                print("\n\t\t\t BYE")
                exit(0)
def generator():    
    while(True):
        get=get_input()
        for i in range(get):
            a=random.choice(generate_pass_list)
            generated_pass_list.append(a)
        design()
        print('\t\t ** PASSWORD ** :'," ".join(generated_pass_list))
        clip_text=" ".join(generated_pass_list)
        generated_pass_list.clear()
        design()
        clipboard(clip_text)
        restart()
generator()