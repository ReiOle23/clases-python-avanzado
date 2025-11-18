from threading import Thread
from time import sleep

running = True

def count_time():
    global running
    time = 0
    while running == True:
        print("Counting",time)
        sleep(1)
        time += 1
    
def stop():
    global running
    input("Pres enter key to stop...")
    running = False
    
h1 = Thread(target=count_time)
h1.start()

h2 = Thread(target=stop)
h2.start()

print("Counter finished.")