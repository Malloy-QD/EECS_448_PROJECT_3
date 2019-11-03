import pygame
class buttom():
    def __init__(self,x,y,width,hight,color,text=None):
        self.x=x
        self.y=y
        self.width=width
        self.hight=hight
        self.color=color
        self.text=text
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color, (self.x,self.y,self.width,self.hight),0)
        #text font, text size
        font = pygame.font.SysFont('times', 40)
        text = font.render(self.text, 1, (0,0,0))
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.hight/2 - text.get_height()/2)))
    
    def ontop(self,position):
        if position[0]<self.x+self.width and position[0]>self.x:
            if position[1]>self.y and position[1]<self.y+self.hight:
                return True
        return False