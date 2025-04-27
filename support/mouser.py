from pynput.mouse import Button, Controller

mouse = Controller()

def clicker(g):
    mouse.position = (g.get("x"), g.get("y"))
    mouse.click(Button.left)

def mover(g):
    mouse.position = (g.get("x"), g.get("y"))