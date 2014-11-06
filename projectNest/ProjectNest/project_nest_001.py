#!/usr/bin/python

#This program makes the output voltage Linear and maps the linear voltage into cm
#It also has a list of bird objects that call various bird sound

import pygame
from pygame.locals import *
import random
from random import randrange, sample, uniform
import math, cmath
import time, signal, sys, Timer, Interpolate
from Adafruit_ADS1x15 import ADS1x15
from pygame.mixer import Sound


pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8)
boot_up = pygame.mixer.Sound("boot_up.wav")
boot_up.play()
      

#[-------------DistanceSensorStuff-------------------------------]        
def signal_handler(signal, frame):
        print ' You exited the program'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ADS1015 = 0x00  # 12-bit ADC

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

sps = 64  # 64 samples per second
gain = 4096

#[-------------Helper--------------------------------------] 

class Helper:
        def __init__(self):
                pass
        
        def logData(self):

                #Below: Makes the IRD sensor's voltage linear.
                #Then Maps the voltage range to a distance range.
                #Then prints to console

                # Read channel 0 in single-ended mode using the settings above
                volts = adc.readADCSingleEnded(1, gain, sps) / 1000
                linearVoltage = 1 / volts

                mappedValue = Interpolate.map(linearVoltage, 0.5, 0.9, 100, 550)

                distance = int("%.0f" % (mappedValue))

                #Limiting the data to a usable range
                #Upper limit:
                if distance > 550:
                        distance = 550
                #Lower limit:
                if distance  < 0:
                        distance = 0

                #print 'distance: ' , distance

                return distance

        
        #[-------------GUISetup----------------------------------------]

        def texts(self):
                colNum = 4
                xSpace = 200
                ySpace = 170
                margin = 10
                line1 = 10
                line2 = 50
                line3 = 80
                line4 = 110
                line5 = 140
                rowNum = 3
                width = colNum*xSpace + margin*2
                height = int(rowNum*ySpace)
                
                
                
                #initialize the screen
                screen = pygame.display.set_mode((width,height),0,32)
                #sets screen to black every frame, like a shutter.
                screen.fill(pygame.Color("black"))

                #Create a text that update live info
                myfont_big = pygame.font.SysFont("calibri", 90)
                myfont_medium = pygame.font.SysFont("calibri", 50)
                myfont_small = pygame.font.SysFont("calibri", 30)

                distance = "Distance: " + str(myHelper.logData()) #myHelper.logData()

                for i in range(0, birdNum):

                        states = "State: " + str(myBirds[i].state)
                        species = "Species: " + str(myBirds[i].species)
                        mood = "Mood: " + str(round(myBirds[i].mood, 4))
                        personality = "Personality: " + str(round(myBirds[i].personality, 4))

                        label_birdNum = myfont_medium.render("Bird " + str(i + 1), 1, (255,155,0))
                        label_dist = myfont_big.render(distance, 1, (255,155,0))
                        label_state = myfont_small.render(states, 1, (255,155,0))
                        label_species = myfont_small.render(species, 1, (255,155,0))
                        label_mood = myfont_small.render(mood, 1, (255,155,0))
                        label_personality = myfont_small.render(personality, 1, (255,155,0))
        

                        if i < colNum:
                                screen.blit(label_birdNum,(i*xSpace + margin,line1))
                                screen.blit(label_state,(i*xSpace + margin, line2))
                                screen.blit(label_species,(i*xSpace + margin, line3))
                                screen.blit(label_mood,(i*xSpace + margin, line4))
                                screen.blit(label_personality,(i*xSpace + margin, line5))
                        else:
                                screen.blit(label_birdNum,((i-colNum)*xSpace + margin,ySpace + line1))
                                screen.blit(label_state,((i-colNum)*xSpace + margin,ySpace + line2))
                                screen.blit(label_species,((i-colNum)*xSpace +margin,ySpace + line3))
                                screen.blit(label_mood,((i-colNum)*xSpace + margin,ySpace + line4))
                                screen.blit(label_personality,((i-colNum)*xSpace + margin,ySpace + line5))

                        screen.blit(label_dist,(xSpace + margin, 0.85*height))

        

        




#[-------------PlayingBirdSounds-------------------------------]  

