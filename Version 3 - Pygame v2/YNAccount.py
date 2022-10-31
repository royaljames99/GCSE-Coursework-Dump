import Classes, time, pygame

def startUp(window):
    yButton = Classes.Button(100, 100, window.ww/2 - 200, window.wh/2 - 50, "YES")
    nButton = Classes.Button(100, 100, window.ww/2 + 100, window.wh/2 - 50, "NO")

    yButton.startColour, yButton.endcolour = (255,0,0),(255,50,50)
    nButton.startColour, nButton.endColour = (0,0,255),(50,50,255)

    qText = Classes.Text("arial", 25, "DO YOU HAVE AN ACCOUNT YET", colour = (255,255,255))
    

    while not (yButton.clicked or nButton.clicked):   
        window.eventGet()
        window.windowSurface.fill((0,0,0))
        qText.showText(window, window.ww/2 - 170, 200)
        yButton.showButton(window)
        nButton.showButton(window)
        yButton.checkClicked(window)
        nButton.checkClicked(window)
        pygame.display.update()
    window.windowSurface.fill((0,0,0))
    if yButton.clicked:
        import Login
        user, userIndex = Login.login(window)
    else:
        import signup
        user, userIndex = signup.newAccount(window)
    
    return user, userIndex