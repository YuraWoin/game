from pygame import *
init()

fon = image.load(r'images/fonforgame.jpg')
icon = image.load(r'c:\YuraWoin\game\images\gameone.jpg')
fon1 = image.load(r'c:\YuraWoin\game\images\home.png')
zombie1 = image.load(r'images/chasing.png')
myfount = font.Font(r'c:\YuraWoin\game\founts\Comic_Relief,Tagesschrift\Comic_Relief\ComicRelief-Bold.ttf', 50)
piv_pav = image.load('c:/YuraWoin/game/images/pulya.jpg')
fon_sounds = mixer.Sound(r'звуки/horror-rumble-winds-253834.mp3')




def walk():
    walk_left = [
        image.load('sprites/left/1.png'),
        image.load(r'sprites\left\2.png'),
        image.load(r'sprites\left\3.png'),
        image.load(r'sprites\left\4.png'),
    ]
    walk_right = [
        image.load(r'sprites\right\1.png'),
        image.load(r'sprites\right\2.png'),
        image.load(r'sprites\right\3.png'),
        image.load(r'sprites\right\4.png'),
    ]
    return walk_left, walk_right
walk()


    
#zombie1 = image.load(r'images/chasing.png')
    

#piv_pav = image.load('c:/YuraWoin/game/images/pulya.jpg')