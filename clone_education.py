import requests, json, os

meta_url = "https://raw.githubusercontent.com/darigovresearch/Meta/main/meta.json"
content = requests.get(meta_url)
json = json.loads(content.content)

content = json["content"]
# print(content)
# print(len(content))

# making a relevant folder
os.chdir("..")
os.mkdir("Darigov Research")
os.chdir("Darigov Research")
os.mkdir("Education")
os.chdir("Education")

# for i in range(0, len(content)):
for i in range(0, 5):
    print("Cloning repository " + str(i + 1) + " of " + str(len(content)))
    relevant_command = "git clone " + content[i]["Repository URL"] + ".git"
    # print(relevant_command)
    os.system(relevant_command)
