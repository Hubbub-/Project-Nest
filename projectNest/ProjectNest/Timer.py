import time

class Timer:
    def __init__(self):
        self.startTime = 0
        self.stopTime = 0
        self.elapsed = 0
        self.running = False

    def start(self):
        self.startTime = time.time()
        self.running = True

    def stop(self):
        self.stopTime = time.time()
        self.running = False

    def reset(self):
        self.startTime = 0
        self.stopTime = 0
        self.elapsed = 0
        self.running = False

    def getElapsedTime(self):
        if self.running == True:
            self.elapsed = time.time() - self.startTime
        else:
            self.elapsed = self.stopTime - self.startTime
        return self.elapsed

#[----------------------Testing-----------------------------]
#stopwatch = Timer()

#stopwatch.start()
#while True:
    #print stopwatch.getElapsedTime()
