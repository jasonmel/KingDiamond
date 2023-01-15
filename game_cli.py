import random
import vlc

mp3_start = vlc.MediaPlayer('./music/game_start.mp3')
mp3_start.play()

player1 = ['D', 'C', 'B', 'A', 'B', 'C', 'D']
player2 = ['D', 'C', 'B', 'A', 'B', 'C', 'D']

while True:
  print(player1)
  print('===================================')
  print(player2)
  
  i1 = 0
  x1 = 'X'
  while x1 == 'X':
    i1 = random.randrange(len(player1))
    x1 = player1[i1]
  
  print('Enter your choice: ')
  x2 = input()
  while not x2 in {'A', 'B', 'C', 'D'} or not x2 in player2:
    print('Wrong input, enter again: ')
    x2 = input()
  i2 = player2.index(x2)
  
  print('Computer: ' + x1 + ', You: ' + x2)
  
  result = 'draw'
  if x1 == 'A':
    if x2 == 'A':
      result = 'draw'
    elif x2 in ['B', 'C']:
      result = 'You lose'
    else:
      result = 'You win'
  
  elif x1 == 'B':
    if x2 == 'A':
      result = 'You win'
    elif x2 == 'B':
      result = 'draw'
    else:
      result = 'You lose'
  
  elif x1 == 'C':
    if x2 in ['A', 'B']:
      result = 'You win'
    elif x2 == 'C':
      result = 'draw'
    else:
      result = 'You lose'
  
  else: #x1 == 'D'
    if x2 == 'A':
      result = 'You lose'
    elif x2 in ['B', 'C']:
      result = 'You win'
    else:
      result = 'draw'

  if result == 'draw':
    weapon_cnt = { 'A': 6, 'B': 4, 'C': 3, 'D': 2 }
    weapon1 = random.randrange(weapon_cnt[x1]) + 1

    print('Your weapon (1 ~ ' + str(weapon_cnt[x1]) + '): ')
    tmp = input()
    while not tmp in '0123456789':
      print('Your weapon (1 ~ ' + str(weapon_cnt[x1]) + '): ')
      tmp = input()
    weapon2 = int(tmp)

    print('Computer: ' + x1 + str(weapon1) + ', You: ' + x1 + str(weapon2))

    if weapon2 == weapon1:
      result = 'draw'
    elif weapon2 < weapon1 or (weapon2 == weapon_cnt[x1] and weapon1 == 1):
      result = 'You win'
    else:
      result = 'You lose'
  
  print(result)
  if result == 'You win':
    player1[i1] = 'X'
  elif result == 'You lose':
    player2[i2] = 'X'
  
  if player1.count('X') == 7:
    print('Game over, you win!')
    break
  if player2.count('X') == 7:
    print('Game over, you lose!')
    break

