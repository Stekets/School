import random
import datetime 

#Kör 1000 gånger
#slumpa 5 siffror
#Kolla om två lika -> räknare går upp
#Spara vilket nummer paret är
#Om fler än två är lika, skippa att räkna
#Nytt försök
#Sparade numret + resultatet in i excelfil
#


savedDice = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
}

dices = 5 # En variabel med antalet tärningar

for i in range(1000): #Ska vara 1000 i parantes när programmet är klart
    rolledDice = [] # tom lista för ett tärningskast
    savedNumber = [] # antalet nummer-par som sparas i en lista
    pair = False
    
    for dice in range(dices): # För varje tärning i listan dices (dvs 5st)

        rolledDice.append(random.randint(1,6))   #slumpas tärningarna random 1-6
    
    # rolledDice = [] test
    # rolledDice = [4,3,4,3,3] test
        
    for tc in rolledDice: # För varje tärningscheck i listan rolled dice
        if rolledDice.count(tc) >= 2 and tc not in savedNumber: # Om tärningen i listan är större eller är lika med två par i ett kasst och om tärningskastet inte sparats i savednumber
            savedNumber.append(tc) #sparas tärningskastets par i saved number
            
    if len(savedNumber) == 1: # Om längden på savedNumber är 1
        for t in rolledDice: # Och om varje tärning i rolled dice uppfyller
            if t in rolledDice and rolledDice.count(t) == 2 and pair == False: #Kraven om att tärningen är i listan och tärningen har ett par
                pair = True # Så kommer paret bli sant
                savedDice[t] += 1 # Och spara tärningen i savedDice
            
    print("You rolled: ", rolledDice)   
print("Here is: ", savedDice)

total="Total: ", (sum(savedDice.values()))
today = datetime.datetime.now()
with open('savedDice.txt', 'a') as f:
    print(savedDice, total, today, file=f)





        
        