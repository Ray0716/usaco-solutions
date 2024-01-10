def match(a, b):
  for x in range(len(a)):
    if a[x-1] == b[x-1]:
      return True
    else:
      pass
  return False
  


def herdle(answer, guess):
  green = 0
  yellow = 0
  
  samelettercount = 0
  ylettercount = 0
  
  anslst = []
  guesslst = []
  
  greenindex = 0
  
  for x in answer:
    anslst.append(x)
    
  for x in guess:
    guesslst.append(x) # making lists of ans and guess
    
    
  #check for greens

  while match(guesslst, anslst):
    for x in range(len(anslst)):
      if anslst[x-1] == guesslst[x-1]:
        #green += 1
        greenindex = x
        
    del anslst[greenindex-1]
    del guesslst[greenindex-1] #delete the green ones so that no prblems in checking for yellow
      

  
  temp = anslst
  anslst = guesslst
  guesslst = temp

  green = 9 - len(guesslst)
  
  

  #check for yellow
  for x in guesslst:
    #print("x:" , x , "  GC:" , guesslst.count(x) , "  AC", anslst.count(x))
    if (guesslst.count(x) < anslst.count(x)) and anslst.count(x) != 0:
        yellow += guesslst.count(x)
        #if answer has more x than guess we ad it to yellow
        #print("#x in guess is less than in ans,  we give it x")
    else:
        yellow += anslst.count(x)
        #print("dumbass thats the problem  added:", anslst.count(x))


  
      #check if there is more X in answer than guess
      # if there is then leave yellow val alone
      # if not (less X in answer than guess), return # X in ans as yellow
      
    
    #check if letter is in ans, if it is check how many
  
  print(green)
  print(yellow)
  return(green, yellow)
  
  
guessin_one = input()
guessin_two = input()
guessin_thr = input()
ansin_one = input()
ansin_two = input()
ansin_thr = input()

guessin = guessin_one + guessin_two + guessin_thr
ansin = ansin_one + ansin_two + ansin_thr


herdle(str(guessin), str(ansin))
