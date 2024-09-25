import pyxel

class GfxManager:

    texturesId = {}

    def __init__(self):
        self.imageId = 0
        #paths
        self.loadImage("assets/tube.png")
        self.loadImage("assets/city.png")
        self.loadImage("assets/tilemap.png")

    def loadImage(self,path):
        pyxel.image(self.imageId).load(0, 0, path) 
        GfxManager.texturesId[path.replace("assets/","").replace(".png","")] = self.imageId;       
        self.imageId+=1

    def draw_text(x,y, text,colour):
        pyxel.text(x+1, y+1, text, 0)
        pyxel.text(x, y, text, colour)
