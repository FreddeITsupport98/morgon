# vaken

vaken = "n"

print("Du sover djupt som en björnen i ide...")  # skriver ut början på koden
print('\v')
while vaken == "n":  # skappar en loop till vaken om användaren svarar nej

    # ger användare input till Ja och nej svar medans convertera till minder bokstäver
    vaken = input("vaknar du [y/n]: ").lower()

# nästa steg efter ja svar.
print("Du masar dig upp och släpper dig in i dushcen.")
print('\v')
# Problem dycker upp och användare ska mötas i val
print("Någon har lämnat en brödråst")

# ger användaren svara på ja eller nej inom input.
duscha = input("flyttar du på brödråsten i duschen? [y/n]:  ").lower()
print('\v')
if duscha == "n":  # svar för nej visar användaren chockades ijäll och konsolen avslutas
    print("Du tror brödråsten är kul att duscha med en brödråst, men du chockades ijäll")
    exit()  # avslutar konsolen
elif duscha == "y":  # Anars
    print("Du valde att flytta brödråsten till köket, och du fortsatte en vanligt dusch")
    print('\v')
else:
    print("Du måste svara en av frågora")

# årstid

season = False
while season == False:
    season = input("vilken årstid [vinter, sommar, vår, höst]: ").lower()
    print('\v')
    if season == "vår" or season == "vinter" or season == "höst" or season == "sommar":
        print("Det är kallt")
        print('\v')
        print("du klär dig i vinterpälsen")
    elif season == "sommar":
        print("sommar och lättklädd är passande")
    else:
        season = False
print('\v')
print('\v')
# Åka Buss eller  cykla

print("Det är att dags att gå till skola men vad är för månad  du behöver kolla up kalandern.")

season2 = input(
    "Du ser månaden men skriv endast i förkortningar som ([jan] [feb] [mar] [apr] [maj] [jun] [jul] [aug] [sep] [oct] [nov] [dec]): "
)
print('\v')

if season2 == "jan" or season2 == "feb" or season2 == "mar":

    season2 = "vår"
    
    print("Det ser ut som det är fråssigt men påväg bli vår i denna sesång.")
    print('\v')
    season2 = input("vill du ta bussen till skolan? [Ja/Nej]: ").lower()
    if season2 == "ja":
        print("Du åker till skolan i varm buss")

    elif season2 == "nej":
        print("Du kommer du håller på komma försent men valde att cykla fast det är isigt")
    else:
        print("Välj minst en av svaren.")

elif season2 == "apr" or season2 == "maj" or season2 == "jun" or season2 == "jul":

    season2 = "sommar"
    
    print("Sommaren är framme och solstrålen från solen visar att vara klardag.")
    print('\v')
    season2 = input("vill du ta cykel till skolan? [Ja/Nej]: ").lower()
    if season2 == "ja":
        print("Du cyklar till skolan i varm soldag")

    elif season2 == "nej":
        print(
            "Du valde att spara på kalorier för preparation inför vinter. Du tar en buss tid")
    else:
        print("Välj minst en av svaren.")

elif season2 == "aug" or season2 == "sep" or season2 == "oct":
    
    season2 = "hösten"
    
    print("Träden är gulnar och djuren lagrar maten, hösten är här.")
    print('\v')
    season2 = input("vill du ta cykel till skolan? [Ja/Nej]: ").lower()
    if season2 == "ja":
        print("Du cyklar till skolan i fast mer påklädd")

    elif season2 == "nej":
        print(
            "Du valde att inte låta smått kal luft röra din skin. Du valde åka bussen")
    else:
        print("Välj minst en av svaren.")

elif season2 == "nov" or season2 == "dec":

    season2 = "vinter"
    print('\v')
    print("Så kallt vinter is coming. Är jultomten snart här?")
    
    season2 = input("vill du ta buss till skolan? [Ja/Nej]: ").lower()
    if season2 == "ja":
        print("Du cyklar till skolan i kyligt grad men också valde du att spara mer på naturen")

    elif season2 == "nej":
        print(
            "Du valde inte låta vintern vinna över dig och gav upp dig till värmen när du steg på bussen")
    else:
        print("Välj minst en av svaren.")

else:
    print("du måste skriva månaden i 3 tecken som t.ex. (jan)")
