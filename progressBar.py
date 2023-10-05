def getProgress(ipc):
    perc = round(100*(ipc/12000),2)
    result = ""
    x = 1

    while x <= round(perc):
        result = result + "█"
        x = x+1

    while x <= 100:
        result = result + "▁"
        x = x+1

    print(result)

#sendMessageToSlack(1565) 
getProgress(1596)
