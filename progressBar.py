def getProgress(ipc):
    perc = round(100*(ipc/12000),2)
    result = ""

    for x in range(1,round(perc)):
        result = result + "█"

    for x in range(round(perc),100):
        result = result + "▁"

    print(x)

#sendMessageToSlack(1565) 
getProgress(13)
