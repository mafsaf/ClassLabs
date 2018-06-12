def agein2035():
   print('Please enter your current age:')
   todayage = int(input())
   while todayage <= 150:
      import datetime
      import os
      now = datetime.datetime.today()
      ageat2035 = int(2035 - now.year + todayage)
      birthyear = int(now.year - todayage)
      os.system('clear')
      print("You were born in, ",now.year - todayage,", and you are ",todayage,".  In 2035 you will be ",2035-now.year+todayage,".")
      print('Enter another age:')
      print('Enter a nuber greater than 150 to quit')
      todayage = int(input())
   now = datetime.datetime.today()
   ageat2035 = int(2035 - now.year + todayage)
   birthyear = int(now.year - todayage)
   os.system('clear')
   print('WOW! You were born in, ',birthyear,', and you are ',todayage,'.  In 2035 you will be ',ageat2035,'.')

agein2035()

