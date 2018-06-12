fruit_basket = ['bannana','apple','pear','plum','orange']
Guesses = 1
while True:
   Guesses += 1
   useguess = input('Please guess a fruit: ')
   if useguess in fruit_basket:
      print('Correct you did it in ' + str(Guesses-1) + ' guess(es).')
      break 
   else:
      print('Try again')
   if Guesses > 5:
      print('Sorry you have had too many tries!')
      break
