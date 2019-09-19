# vaken 

vaken = "n"

print("Du sover djupt som en björnen i ide...") #skriver ut början på koden

while vaken == "n": #skappar en loop till vaken om användaren svarar nej
      vaken = input("vaknar du [y/n]: ").lower() #ger användare input till Ja och nej svar medans convertera till minder bokstäver  

print("Du masar dig upp och släpper dig in i dushcen.") # nästa steg efter ja svar.
print("Någon har lämnat en brödråst") #Problem dycker upp och användare ska mötas i val

duscha = input("flyttar du på brödråsten i duschen? [y/n]:  ").lower() #ger användaren svara på ja eller nej inom input.

if duscha == "n": #svar för nej visar användaren chockades ijäll och konsolen avslutas
    print("Du tror brödråsten är kul att duscha med en brödråst, men du chockades ijäll")
    exit() # avslutar konsolen
elif duscha == "y": #Anars
    print("Du valde att flytta brödråsten till köket, och du fortsatte en vanligt dusch")
else:
  print("Du måste svara en av frågora")
  
#årstid

season = False
while season == False:
    season = input("vilken årstid [vinter, sommar, vår, höst]: ").lower()
    if season == "vår" or season == "vinter" or season == "höst" or season == "sommar":
        print("Det är kallt")
        print("du klär dig i vinterpälsen")
    elif season == "sommar":
        print("sommar och lättklädd är passande")
    else: 
        season = False
        
# Buss eler cykla

season2 = sommar 

print("ska du ta en cykel tur")