import pygame
import random

pygame.init()
win_width = 800
win_height = 800
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake")
pygame.display.update()

move_right = True
move_left = False
move_up = False
move_down = False
snake_width = 20
snake_height = 20
vel = snake_height
score = 0
run = True

class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xlst = [800]
        self.ylst = [800]
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.key_pressed = pygame.key.get_pressed()
        self.x1_change = 0
        self.y1_change = 0

    def head_movement(self):
        #pygame.draw.rect(win, (0, 255, 0), (self.x,self.y, 50,50))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not self.move_right:
                    self.move_left = True
                    self.move_right = False
                    self.move_up = False
                    self.move_down = False
            elif event.key == pygame.K_RIGHT and not self.move_left:
                self.move_left = False
                self.move_right = True
                self.move_up = False
                self.move_down = False
            elif event.key == pygame.K_UP and not self.move_down:
                self.move_left = False
                self.move_right = False
                self.move_up = True
                self.move_down = False
            elif event.key == pygame.K_DOWN and not self.move_up:
                self.move_left = False
                self.move_right = False
                self.move_up = False
                self.move_down = True
        if self.move_right:
            self.x += vel
        if self.move_left:
            self.x -= vel
        if self.move_up:
            self.y -= vel
        if self.move_down:
            self.y += vel
        pygame.draw.rect(win, (255, 255, 0), (self.x,self.y, snake_width,snake_height))
        pygame.display.update()

    def head_position(self):
        return (self.x,self.y)

    def add_tale(self):
        self.xlst.append(win_width)
        self.ylst.append(win_height)

    def refresh_tale(self,score):
        for i in range(score,0,-1):
            pygame.draw.rect(win, (0, 255, 0), (self.xlst[i], self.ylst[i], snake_width, snake_height))
            self.xlst[i] = self.xlst[i-1]
            self.ylst[i] = self.ylst[i-1]
            pygame.display.update()




class apple:
    def __init__(self):
        self.x = 0
        self.y = 0

    def random(self):
        self.x = random.choice(range(0,win_width+snake_width,snake_width))
        self.y = random.choice(range(0,win_height+snake_height,snake_height))
        pygame.display.update()

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, snake_width, snake_height))
        pygame.display.update()

    def postion(self):
        return (self.x,self.y)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (255,255,0))
    win.blit(value, [0, 0])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [win_width / 5, win_height / 2])

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()
apple1 = apple()
apple.random(apple1)
alive = True
head = snake(100,100)
lst_tale = snake(snake_width,snake_height)

while run:
    while alive==False and run:
        win.fill((200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        message("You Lost! Your Score="+str(score)+" Press R-Replay Q-Quit",(255,0,0))
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                alive = True
                win.fill((0,0,0))
                apple1 = apple()
                apple.random(apple1)
                alive = True
                head = snake(100, 100)
                lst_tale = snake(snake_width, snake_height)
                score = 0
            elif event.key == pygame.K_q:
                pygame.quit()
    while alive and run:
        if not 0<=head.x<=win_width or not 0<=head.y<=win_height:
            alive = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        head.head_movement()
        for i in range(len(lst_tale.xlst), 1, -1):
            if head.head_position() == (lst_tale.xlst[i - 1], lst_tale.ylst[i - 1]):
                alive = False
        if head.head_position() == apple1.postion():
            score += 1
            apple.random(apple1)
            lst_tale.add_tale()
        for n in range(len(lst_tale.xlst)):
            if apple1.postion()==(lst_tale.xlst[n],lst_tale.ylst[n]):
                apple1.random()
        lst_tale.xlst[0] = head.x
        lst_tale.ylst[0] = head.y
        lst_tale.refresh_tale(score)
        apple1.draw()
        win.fill((0, 0, 0))
        Your_score(score)
        clock.tick(20)
        pygame.display.update()
    alive = False

pygame.quit()

