import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import psycopg2
import time
import os
import git


def getString(stat, value):
  percent = 100 * value/18
  if percent < 16.6:
      tempStr = "trivial"
  elif percent < 33.3:
      tempStr = "low"
  elif percent < 50:
      tempStr = "medium"
  elif percent < 66.6:
    tempStr = "concerning"
  elif percent < 83.3:
    tempStr = "high"
  else:
      tempStr = "critical"
  return tempStr + " " + stat

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "joyfulAnn",
                        port = 5432)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('SELECT * FROM ipcdata;')

rows = cur.fetchall()

conn.commit()
conn.close()

url = "http://127.0.0.1:7860"

option_payload = {
    "sd_model_checkpoint": "dreamshaper_8.safetensors [879db523c3]"
}

response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)

seed = 6692921564

repo = git.Repo()  # ex. "/User/some_user/some_dir"
origin = repo.remote("origin")  
assert origin.exists()
origin.fetch()

new_branch = repo.create_head("main", origin.refs.main)  # replace prod with master/ main/ whatever you named your main branch
new_branch.checkout()


f = open("Prompts.txt", "a")
f.write("StableDiffusion Prompts\n")
f.close()


#ipcs = [281, 811]
#for j in ipcs:
for row in rows:

    f = open("Prompts.txt", "a")

    #row = rows[j-1]
    id = row[0]



    name = row[1]
    birthDate = " born on " + str(row[2])
    race = row[4]
    subrace = row[5]
    gender = row[6]
    height = "height " + row[7]
    skincolor = row[8] + " skin"
    haircolor = row[9] + " hair"
    eyecolor = row[10] + " eyes"
    handedness = row[11] + " handed"
        
    strength = getString("strength", row[12])
    force = getString("force", row[13])
    sustain = getString("sustain", row[14])
    tolerance = getString("tolerance", row[15])
    dexterity = getString("dexterity", row[16])
    speed = getString("speed", row[17])
    precision = getString("precision", row[18])
    reaction = getString("reaction", row[19])
    intelligence = getString("intelligence", row[20])
    memory = getString("memory", row[21])
    processing = getString("processing", row[22])
    reasoning = getString("reasoning", row[23])
    constitution = getString("constitution", row[24])
    healing = getString("healing", row[25])
    fortitude = getString("fortitude", row[26])
    vitality = getString("vitality", row[27])
    luck = getString("luck", row[28])

    type = "cinematic picture , clothed "

    promptString = type + " , " + skincolor + " , " + haircolor + " , " + race + birthDate + ", subrace " + subrace + " , " + gender + " , " + height + " , " +  eyecolor + " , " + handedness + " , " + strength + " , " + force + " , " + sustain + " , " + tolerance + " , " + dexterity + " , " + speed + " , " + precision+ " , " + reaction + " , " + intelligence + " , " + memory + " , " + processing + " , " + reasoning + " , " + constitution + " , " + healing + " , " + fortitude + " , " + vitality + " , " + luck

    #seed = str(row[12]) + str(row[13]) + str(row[14]) + str(row[15]) + str(row[16]) + str(row[17]) + str(row[18]) + str(row[19]) + str(row[20]) + str(row[21]) + str(row[22]) + str(row[23]) + str(row[24]) + str(row[25]) + str(row[26]) + str(row[27]) + str(row[28])
    #seed = str(row[12]) +  str(row[16]) +  str(row[20])  + str(row[24]) +  str(row[28])
 
    f.write("\n=======================")
    f.write("\nIPC "+ str(id))
    f.write("\n"+ str(promptString))
    f.write("\nseed : "+ str(seed))
    
    if(os.path.isfile("Output/"+str(id)+'.png')):
        print("Skipped " +str(id))
        continue

    seed = seed - 100

    payload = {
    "prompt": promptString,
    "steps": 20,
    "width": 512,
    "height": 512,
    "seed": seed
    }

    print("    IPC ", id)
    print(promptString)
    print(seed)

   

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save("Output/"+str(id)+'.png', pnginfo=pnginfo)

    print("   -----------------")

    f.close()

    repo.git.add('--all')
    repo.index.commit("Generated IPC " +str(id)+"\n LINK : https://github.com/AnnEsther/IPC_Headshots/blob/main/Output/"+str(id)+".png")

    repo.git.push("--set-upstream", origin, repo.head.ref)

    time.sleep(30)



   



# 00:  1
# 01: 'Eve'
# 02: 2018
# 03: 0
# 04: 'Human'
# 05: 'Nordic Human'
# 06: 'Male'
# 07: '6\'3"'
# 08: 'Pale'
# 09: 'Platinum'
# 10: 'Green'
# 11: 'Right'
# 12: 16
# 13: 6
# 14: 5
# 15: 5
# 16: 14
# 17: 6
# 18: 6
# 19: 2
# 20: 7
# 21: 2
# 22: 2
# 23: 3
# 24: 8
# 25: 4
# 26: 3
# 27: 1
