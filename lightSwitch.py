def Light():
  while True:
    #ask for user input
    choice1 = str(input("is the light on or off?: "))
    #check if switch is on 
    if choice1.lower() == "on":
      print("the light is on ") #on output to screen
      break
    #check else if switch is  off  
    elif choice1.lower() == "off":
      print("the light is off") #off output to screen
      break
Light()    
    
   
    
  
