# PLAN:
# have the buttons over the board but semi-transparent
# goes solid when hovered over it
# after opening the block screen, a page with all the blocks will appear
# once clicked on one, it will stay on your mouse until you release
# the block will be translucent in whatever color you are
# make it snap to grid
# and every time the position changes check if that move is possible
# if it's not possible, make the color grey or smth like that
# once released mouse, move on (no change mind - release move type)
# drag to the edges of the board to remove the piece
# ofc theres X button on the choose block place too so you can look at the board
# also when you are dragging, the buttons do not turn solid or work

import pygame
pygame.init()

w = 720
screen = pygame.display.set_mode((w,w))

clock = pygame.time.Clock()
pygame.display.set_caption("Blokus")

class Board():
    def __init__(self, padding, blockSize, colors):
        self.colors = colors
        self.size = blockSize
        self.padding = padding

        self.values = []
        for y in range(20):
            self.values.append([])
            for _ in range(20):
                self.values[y].append(0)
        
        self.rects = []
        for y in range(20):
            self.rects.append([])
            for x in range(20):
                self.rects[y].append(pygame.Rect(padding+x*blockSize, padding+y*blockSize, blockSize, blockSize))

    def drawBoard(self):
        self.drawBlocks()
        self.drawLines()
    
    def drawBlocks(self):
        for y in range(20):
            for x in range(20):
                pygame.draw.rect(screen, self.colors[self.values[y][x]], self.rects[y][x])
    
    def drawLines(self):
        for y in range(21):
            lineStart = (self.padding, y*self.size + self.padding)
            lineEnd = (w - self.padding, y*self.size + self.padding)
            pygame.draw.line(screen, (200,200,200), lineStart, lineEnd, 5)
        
        for x in range(21):
            lineStart = (x*self.size + self.padding, self.padding)
            lineEnd = (x*self.size + self.padding, w - self.padding)
            pygame.draw.line(screen, (200,200,200), lineStart, lineEnd, 5)

def setup():
    padding = w*0.03
    blockSize = (w-padding*2)/20
    colors = [(255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,255,0)]

    board = Board(padding, blockSize, colors)

    stage = "index"

    return board, stage

def main():
    board, stage = setup()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        screen.fill((200,200,200))

        board.drawBoard()

        pygame.display.flip()
        clock.tick(60)

main()
