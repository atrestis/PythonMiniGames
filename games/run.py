import msvcrt
import time

def startrunning():
        high_score = 55
        name = "Try to beat me"
        while True:
                distance = int(0)
                print("\n--------------------------------------------------------------")
                print('\n\n Welcome to 100m sprint in python Press x & z rapidly to run!')
                print('* = 10m')
                print("\n**Current record: " + str(high_score) + "s, by: " + name)
                print('\nPress enter to start')
                input()
                print('Ready...')
                time.sleep(1)
                print('GO!')
                
                start_time = time.time()
                while distance < 100:
                        
                        k1 = msvcrt.getch().decode('ASCII')
                        if k1 == 'z':
                                k2 = msvcrt.getch().decode('ASCII')
                                if k2 == 'x':
                                        distance += 1
                                        if distance == 50:
                                                print("* Almost done! Don't give up!")
                                        elif distance % 10 == 0:
                                                print('*')
                                                
                fin_time = time.time() - start_time
                fin_time = round(fin_time,2)
        
                
                print('Well done you did it in...')
                print(fin_time)
                
                
                if fin_time < high_score:
                        print("Wow! We got a record breaker here! ")
                        name = input("Please enter your name : ")
                        high_score = fin_time
                
                
                                

if __name__ == "__main__":
   startrunning()