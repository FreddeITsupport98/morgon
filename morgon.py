# vaken 

vaken = "n"

print("Du sover djupt som en björnen i ide...")

while vaken == "n":
    vaken = input("vaknar du [y/n]: ").lower()   

print("Du masar dig upp och släpper dig in i dushcen.")
print("Någon har lämnat en brödråst")

duscha = input("flyttar du på brödråsten i duschen? [y/n]:  ").lower()

if duscha == "n": 
    print("Du tror brödråsten är kul att duscha med en brödråst, men du chockades ijäll")
    exit()
elif duscha == "y":
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