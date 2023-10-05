def getProgress(ipc):
    perc = round(100*(ipc/12000),2)
    result = ""
    x = 1

    for x in range(1,(perc)):
        result = result + "█"

    for x in range(round(perc),100):
        result = result + "▁"

    print(result)

#sendMessageToSlack(1565) 
getProgress(13)
