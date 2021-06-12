import json
filename = "highscoreDB.json"
#--- load high scores:
with open(filename,"r") as f:
  data = json.load(f)

#-- function to add score:
def newScore(name,score): #returns true if new high score set.
    data["scores"].append({"name":name, "score":score})
    if score > data ["highscore"]["score"]: 
        data["highscore"]["score"] = score
        data["highscore"]["player"] = name
        return True
    else:
        return False

#-- function to retrieve entire leaderboard:
def retrieveScores():
    return data["scores"]

#-- function to retrive high score:
def retrieveHighScore():
    return data["highscore"]

#-- function to save all scores:
def save():
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)