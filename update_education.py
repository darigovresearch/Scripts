# update_education.py is code to update all locally cloned education repos

import requests
import json as js
import os

meta_url = "https://raw.githubusercontent.com/darigovresearch/Meta/main/meta.json"


def main():

    content = requests.get(meta_url)
    json = js.loads(content.content)

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

        # enter folder
        os.chdir(folder_name)

        # run command
        relevant_command = "git pull"
        # print(relevant_command)
        os.system(relevant_command)

        # return to parent directory
        os.chdir("..")


if __name__ == '__main__':
    main()
