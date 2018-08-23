# import libraries 
import random
import time

# create function for Draft Order 
def assignDraftOrder():
  
  # insert players names here 
  players = ['Bob', 'Ray', 'Fred', 'Fred2']
  
  # list out players as they appear in the fantasy football league 
  print ('The order of players as they joined is:')
  
  for i in range(0,10):
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
  for i in range(0,10):
    j = i + 1
    print ("{}. {}".format(j, draftOrder[i]))
    time.sleep(3)
    
