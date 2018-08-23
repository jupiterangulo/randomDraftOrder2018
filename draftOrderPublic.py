# import libraries 
import random
import time

# create function for Draft Order 
def assignDraftOrder():
  
  # enter number of players in your league
  size = 10 #default to 10
  
  # insert players names here 
  players = ['Bob', 'Ray', 'Fred', 'Leroy', 'Otis',
             'Chet', 'Chad', 'Miles', 'Guy', 'Clay']
  
  print ('The order of players as they joined is:')
  for i in range(0,size):
    j = i + 1
    print ("{}. {}".format(j, players[i]))
    
  # randomize the list to get the draft order 
  draftOrder =  random.sample(players, len(players))

  # dramatic pause 
  time.sleep(5)

  # output the draft order with a dramatic pause 
  print ('The Draft Order Is:')

  # one more dramatic pause because why not
  time.sleep(3)
  for i in range(0,size):
    j = i + 1
    print ("{}. {}".format(j, draftOrder[i]))
    time.sleep(3)
    
