
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


def getPrompt(row):
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

    return promptString