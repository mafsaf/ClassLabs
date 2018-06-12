import os
def Correct():
    os.system('clear')
    print('Correct you entered: ', '\033[1;32m', useguess, '\033[1;m')
    print('It took you ', '\033[1;32m', str(Guesses-1), '\033[1;m', ' guess(es).')
    if Guesses >= 2:
       print('You also guessed: ')
       print(userguesses)
    return;

def InCorrect():
    os.system('clear')
    print('Sorry your guess of:', '\033[1;31m', useguess, '\033[1;m', ' is incorrect.')
    print('you have ', '\033[1;36m', str((limit-Guesses)+1), '\033[1;m', ' attempt(s) left.')
    print('')
    wait = input('Press ENTER to retry')
    os.system('clear')
    return;

fruit_basket = ['banana','apple','pear','plum','orange']
limit = 5
userguesses = []
Guesses = 1
while True:
   Guesses += 1
   os.system('clear')
   useguess = input('Please guess a fruit: ')
   userguesses.append(useguess)
   if useguess.lower() in fruit_basket:
      Correct()
      break 
   else:
      InCorrect()
   if Guesses > limit:
      os.system('clear')
      print('\033[1;38m', 'Sorry you have had too many tries!', '\033[1;m')
      print('Your guesses are:')
      print(userguesses)
      break
