import pygame
import unittest
from pygame.locals import *

def helloWorld():
    print("hello world!")


def forLoopAndList():
    listofNumbers=[]
    for x in range(50):
        listofNumbers.append(x)

    for number in listofNumbers:
        number=number*96
        print(int(number))
    print(int(listofNumbers[-1]))
    listofNumbers.reverse()

def recursionDemo(listA, n):
    
    if len(listA) > n:
        temp=[]
        for number in listA:
            temp.append(number)
        return temp
    else:
        if len(listA)==0:
            listA.append(0)
            return recursionDemo(listA,n)
        elif len(listA)==1:
            listA.append(1)
            return recursionDemo(listA,n)
        else: 
            listA.append(listA[-1]+listA[-2])
            return recursionDemo(listA,n)


def pygameDemo():
    pygame.init()
    pygame.display.set_caption('This is a test of pygames window')
    screen=pygame.display.set_mode((1280,720))
    imagetodisplay=pygame.image.load("../course-project-a8-mcm/hello.png")
    while True:
        screen.fill(0)
        screen.blit(imagetodisplay,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)
        pygame.display.flip()

#helloWorld()
forLoopAndList()
#fiblist=[0,1]
#print(recursionDemo(fiblist,5))

class tests(unittest.TestCase):
    def test0(self):
        temp=recursionDemo([0,1], 5)
        self.assertEqual(temp, [0,1,1,2,3,5])
    def test1(self):
        self.assertEqual(recursionDemo([0,1], 6), [0,1,1,2,3,5,8])
    def test2(self):
        self.assertEqual(recursionDemo([0,1], 7), [0,1,1,2,3,5, 8,13])
    def testForloop(self):
        temp=[]
        for x in range(50):
            temp.append(x*96)
        self.assertEqual(forLoopAndList(),temp)
thetests=tests()
thetests.test0()
thetests.test1()
thetests.test2()
thetests.testForloop

pygameDemo()