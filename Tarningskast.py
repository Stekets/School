import random
import datetime 

#Krav på programmet:
#Ska Köra 1000 gånger (forloop)
#slumpa 5 tärningskast random mellan siffrorna 1-6
#Kolla om två lika och endast två. Om fler än två är lika ska den inte räknas som ett par. Är det endast ett par ska den räknas.
#Spara vilket nummer paret är
#Sparade numret + resultatet skrivs över till en textfil.



savedDice = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
} # Variabel som sparar antal par 

dices = 5 # En variabel som sparar antalet tärningar

for i in range(1000): #En for-loop som kör programmet 1000 gånger
    rolledDice = [] # tom lista för den rullade tärningens utfall
    savedNumber = [] # antalet nummer-par som sparas i en lista
    pair = False # variabel som anger falsk
    
    for dice in range(dices): # För varje tärning i listan dices (dvs 5st)

        rolledDice.append(random.randint(1,6))   #slumpas tärningarna random 1-6
  
        
    for tc in rolledDice: #Checkar om vi har ett par
        if rolledDice.count(tc) >= 2 and tc not in savedNumber: # Checkar att antalet tärningar är mer än 2 för att möjligt kunna få par
            savedNumber.append(tc) #lägger till tärningskastet i savedNumber
            
    if len(savedNumber) == 1: # Om längden på savedNumber är 1 (ett par)
        for t in rolledDice: # Kollar värdet i rolled dice
            if t in rolledDice and rolledDice.count(t) == 2 and pair == False: #Uppfylls kraven om att tärningarnas värde i rolled dice och antalet tärningar är endast 2 och statusen på par är falsk
                pair = True # Så kommer paret bli sant
                savedDice[t] += 1 # Och spara tärningen i savedDice
            
    print("You rolled: ", rolledDice)   #Printar alla tärningsutfall
print("Here is: ", savedDice) #Printar dictionaryn med antalet par för resp. möjligt utfall

total="Total: ", (sum(savedDice.values())) #Summerar totalen på antalet par
today = datetime.datetime.now() #Datum & tid för när kasten gjordes
with open('savedDice.txt', 'a') as f: #Skapar en textfil savedDice som lägger till 
    print(savedDice, total, today, file=f)





        
        
