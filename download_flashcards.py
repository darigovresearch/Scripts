# download_flashcards.py is code to clone all .apkg files from Flashcards

import requests, json, os
from urllib.parse import unquote

meta_url = "https://raw.githubusercontent.com/darigovresearch/Meta/main/meta.json"
content = requests.get(meta_url)
json = json.loads(content.content)

content = json["content"]
# print(content)
# print(len(content))

# making a relevant folder
os.chdir("..")
try:
    # try to make the folder
    os.mkdir("Darigov Research Flashcards")
except Exception as e:
    # notify user that folder already exists
    print("Folder already exists")

os.chdir("Darigov Research Flashcards")

# getting all relevant urls
all_download_urls = []
for i in range(0, len(content)):

    download_list = content[i]["downloads"]
    for j in range(0, len(download_list)):
        # print(download_list[j]["download URL"])

        all_download_urls.append(download_list[j]["download URL"])

# print(all_download_urls)
# print(len(all_download_urls))

# downloading all content of each file
for i in range(0, len(all_download_urls)):

    # making the request
    r = requests.get(all_download_urls[i])

    print("Downloading file " + str(i + 1) + " of " + str(len(all_download_urls)))
    print("\t" + all_download_urls[i] + "\n")

    # generating the filename from the urlsafe string
    temp_split = all_download_urls[i].split("/")
    filename = unquote(temp_split[-1])

    # creating & writing to the file
    open(filename, 'wb').write(r.content)
