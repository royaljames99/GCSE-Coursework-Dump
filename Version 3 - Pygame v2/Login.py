import Classes, time, hashlib, pygame, json


def login(window):
    loggedIn = False
    while not loggedIn:

        valid = False
        while not valid:

            usnmBox = Classes.textBox(400, 50, window.ww/2 - 200, window.wh/2 - 25, "Enter Username")
            Classes.getTxbxInput(usnmBox, window)
            #validate input
            try:
                usnm = usnmBox.text
                valid = True
                for i in usnm:
                    if i not in Classes.valid_characters:
                        valid = False
                        charMessage = "You can only use the following characters: "
                        for i in Classes.valid_characters:
                            charMessage += i
                        invalidText = Classes.Text("arial", 25,charMessage, colour = (255,255,255))
            except:
                invalidText = Classes.Text("arial",25,"IMPOSSIBLE UERNAME", colour = (255,255,255))
            
            #show invalid message if necissary
            if not valid:
                invalidText.showText(window, 100, 600)
                pygame.display.update()
                time.sleep(2)
            
        #password
        valid = False
        while not valid:

            pswdBox = Classes.textBox(400, 50, window.ww/2 - 200, window.wh/2 - 25, "Enter Password")
            Classes.getTxbxInput(pswdBox, window)
            #validate input
            try:
                pswd = pswdBox.text
                valid = True
                for i in usnm:
                    if i not in Classes.valid_characters and valid:
                        valid = False
                        charMessage = "You can only use the following characters: "
                        for i in Classes.valid_characters:
                            charMessage += i
                        invalidText = Classes.Text("arial", 25, "INVALID USERNAME", colour = (255,255,255))
            except:
                invalidText = Classes.Text("arial", 25, "IMPOSSIBLE USERNAME", colour = (255,255,255))
            
            #show invalid message if necissary
            if not valid:
                invalidText.showText(window, 100, 600)
                pygame.display.update()
                time.sleep(2)
            
            #Encrypt password
            pswdEnc = hashlib.sha512()
            pswd = bytes(pswd, "ascii")
            pswdEnc.update(pswd)
            pswdEnc = str(pswdEnc.digest())
            
            #CHECK USERNAME AND PASSWORD
            with open("Users.json", "r") as file:
                data = json.load(file)
            

            for i in range(0, len(data["Logins"])):
                if data["Logins"][i]["Username"] == usnm and data["Logins"][i]["Pswd"] == pswdEnc:
                    
                    loggedIn = True

                    user = usnm
                    userIndex = i
                    pswd = ""

                    return user, userIndex

            if not loggedIn:
                errorText = Classes.Text("arial", 25, "Username or Password incorrect", colour = (255,255,255))
                errorText.showText(window, 100, 600)
                pygame.display.update()
                time.sleep(2)
                window.windowSurface.fill((0,0,0))
            
