import Classes, YNAccount, game

window = Classes.Window(1500,700, "Music Game")
window.initScreen()

user, userIndex = YNAccount.startUp(window)

game.game(window, user, userIndex)