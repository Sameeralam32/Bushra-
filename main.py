import time
import random
from colorama import Fore,init

init()

class Hack_Insta_Gram:
    def __init__(self , users , x):
        self.users = users
        self.x = x -1
    def get_info___(self):
        return f'{Fore.CYAN}{self.x:3}% Hacked to : $ {self.users} $ '
    def get_info_complete(self):
        return f'{Fore.LIGHTBLUE_EX}{self.x:3}% Hacked to : {self.users}  comming to complete.'
    def complete(self):
        return f'{Fore.GREEN}{self.x:3}% username: [ {self.users} ] password: [ {password_generator()} ] ### <<< HACKED >>> ###'

def password_generator():

    num_gen = '1234567890*&#~'

    password = ''.join(random.choice(num_gen)for i in range(10))

    return password

users_for_hacking = input("Enter username: ")

for i in ''.join(users_for_hacking):
    print(i)

for x in range(1,102):
    newUsers = Hack_Insta_Gram(users_for_hacking , x)
    time.sleep(.6)
    if x == 70 :
        print(newUsers.get_info_complete())
    elif x == 100:
        print(newUsers.complete())
        print(Fore.RED + "follow my instagram : aliashooooooooouri")
    elif x == 1:
        print(Fore.GREEN + 'checked proxy list pls wait')
        time.sleep(9.99)
        print('Connected To Proxy list ')
        time.sleep(.9)
        print('Connected To Tor ... PLEASE WAITING ,,, #!$')
        time.sleep(6.66)
        print('Connected all ...')
    else:
        print(newUsers.get_info___())
