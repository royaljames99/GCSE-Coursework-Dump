import time,json,random

valid_characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
";",":",",",".","'","!","£","$","%","^","&","?","@","~","-","_"," ","`","¬","0","1","2","3","4","5","6","7","8","9"]

userIndex = int

def newAccount():
    accountCreated = False
    while not accountCreated:
        valid = False
        while not valid:
            try:
                newUsnm = str(input("Enter username: "))
                valid = True
                for i in newUsnm:
                    if i not in valid_characters and valid:
                        valid = False
                        print("invalid characters")
            except:
                print("Not valid")
        valid = False
        while not valid:
            try:
                newPswd = str(input("Enter password: "))
                valid = True
                for i in newPswd:
                    if i not in valid_characters and valid:
                        valid = False
                        print("invalid characters")
            except:
                print("Not valid")

        
        #load file dictionary
        with open("Logins.json", "r") as file:
            data = json.load(file)
            
            #Check username hasn't already been chosen
            valid = True
            for i in data["Logins"]:
                if i["Usnm"] == newUsnm and valid:
                    print("Username already in use, please choose another")
                    valid = False

            if valid:    
                #assemble new account dict for file insertion
                newLogin = {"Usnm":newUsnm, "Pswd":newPswd, "highscore":0}

                #edit file dict
                data["Logins"].append(newLogin)

                #set global variables of username for later file editing
                global userIndex
                userIndex = data["Logins"].index({"Usnm":newUsnm, "Pswd":newPswd, "highscore":0})

                #insert edited dictionary into file
                with open("Logins.json", "w+") as file:
                    json.dump(data, file, indent = 5)
                    print("login created")
                    accountCreated = True

    #erase usnm and password variables for security
    newPswd = str


def login():
    loggedIn = False
    while not loggedIn:
        valid = False
        while not valid:
            try:
                Usnm =str(input("Enter username: "))
                valid = True
                for i in Usnm:
                    if i not in valid_characters and valid:
                        valid = False
                        print("invalid characters")
            except:
                print("Not a possible username")
        valid = False
        while not valid:
            try:
                Pswd = str(input("Enter password: "))
                valid = True
            except:
                print("Not a possible password")
        
        #load accounts file
        with open("Logins.json", "r") as file:
            data = json.load(file)

        #loop through logins in file
        for i in range(0,len(data["Logins"])):
            if data["Logins"][i]["Usnm"] == Usnm and data["Logins"][i]["Pswd"] == Pswd:
                loggedIn = True

                #set global variables of username for later file editing
                global userIndex
                userIndex = i

                #reset password for security reasons
                Pswd = ""

        #failed login handling
        if not loggedIn:
            print("Username or Password incorrect")


def startup():
    valid = False
    while not valid:
        try:
            cPlayerCheck = str(input("Do you have a login yet? (Y/N) ")).upper()
        except:
            print()
            print("whatever you typed was not what you were supposed to")
        else:
            valid = True
            options = ["Y","N"]
            if cPlayerCheck not in options:
                print("That wasn't one of the options")
                valid = False
            else:
                if cPlayerCheck == "Y":
                    login()                    
                else:
                    newAccount()


def endGame(score,userIndex):

    print()
    print("GAME OVER")

    with open("Logins.json", "r") as file:     
        data = json.load(file)
        if data["Logins"][userIndex]["highscore"] <= score :
            data["Logins"][userIndex]["highscore"] = score
        
        if score > data["Highscore"][0]["Score"]:
            data["Highscore"].insert(0,{"User": data["Logins"][userIndex]["Usnm"], "Score":score})
            data["Highscore"].pop(5)
        elif score > data["Highscore"][1]["Score"]:
            data["Highscore"].insert(1,{"User": data["Logins"][userIndex]["Usnm"], "Score":score})
            data["Highscore"].pop(5)
        elif score > data["Highscore"][2]["Score"]:
            data["Highscore"].insert(2,{"User": data["Logins"][userIndex]["Usnm"], "Score":score})
            data["Highscore"].pop(5)
        elif score > data["Highscore"][3]["Score"]:
            data["Highscore"].insert(3,{"User": data["Logins"][userIndex]["Usnm"], "Score":score})
            data["Highscore"].pop(5)
        elif score > data["Highscore"][4]["Score"]:
            data["Highscore"].insert(4,{"User": data["Logins"][userIndex]["Usnm"], "Score":score})
            data["Highscore"].pop(5)
        else:
            pass
        
        print()
        print("HIGHSCORES:")
        place = 0
        for i in data["Highscore"]:
            place += 1
            print(place,": ", data["Highscore"][place-1]["User"]," with ", data["Highscore"][place-1]["Score"]," points!")

        print()
        print("Your highscore is", data["Logins"][userIndex]["highscore"])

    with open("Logins.json", "w") as file:
        json.dump(data, file, indent = 5)

    quit()



startup()

indexsUsed = []

with open("Songs.json", "r") as file:
        songs = json.load(file)

score = 0

while True:

    #select song
    if len(songs["Songs"]) == len(indexsUsed):
        print("You appear to have solved every song in our list, congrats.")
        endGame(score,userIndex)

    songNotUsed = False #Variable that keeps track of if we have found an unused song
    while not songNotUsed:
        index = random.randint(0,len(songs["Songs"])-1)
        if index not in indexsUsed:
            indexsUsed.append(index)
            songNotUsed = True

    song = songs["Songs"][index]["name"]
    artist = songs["Songs"][index]["artist"]

    #edit song name to display to player
    songWords = song.split(" ")
    displaySong = ""
    for i in songWords:
        displaySong += songWords[songWords.index(i)][0]
        for j in range(0,len(i)-1):
            displaySong += " _"
        displaySong += "   "

    print("song is ",displaySong)
    print("artist is ",artist)
    
    #Guessing cycle
    guesses = 0
    correct = False
    while guesses < 2:
        valid = False
        while not valid:    
            try:
                guess = str(input("Enter guess: "))
            except:
                print("Not a valid guess")
            else:
                valid = True
                for i in guess:
                    if i not in valid_characters and valid:
                        valid = False
                        print("invalid characters")
                guesses += 1

        if guess.upper() == song.upper():
            if guesses == 1:
                print("CORRECT, +3 POINTS")
                score += 3
            else:
                print("CORRECT, +1 POINTS")
                score += 1
            print(" YOU HAVE ", score, "POINTS")
            correct = True
            guesses = 2 #janky way of breaking guess loop

        else:
            print("INCORRECT")

    if correct:
        print()
        print()
        #breakpoints to seperate questions
    else:
        endGame(score,userIndex)