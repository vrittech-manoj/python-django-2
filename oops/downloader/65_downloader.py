import requests
from datetime import datetime

def download(image_url):
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
for image_url in image_data:
    print("downloading ",image_url)
    i = i+1

    download(image_url)


t2 = datetime.now()

# Calculate execution time
execution_time = t2 - t1

total_seconds = execution_time.total_seconds()
print(f"Execution time: {total_seconds} seconds")