class Birds:

        #pygame.mixer.init()
        #pygame.mixer.set_num_channels(8)

        
        
        def __init__(self, species, channel, personality):
                self.distance = myHelper.logData()
                self.stopwatch = Timer.Timer()
                #self.stopwatch.start()
                self.moodwatch = Timer.Timer()
                self.species = species
                self.channel = channel
                self.personality = personality
                self.mood = 0
                self.dropDist = Interpolate.map(self.mood, -10, 10, 249, 50)
                self.drop = Interpolate.map(self.personality, -10, 10, 2, 0.5)
                self.jumpDist = Interpolate.map(self.mood, -10, 10, 500, 250)
                self.jump = Interpolate.map(self.personality, -10, 10, 0.5, 2)
                self.lastState = 'chilled'
                self.state = self.lastState
                self.triggerInterupt = False
                
                self.voice = pygame.mixer.Channel(self.channel)
                #print self.voice.get_busy()


        def playSounds(self):
               
                if self.state == 'threat':
                        threat = pygame.mixer.Sound(self.species + '_threat.wav')
                        self.voice.play(threat)
                        #print 'threat'
                elif self.state == 'chilled':
                        chilled  = pygame.mixer.Sound(self.species + '_chilled_1.wav')
                        self.voice.play(chilled)
                        #print 'chilled'
                elif self.state == 'caution':
                        caution  = pygame.mixer.Sound(self.species + '_caution.wav')
                        self.voice.play(caution)
                        #print 'caution'
                elif self.state == 'musical':
                        musical  = pygame.mixer.Sound(self.species + '_musical.wav')
                        self.voice.play(musical)
                        #print 'musical'                       


                #print 'playing'
                        
        def startMoodWatch(self):
                if self.moodwatch.running == False and self.distance < self.dropDist:
                        self.moodwatch.start()
                if self.moodwatch.running == False and self.distance > self.jumpDist:
                        self.moodwatch.start()
                        
        def stopMoodWatch(self):
                if self.distance > self.dropDist and self.distance < self.jumpDist:
                        self.moodwatch.reset()

        def changeMood(self):
                dropTime = Interpolate.map(self.personality, -10, 10, 3, 10)
                jumpTime = Interpolate.map(self.personality, -10, 10, 10, 3)
                if self.distance < self.dropDist and self.moodwatch.getElapsedTime() > dropTime:
                        self.mood -= self.drop
                        self.moodwatch.reset()
                        if self.mood < -10:
                                self.mood = -10
                if self.distance > self.jumpDist and self.moodwatch.getElapsedTime() > jumpTime:
                        self.mood += self.jump
                        self.moodwatch.reset()
                        if self.mood > 10:
                                self.mood = 10
                


        def changeState(self):

                if self.mood > 5:
                        self.state = 'musical'
                elif self.mood > -2 and self.mood < 5:
                        self.state = 'chilled'
                elif self.mood < -2 and self.mood > -7:
                        self.state = 'caution'
                elif self.mood < -7:
                        self.state = 'threat'
                
                else:
                        self.state = 'sleep'



        def hasStateChanged(self):
                if self.state != self.lastState:
                        self.triggerInterupt = True
                        self.lastState = self.state


        def waiting(self):
                waitTime = Interpolate.map((abs(self.personality)), 0, 5, 20, 5)
                #print 'waiting'
                #print waitTime
                #print self.stopwatch.getElapsedTime()
                if self.voice.get_busy() is 0 and self.stopwatch.getElapsedTime() > waitTime:
                        #print 'play sound again'
                        self.playSounds()
                        self.stopwatch.reset()
                        return False
                else:
                        return True

        def waitingInterupt(self):
                fadeoutTime = 100
                if self.triggerInterupt == True:
                        self.voice.fadeout(fadeoutTime)
                        #print 'fadeout'
                        #print self.voice.get_busy() 
                        if self.voice.get_busy() is 0:
                                self.playSounds()
                                self.stopwatch.reset()
                                self.triggerInterupt = False

        def startTimer(self):
                if self.voice.get_busy() is 0 and self.stopwatch.running is False:
                        self.stopwatch.start()
                        #self.waiting()
                        #print 'start Time'


        def update(self):
                self.distance = myHelper.logData()
                self.startMoodWatch()
                self.stopMoodWatch()
                self.changeMood()
                self.changeState()
                self.hasStateChanged()
                self.startTimer()
                self.waiting()
                self.waitingInterupt()
                #print self.triggerInterupt

    
#[-------------SpecialSetup------------------------------------]

myHelper = Helper()

#A dictionary of the different bird species that can be added to the bird list
birdSpecies = ['tui', 'kokako', 'robin', 'stiazchbird']

birdList = []

#Number of birds added per nest
birdNum = 4

myBirds = []


def randomInsert():
        for i in range(0, birdNum):
                #puts a random number that's a float
                personality = random.uniform(-10,10) 
                key = ''.join(random.sample(birdSpecies, 1))
                birdList.append(key)
                myBirds.append (Birds(key, i, personality))
                #print personality
        return birdList

print randomInsert()

#for i in range(0,birdNum):
                #myBirds[i].playSounds()



#[-------------DrawLoop----------------------------------------]
        
while True:

        #Create a pygame window
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        #Creates a GUI window        
        myHelper.texts()

        pygame.display.update()
        
        #myHelper.logData()

        for i in range(0,birdNum):
                myBirds[i].update()
                
        
                



        






        
