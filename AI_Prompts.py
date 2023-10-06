import requests
import io
import base64
from PIL import Image, PngImagePlugin

import time
import os

import slack_workflow
import ipc_database
import promptGen
import gitRepo
import stableDiffusionApi
import analytics




seed = 6692921564

rows = ipc_database.getIpcData()

stableDiffusionApi.setModel("dreamshaper_8.safetensors [879db523c3]")

gitRepo.connect()

analytics.updateTxtFile("-----StableDiffusion Prompts-----\n")


#ipcs = [281, 811]
#for j in ipcs:
for row in rows:

    id = row[0]

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    promptString = promptGen.getPrompt(row)
 
    seed = seed - 100
    
    if(os.path.isfile("Output/"+str(id)+'.png')):
        print("Skipped " +str(id))
        continue

    analytics.updateTxtFile("\n=======================\nIPC "+str(id)+"\n"+str(promptString)+"\ntime : "+current_time)

    print("    IPC "+ str(id)+ " at "+current_time)
    # print(promptString)
    # print(seed)


    r = stableDiffusionApi.generate(promptString, seed)
    stableDiffusionApi.saveImage(r, id)

    #print("   -----------------")

    gitRepo.update(id)

    slack_workflow.sendMessageToSlack(id)

    #time.sleep(30)



   



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
