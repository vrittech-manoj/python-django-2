import requests
from datetime import datetime
import threading

def download(image_url,i):
    data  = requests.get(image_url)
    # #save this image
    with open(f"{i}.png", "wb") as f:
        f.write(data.content)

image_data = [
              "https://cnex.com.np/images/Pioneering-Female-Img7.png",
              "https://cnex.com.np/images/Our-Story.png",
              "https://cnex.com.np/images/Our-Story.png",
              "https://cnex.com.np/images/Pioneering-Female-Img7.png",
              "https://cnex.com.np/images/disk-image-rotate.png",
            ]


t1 = datetime.now()
print("****************with threading********************")


i = 0

thread_lst = []
for image_url in image_data:
    i = i+1
    thread_1 = threading.Thread(target=download,args=[image_url,i])
    thread_1.start()
    thread_lst.append(thread_1)


for task in thread_lst:
    task.join()


t2 = datetime.now()

# Calculate execution time
execution_time = t2 - t1

total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds")

