import requests, json, os

meta_url = "https://raw.githubusercontent.com/darigovresearch/Meta/main/meta.json"
content = requests.get(meta_url)
json = json.loads(content.content)

content = json["content"]
# print(content)
# print(len(content))

# going to relevant folder
os.chdir("..")
os.chdir("Darigov Research")
os.chdir("Education")

for i in range(0, len(content)):
    print("Updating repository " + str(i + 1) + " of " + str(len(content)))
    folder_name = content[i]["Repository URL"][35:]
    os.chdir(folder_name)
    relevant_command = "git pull"
    # print(relevant_command)
    os.system(relevant_command)
    os.chdir(folder_name)
