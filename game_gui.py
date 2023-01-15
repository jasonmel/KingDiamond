import random
import vlc
import time

from tkinter import *
from tkinter import messagebox
root = Tk()

mp3_start = vlc.MediaPlayer('./music/game_start.mp3')
mp3_start.play()

def play_dead():
  mp3_start.set_pause(1)
  mp3_dead = vlc.MediaPlayer('./music/dead.mp3')
  mp3_dead.play()
  #time.sleep(4)
  mp3_start.set_pause(0)

player1 = ['D', 'C', 'B', 'A', 'B', 'C', 'D']
player2 = ['D', 'C', 'B', 'A', 'B', 'C', 'D']
photo1 = []
photo2 = []
button1 = []
button2 = []

deadPhoto = PhotoImage(file='./image/dead.png')

def callback(i2):
  i1 = 0
  x1 = 'X'
  while x1 == 'X':
    i1 = random.randrange(len(player1))
    x1 = player1[i1]

  x2 = player2[i2]

  print(i1, x1, i2, x2)

  for i in range(3):
    button1[i1].after(400 * i + 200, lambda: button1[i1].configure(highlightbackground='red'))
    button2[i2].after(400 * i + 200, lambda: button2[i2].configure(highlightbackground='red'))
    button1[i1].after(400 * i + 400, lambda: button1[i1].configure(highlightbackground='SystemButtonFace'))
    button2[i2].after(400 * i + 400, lambda: button2[i2].configure(highlightbackground='SystemButtonFace'))

  result = 'draw'
  if x1 == 'A' and x2 == 'D':
    result = 'You win'
  elif x1 == 'D' and x2 == 'A':
    result = 'You lose'
  elif x1 < x2:
    result = 'You lose'
  elif x1 > x2:
    result = 'You win'

  print(result)

  if result == 'You win':
    button1[i1]['text'] = 'X'
    button1[i1]['image'] = deadPhoto
    player1[i1] = 'X'
    play_dead()
  elif result == 'You lose':
    button2[i2]['text'] = 'X'
    button2[i2]['image'] = deadPhoto
    player2[i2] = 'X'
    button2[i2]['state'] = DISABLED
    play_dead()

  if player1.count('X') == 7:
    print('Game over, you win!')
    result = messagebox.showinfo(title='Game over', message='Game over, you win!')
    root.destroy()
  if player2.count('X') == 7:
    print('Game over, you lose!')
    result = messagebox.showinfo(title='Game over', message='Game over, you lose!')
    root.destroy()

for i in range(len(player1)):
  photo1.append(PhotoImage(file = './image/' + player1[i] + '1.png'))
  button1.append(Button(root, text=player1[i], image=photo1[i]))
  button1[i].configure(highlightbackground='SystemButtonFace')
  button1[i].grid(row=0, column=i)
  button1[i]['state'] = DISABLED

wallPhoto = PhotoImage(file='./image/wall.png')
wall = Button(root, image=wallPhoto)
wall.grid(row=1, column=0, columnspan=7)

for i in range(len(player2)):
  if i == 5:
    photo2.append(PhotoImage(file = './image/' + player2[i] + '2_2.png'))
  else:
    photo2.append(PhotoImage(file = './image/' + player2[i] + '2.png'))
  button2.append(Button(root, text=player2[i], image=photo2[i], command=lambda i=i: callback(i)))
  button2[i].configure(highlightbackground='SystemButtonFace')
  button2[i].grid(row=2, column=i)

root.mainloop()
