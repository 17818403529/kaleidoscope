from time import time, sleep


class Particle:
    def __init__(self, pos, speed, acc):
        self.pos = pos
        self.speed = speed
        self.acc = acc

    def move(self, frame):
        for i in range(3):
            self.speed[i] += self.acc[i] * frame
            self.pos[i] += self.speed[i] * frame

    def act(self):
        self.move()


class GameEngine:
    def __init__(self):
        self.object = []
        self.fps = 60
        self.frame = 1 / 60

    def run(self):
        while True:
            # frame-by-frame simulation
            t0 = time()
            for i in self.object:
                i.act()
            t1 = time()
            sleep(self.frame - (t1 - t2))
