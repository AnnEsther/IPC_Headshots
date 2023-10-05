import requests    

URL = 'https://hooks.slack.com/triggers/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'


def sendMessageToSlack(ipc):
    myobj = {
        "message": "Generated " +ipc+ "\nhttps://github.com/AnnEsther/IPC_Headshots/blob/main/Output/"+str(ipc)+".png\nCompleted : "+str(100*(ipc/12000))+"%",
        "ipc": ipc
    }
    x = requests.post(URL, json = myobj)
    print(x.text)

    