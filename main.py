import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
import time
import traceback
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()

try:
    def main():
        os.system('cls')
        print(f"""{Fore.WHITE}
    ██████╗░███████╗████████╗████████╗███████╗██████╗░  ██████╗░░█████╗░██╗░░░██╗
    ██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝
    ██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝  ██║░░██║███████║░╚████╔╝░
    ██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗  ██║░░██║██╔══██║░░╚██╔╝░░
    ██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██║░░██║░░░██║░░░
    ╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

    ░█████╗░░░░░█████╗░░░░░░███╗░░
    ██╔══██╗░░░██╔══██╗░░░░████║░░
    ██║░░██║░░░██║░░██║░░░██╔██║░░
    ██║░░██║░░░██║░░██║░░░╚═╝██║░░
    ╚█████╔╝██╗╚█████╔╝██╗███████╗
    ░╚════╝░╚═╝░╚════╝░╚═╝╚══════╝""")
        print(f'{Fore.RED}(1) Search')
        print(f'{Fore.RED}(2) System')
        print('(0) Exit')
        
        pick = (int(input(f'{Fore.GREEN}What would you like to do? ')))
        
        if pick == 1:
            search()
        if pick == 2:
            system()
        if pick == 0:
            os.system('cls')
            exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')


    def search():
        os.system('cls')
        print(f"""{Fore.WHITE}
    ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
    ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
    ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
    ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
    ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")
        print(f'{Fore.RED}(1)Search Amazon.com')
        print(f'{Fore.RED}(2)Search DuckDuckGo')
        print(f'{Fore.RED}(3)Search YouTube')        
        print(f'{Fore.RED}(4)Search NewEgg')
        print(f'{Fore.RED}(5)Search Google')
        print(f'{Fore.RED}(6)VSCODE Web Builder')
        print('(0)Quit')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.amazon.ca/s?k='+var1+'')
            os.system('py main.py')
        if search == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://duckduckgo.com/?q='+var2+' ')
            os.system('py main.py')
        if search == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.youtube.com/results?search_query='+var3+'')
            os.system('py main.py')
        if search == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('py main.py')
        if search == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.google.com/search?q='+var5+'')
            os.system('py main.py')
        if search == 6:
            os.system('start firefox vscode.dev')
            os.system('py main.py')
        if search == 0:
            os.system('cls')
            sys.exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')






    def system():
        os.system('cls')
        print(f"""{Fore.WHITE}
░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝""")
        print(f'{Fore.RED}(1)Run train')
        print(f'{Fore.RED}(2)HTOP')
        print(f'{Fore.RED}(3)Search directory')
        print(f'{Fore.RED}(4)Clone somthing off of Github.')
        print(f'{Fore.RED}(5)Make a File')
        print(f'{Fore.RED}(7)Check the weather')
        print(f'{Fore.RED}(8)Run system command')
        print(f'{Fore.RED}(0)Exit')
        System = int(input(f'{Fore.GREEN}What would you like to do: '))
        if System == 1:
            os.system('sl')
            os.system('python main.py')
        if System == 2:
            os.system('htop')
            os.system('python main.py')
        if System == 3:
            var7 = str(input(f'{Fore.RED}What directory would you like to search: '))
            os.system('ls '+var7+'')
            os.system('python main.py')
        if System == 4:
            var8 = str(input(f'{Fore.RED}What would you like to clone: '))
            os.system('git clone '+var8+'')
            os.system('python main.py')
        if System == 5:
            var9 = str(input(f'{Fore.RED}What file would you like to make. EX python.py: '))
            os.system('type nul > '+var9+'')
            os.system('python main.py')
        if System == 8:
            var10 = str(input(f'{Fore.RED}What command would you like to run: '))
            os.system(''+var10+'')
            os.system('python main.py')
        if System == 0:
            exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')

        
    main()

except KeyboardInterrupt:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT}If you are trying to end the script please type zero when you get the popup.')
    time.sleep(3)
    os.system('py main.py')
    
except Exception:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT }Sorry for this error. Please report it to https://github.com/tysudo/better_day-0.0.1/issues')
    time.sleep(3)
    os.system('start firefox https://github.com/tysudo/better_day-0.0.1/issues')