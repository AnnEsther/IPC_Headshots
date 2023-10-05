def getProgressBar(ipc):
    perc = round(100*(ipc/12000),2)
    result = ""
    x = 1

    while x <= round(perc):
        result = result + "█"
        x = x+2

    while x <= 100:
        result = result + "▁"
        x = x+2

    return result

#getProgress(1596)
