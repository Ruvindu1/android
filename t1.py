import time
import urllib
import sys
import os

os.system('clear')

won_data="""     >>>>    WON data    <<<<          """
no_data="""      >>>>    NO  data    <<<<          """
bar = "\033[1;36;40m\n___________________________________________________________\n"

name="""\033[1;36;40m

             **                  **                 M
               **               **                  E 
                ** *********** **                   G
                 ***************                    A
                ******************
              **** @ ****** @ *****
             ***********************                R
            *************************               U
           ***************************              N          
                                        
        ****    ******************     ****         2  
       ******  ********************   ******          
       ******  *********************  ******        0     
       ******  *********************  ******         
       ******  *********************  ******        2     
       ******  *********************  ******          
       ******  *********************  ******        0  
       ******  *********************  ******            
       ******  *********************  ******              
       ******  *********************  ******              
       ******  *********************  ******              
       ******    *****************    ******           
        ****       *************       ****           
                                                    
                ******       *****                 R     
               ********     ********               J      
               ********     ********                     
               ********     ********               S     
               ********     ********               T    
               ********     ********               U      
               ********     ********               D      
               ********     ********               I      
                ******       ******                O      
__________________________________________________________
\033[1;35;40m      __  __               _      ____        _   _       
\033[1;33;40m     |  \/  | ___  __ _   / \    |  _ \ _   _| \ | | Hack
\033[1;32;40m     | |\/| |/ _ \/ _` | / O \   | |_) | | | |  \| |    
\033[1;30;40m     | |  | |  __/ (_| |/ ___ \  |  _ <| |_| | |\  |    
\033[1;32;40m     |_|  |_|\___|\__, /_/   \_\ |_| \_\\___|||_| \_|    
\033[1;34;40m                  |___/                                 
\033[1;35;40m              [Be Cool] mod by RJ studio 2020
\033[1;32;40m___________________________________________________________
"""

print(name, "")




try:
    f = open("file1.txt", "r")
    file1 = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("file1.txt", "w")
    f.write(wr)
    f.close
    f = open("file1.txt", "r")
    file1 = f.read()
    f.close

try:
    f = open("file2.txt", "r")
    f = open("file2.txt", "r")
    file2 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("file2.txt", "w")
    f.write(wr)
    f.close
    f = open("file2.txt", "r")
    file2 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name,"\n")
    a = int(input("\033[1;36;40mEnter Amount - "))
    headers = {"Host": "megarun.dialog.lk",
              "Authorization": file1, "X-Unity-Version": "2018.3.0f2"}
    url = file2
    
    t = 0
    while a > t:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers)
        resp = str(res)
        if resp == '<Response [204]>':
            print(no_data)
        elif resp == '<Response [200]>':
            print(won_data)
        else:
            print("\n\033[1;31;40m [retry] Checking your internet connection... [retry]")
        

        t+=1
        print("\033[1;0;40m\n",str(t), "Please Wait For Next request",end="")
        for i in range(180):
            
            ls = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(ls)) +"% ",end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
