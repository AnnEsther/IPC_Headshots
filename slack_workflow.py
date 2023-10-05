import requests    
import progressBar

URL = 'https://hooks.slack.com/triggers/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'


def sendMessageToSlack(ipc):
    p = str(round(100*(ipc/12000),2))
    pBar = progressBar.getProgressBar(ipc) +" : "+p+" % "
    myobj = {
        "message": "Generated " +str(ipc)+ "\nhttps://github.com/AnnEsther/IPC_Headshots/blob/main/Output/"+str(ipc)+".png\n"+ pBar ,
        "ipc": ipc
    }
    x = requests.post(URL, json = myobj)
    print(pBar)

#sendMessageToSlack(1565) 
