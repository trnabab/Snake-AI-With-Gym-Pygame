import pygame, random, sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(11,10), Vector2(10,10), Vector2(9,10)]
        self.direction = Vector2(1,0)
        self.fruit_eaten = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left , (cell_size, cell_size))
		
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (cell_size, cell_size))

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (cell_size, cell_size))
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (cell_size, cell_size))
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (cell_size, cell_size))
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (cell_size, cell_size))

    def drawSnake(self):
        for i, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x*cell_size, block.y*cell_size, cell_size, cell_size)
            # pygame.draw.rect(screen, (81, 112, 232), snake_rect)
            if i == 0:
                self.update_head()
                screen.blit(self.head, block_rect)
            elif i == len(self.body) - 1:
                self.update_tail()
                screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[i+1] - block
                next_block = self.body[i-1] - block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                elif prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                    screen.blit(self.body_tl, block_rect)
                elif prev_block.y == -1 and next_block.x == 1 or prev_block.x == 1 and next_block.y == -1:
                    screen.blit(self.body_tr, block_rect)
                elif prev_block.y == 1 and next_block.x == -1 or prev_block.x == -1 and next_block.y == 1:
                    screen.blit(self.body_bl, block_rect)
                elif prev_block.y == 1 and next_block.x == 1 or prev_block.x == 1 and next_block.y == 1:
                    screen.blit(self.body_br, block_rect)

    def moveSnake(self):
        if self.fruit_eaten:
            body_copy = self.body[:]
            self.fruit_eaten = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy   
    
    def gameOver(self):
        if not 0 <= self.body[0].x < cell_number or  not 0 <= self.body[0].y < cell_number:
            return True

        for i in self.body[1:]:
            if i == self.body[0]:
                return True
        
        return False
    
    def add_block(self):
        self.fruit_eaten = True
    
    def update_head(self):
        self.head_dir = self.body[1] - self.body[0]

        if self.head_dir == Vector2(0,1): self.head = self.head_up
        elif self.head_dir == Vector2(0,-1): self.head = self.head_down
        elif self.head_dir == Vector2(1,0): self.head = self.head_left
        elif self.head_dir == Vector2(-1,0): self.head = self.head_right
    
    def update_tail(self):
        self.tail_dir = self.body[-2] - self.body[-1]

        if self.tail_dir == Vector2(0,1): self.tail = self.tail_up
        elif self.tail_dir == Vector2(0,-1): self.tail = self.tail_down
        elif self.tail_dir == Vector2(1,0): self.tail = self.tail_left
        elif self.tail_dir == Vector2(-1,0): self.tail = self.tail_right

class FRUIT:
    def __init__(self):
        self.setPosition()
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (cell_size, cell_size))

    def drawFruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        # pygame.draw.rect(screen, (228, 85, 79), fruit_rect)
        screen.blit(self.apple, fruit_rect)
    
    def setPosition(self):
        self.x = random.randint(0, (cell_number-1))
        self.y = random.randint(0, (cell_number-1))
        self.pos = Vector2(self.x, self.y)

class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0
    
    def update(self):
        self.snake.moveSnake()
        self.collision()

    def drawElements(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()
    
    def collision(self):
        if self.snake.gameOver():
            pygame.quit()
            sys.exit()

        if self.snake.body[0]== self.fruit.pos:
            self.fruit.setPosition()
            self.snake.add_block()
            self.score+=1
            print(self.score)


cell_size = 20
cell_number = 20

pygame.init()
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()


game = GAME()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT :
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)

    screen.fill((175,215,70))
    game.drawElements()
    pygame.display.update()
    clock.tick(60)
