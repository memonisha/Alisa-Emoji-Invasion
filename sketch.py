from p5 import *
def setup():
  createCanvas(windowWidth,windowHeight)
  global stickgirl,e1,e2,e3,e4,e5,e6,e7,e8,e9,gameState,stickX,score,level, highscore
  highscore=0
  score=0
  level=1
  gameState="play"
  loadImage('stickalisa.png','stick')
  loadSound('clown.mp3','music')
  stickX=0
#dictionary -> {key:value,key:value,key:value..........}
  #dictionary is a collection of key:value pairs
  e1={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e2={
    'x':random(0,width),
    'y':random(500,height+100)
  }
  e3={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e4={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e5={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e6={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e7={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e8={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e9={
    'x':random(0,width),
    'y':random(350,height+100)
  }

def draw():
  global stickgirl,e1,e2,e3,e4,e5,e6,e7,e8,e9,gameState,stickX,level,score
  #rgba-> 4th is a-alpha(transparency)
  changeBackground()
  fill('crimson')
  rect(0,0,width,20)
  image(assets['stick'],stickX,20,50,50)
  print(gameState)
  


  drawEmoji(e1)
  drawEmoji(e2)
  drawEmoji(e3)
  drawEmoji(e4)
  drawEmoji(e5)
  drawEmoji(e6)
  drawEmoji(e7)
  drawEmoji(e8)
  drawEmoji(e9)

  scoreBoard()
  changeLevel()




  if gameState=="over":

    assets['music'].stop()
    push()
    fill("white")
    textSize(150)
    textFont("georgia")
    textAlign(CENTER)
    text("GAME OVER",width/2,height/2)
    pop()
  if gameState=="play":
    stickX=mouseX
    fallEmoji(e1)
    fallEmoji(e2)
    fallEmoji(e3)
    fallEmoji(e4)
    fallEmoji(e5)
    fallEmoji(e6)
    fallEmoji(e7)
    fallEmoji(e8)
    fallEmoji(e9)

    collideEmoji(e1)
    collideEmoji(e2)
    collideEmoji(e3)
    collideEmoji(e4)
    collideEmoji(e5)
    collideEmoji(e6)
    collideEmoji(e7)
    collideEmoji(e8)
    collideEmoji(e9)
    if (not(assets['music'].isPlaying())):
      assets['music'].play()



  #crosshair()
  #drawTickAxes()

def drawEmoji(emo):
  global level
  textSize(40)
  if level==1:
    text("😄",emo['x'],emo['y'])
  elif level==2:
    text("🙂",emo['x'],emo['y'])
  elif level==3:
    text("😒",emo['x'],emo['y'])
  elif level==4:
    text("😠",emo['x'],emo['y'])
  elif level==5:
    text("😡",emo['x'],emo['y'])
  elif level==6:
    text("🤬",emo['x'],emo['y'])


def fallEmoji(emo):
  global score,level
  #print("fall")
  if level==1:
    emo['y']=emo['y']-5
  elif level==2:
    emo['y']=emo['y']-6
  elif level==3:
    emo['y']=emo['y']-8
  elif level==4:
    emo['y']=emo['y']-10
  elif level==5:
    emo['y']=emo['y']-11
  elif level==6:
    emo['y']=emo['y']-13
  if emo['y'] < 0:
    score=score+1
    emo['y']=height+50
    emo['x']=random(0,width)

def collideEmoji(emo):
  global gameState, highscore
  distX=abs(emo['x']-mouseX)
  distY=abs(emo['y']-20)
  #print(distX)
  if distX<20 and distY<20:
    print("oh no")
    
    gameState="over"
    if highscore < score:
      highscore = score

def scoreBoard():
  global score, highscore
  fill(197, 89, 255)
  noStroke()
  rect(width-350,height-120,300,110,10)
  fill("white")
  textSize(30)
  text(f"score : {score}",width-320,height-50)
  text(f"highscore: {highscore}",width-320,height-110)



def changeLevel():
  global score,level
  if score<=20:
    level=1
  elif score<=40:
    level=2
  elif score<=60:
    level=3
  elif score<=80:
    level=4
  elif score<=120:
    level=5
  else:
    level=6

  fill("white")
  textSize(30)
  text(f"level : {level}",width-320,height-80)

def changeBackground():
  global level 
  if level==1:
    background(41, 188, 224,30)
  elif level==2:
    background(66, 135, 245,30)
  elif level==3:
    background(24, 87, 186,30)
  elif level==4:
    background(48, 24, 186,30)
  elif level==5:
    background(81, 2, 150,30)
  elif level==6:
    background(128, 14, 29,30)

def mousePressed():
  global gameState, score
  if gameState == "over":
    gameState = "play"
    score = 0
  










