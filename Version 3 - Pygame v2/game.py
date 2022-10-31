import Classes, json, time, pygame, random, sys

def updateLeaderboard(user, userIndex, score):
    with open("Users.json", "r") as file:
        data = json.load(file)
    
    if data["Logins"][userIndex]["Highscore"] <= score:
        data["Logins"][userIndex]["Highscore"] = score
    
    #Order top 5 scores
    leaderboardScores = [{"score" : 0, "name" : ""},{"score" : 0, "name" : ""},{"score" : 0, "name" : ""},{"score" : 0, "name" : ""},{"score" : 0, "name" : ""}]
    usersUsed = []
    for i in range(0,5):
        for j in data["Logins"]:
            if j["Highscore"] > leaderboardScores[i]["score"] and j["Username"] not in usersUsed:
                leaderboardScores[i]["score"], leaderboardScores[i]["name"] = j["Highscore"], j["Username"]
        usersUsed.append(leaderboardScores[i]["name"])
    for i in range(0,5):
        data["Highscore"][i]["User"], data["Highscore"][i]["Score"] = leaderboardScores[i]["name"], leaderboardScores[i]["score"]


    with open("Users.json", "w") as file:
        json.dump(data, file, indent = 5)


def displayScoreGUI(window, score, user):
    
    window.windowSurface.fill((0,0,0))


    with open("Users.json", "r") as file:
        leaderboard = json.load(file)

    leaderboardTitle = Classes.Text("arial", 25, "HIGHSCORES", colour = (255,255,255))
    leaderboard1 = Classes.Text("arial", 25, leaderboard["Highscore"][0]["User"] + " with a score of " + str(leaderboard["Highscore"][0]["Score"]), colour = (255,255,255))
    leaderboard2 = Classes.Text("arial", 25, leaderboard["Highscore"][1]["User"] + " with a score of " + str(leaderboard["Highscore"][1]["Score"]), colour = (255,255,255))
    leaderboard3 = Classes.Text("arial", 25, leaderboard["Highscore"][2]["User"] + " with a score of " + str(leaderboard["Highscore"][2]["Score"]), colour = (255,255,255))
    leaderboard4 = Classes.Text("arial", 25, leaderboard["Highscore"][3]["User"] + " with a score of " + str(leaderboard["Highscore"][3]["Score"]), colour = (255,255,255))
    leaderboard5 = Classes.Text("arial", 25, leaderboard["Highscore"][4]["User"] + " with a score of " + str(leaderboard["Highscore"][4]["Score"]), colour = (255,255,255))

    leaderboardTitle.showText(window, 20, 10)
    leaderboard1.showText(window, 20, 55)
    leaderboard2.showText(window, 20, 85)
    leaderboard3.showText(window, 20, 115)
    leaderboard4.showText(window, 20, 145)
    leaderboard5.showText(window, 20, 175)


    displayScore = Classes.Text("arial", 25, "Score = " + str(score), colour = (255,255,255))
    displayScore.showText(window, 1350, 25)


    pygame.display.update()


def endGame():
    pygame.QUIT()
    sys.exit()


def genSong(window, indexsUsed):

    with open("Songs.json", "r") as file:
        songs = json.load(file)
    
    if len(songs["Songs"]) == len(indexsUsed):
        userMessage = Classes.Text("arial", 25, "You appear to have used all our songs", colour = (255,255,255))
        userMessage.showText(window, 100, 600)
        pygame.display.update()
        time.sleep(2)
        endGame()

    songNotUsed = False
    while not songNotUsed:
        index = random.randint(0, len(songs["Songs"]) - 1)
        if index not in indexsUsed:
            indexsUsed.append(index)
            songNotUsed = True

    song = songs["Songs"][index]["name"]
    artist = songs["Songs"][index]["artist"]

    songWords = song.split(" ")
    displaySong = "Song is: "
    for i in songWords:
        displaySong += songWords[songWords.index(i)][0]
        for j in range(0,len(i) - 1):
            displaySong += " _"
        displaySong += "    "
    
    return song, artist, displaySong, indexsUsed


def clue():
    import os
    os.system("0001-5302.mp4")

def guess(window, song, artist, displaySong, score, user, userIndex):

    correct = False

    songDisplay = Classes.Text("arial", 25, displaySong, colour = (255,255,255))
    songDisplay.showText(window, 550, 200)
    artistDisplay = Classes.Text("arial", 25, artist, colour = (255,255,255))
    artistDisplay.showText(window, 550, 250)

    guesses = 0
    while guesses < 2:  
        valid = False
        while not valid:
            guessBox = Classes.textBox(400, 50, window.ww/2 - 200, window.wh/2 - 25, "Enter Guess")
            clueButton = Classes.Button(200, 50, window.ww * 0.75, window.wh * 0.25, "-1 point = Clue")

            while not guessBox.complete:
                window.eventGet()
                guessBox.checkActive(window)
                guessBox.keypressed(window)
                guessBox.showTextBox(window)
                clueButton.checkClicked(window)
                clueButton.showButton(window)

                if clueButton.clicked:
                    score -= 1
                    clueButton.unclickButton()
                    displayScoreGUI(window, score, user)
                    songDisplay = Classes.Text("arial", 25, displaySong, colour = (255,255,255))
                    songDisplay.showText(window, 550, 200)
                    artistDisplay = Classes.Text("arial", 25, artist, colour = (255,255,255))
                    artistDisplay.showText(window, 550, 250)
                    guessBox.showTextBox(window)
                    clueButton.showButton(window)
                    pygame.display.update()
                    clue()                    

                pygame.display.update()
                time.sleep(0.03)

            try:
                guess = str(guessBox.text)
                valid = True
                for i in guess:
                    if i not in Classes.valid_characters and valid:
                        valid = False
                        userMessage = Classes.Text("arial", 25, "Invalid guess", colour = (255,255,255))
            except:
                userMessage = Classes.Text("arial", 25, "Invalid guess", colour = (255,255,255))
            
            if not valid:
                userMessage.showText(window, 550, 600)
                pygame.display.update()
                time.sleep(2)
        
        valid = False
        guesses += 1
        if guess.upper() == song.upper():
            correct = True

            if guesses == 1:
                userMessage = Classes.Text("arial", 25, "CORRECT, +3 Points", colour = (255,255,255))
                userMessage.showText(window, 550, 600)
                pygame.display.update()
                time.sleep(2)
                score += 3
                updateLeaderboard(user, userIndex, score)
            else:
                userMessage = Classes.Text("arial", 25, "CORRECT, +1 Point", colour = (255,255,255))
                userMessage.showText(window, 550, 600)
                pygame.display.update()
                time.sleep(2)
                score += 1
                updateLeaderboard(user, userIndex, score)
            
            guesses = 2
        else:
            userMessage = Classes.Text("arial", 25, "INCORRECT", colour = (255,255,255))
            userMessage.showText(window, 550, 600)
            pygame.display.update()
            time.sleep(2)

    return correct, score 
        
        
        


def game(window, user, userIndex):
    
    score = 0
    indexsUsed = []

    while True:

        window.eventGet()

        displayScoreGUI(window, score, user)

        song, artist, displaySong, indexsUsed = genSong(window, indexsUsed)

        correct, score = guess(window, song, artist, displaySong, score, user, userIndex)

        if not correct:
            endGame()