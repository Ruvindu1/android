import time
import urllib
import sys
import os

os.system('clear')

won_data="""     >>>>    WON data    <<<<          """
no_data="""      >>>>    NO  data    <<<<          """
line = """\033[1;36;40m\n___________________________________________________________\n"""

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

\033[1;35;40m             [Be Cool] mod by RJ studio 2020
"""

print(name, "")


try:
    f = open("file_auth.txt", "r")
    file_auth = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("file_auth.txt", "w")
    f.write(wr)
    f.close
    f = open("file_auth.txt", "r")
    file_auth = f.read()
    f.close
    
try:
    f = open("file_url.txt", "r")
    f = open("file_url.txt", "r")
    file_url1 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("file_url.txt", "w")
    f.write(wr)
    f.close
    f = open("file_url.txt", "r")
    file_url1 = f.read()
    f.close


try:
    import requests


except ImportError:
    print('waiting.......')
    os.system('pip3 install requests')
    print('%s Requests installed.')
    os.system('clear')
    import requests

    auth=file_auth
def main():
    os.system("clear")
    print(name,"\n")
  
    
head = {"Host": "megarun.dialog.lk",
              "Authorization": file_auth, "X-Unity-Version": "2018.3.0f2"}
url = file_url1
    
s = int(input("\033[1;36;40mEnter Amount - "))
    
rr=0  
for rr in range(rr,s):
  os.system("clear")
  print(name)
  size = 0
  rj = requests.get(url, headers=head)
  request = str(rj)
  if request == '<Response [204]>':
    print(no_data)
  elif request == '<Response [200]>':
    print(won_data)
  else:
    print(line)
    print("\n\033[1;31;40m [retry] Check Again your internet connection... [retry]")
    print(line)

  rr+=1
  print("\033[1;0;40m\n",str(rr), "Wait For Next request",end="")
  for j in range(180):
      
    rrr = j/180*100
    print("\033[1;36;40m\n>>> [+]",str(int(rrr)) +"% ",end="")
            
    time.sleep(0.5)
    sys.stdout.write("\033[F")
        
os.system('figlet FINISHED')
again()


def again():
    again = input('Restart Algorithm  (y/n) :- ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else: ('close the Algorithm ')

if __name__ == "__main__":
    main()
