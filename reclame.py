from algemene_functies import mijn_functie_2


def combinatie(mijn_functie_2):
                laagste_waarde = min ()
                hoogste_waarde = max ()
                korte_lijst = laagste_waarde + hoogste_waarde(mijn_functie_2)
                uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
                return uitvoer



print ()

# huiswerk code nr 5 hieronder
smaak = "aardbei"
prijs = "4 euro"
korting = "3 euro"


def aanbieding_1(smaak,prijs,korting):
        uitvoer = (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {korting}.")
        return uitvoer

print (aanbieding_1(smaak,prijs,korting))


# huiswerk code nr 6 en 7 hieronder
inkomsten = [30 + 25 + 18 + 32 + 52 + 45 + 22]
totaal_bedrag = sum (inkomsten)
belasting = 0.09
btw = totaal_bedrag * belasting
# na de inkomsten van een week, totale bedrag (is sum dus summary van een reeks getallen) = sum (inkomsten) daarna 
# belasting definieeren met =, daarna de btw word totaal (sum) * belasting, dan heb je
# dat vastgelegd voor je def regels.


def inkomsten_totaal(totaal_bedrag, btw: str):
        aanbieding = (f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald moet worden")
        print (aanbieding)

print ()

inkomsten_totaal (totaal_bedrag, btw)

# Huiswerk code nr 8 hieronder:

getallen_lijst = [22, 25, 16, 30, 40, 35, 28]

def laagste_hoogste(getallen_lijst):
                laagst = min (getallen_lijst)
                hoogste = max (getallen_lijst)
                return (laagst,hoogste)
                
print ()
               
print (laagste_hoogste(getallen_lijst))

# code 9
# EERST definieeren van de code bijv def gemiddelde ( uitgaven )
# Daarna, som = sum (waarden of in dit geval uitgaven)
# Daarna, aantal = len (uitgaven tussen ())
# Daarna, bedrag = som/aantal
# Daarna de zin in formatted string (f" zin zin" met *bedrag* tussen {})
# Dan onder de def, 2 x enter dus, de waarden van uitgaven definieren: uitgaven = ...
# Resultaat = bereken_en_toon_gemiddelde (bedrag) dan print resultaat


uitgaven = [24, 25, 18, 32, 28, 16, 40]

def gemiddelde(uitgaven):
                som = sum (uitgaven)
                aantal = len (uitgaven)
                bedrag = som/aantal 
                return (f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro.")

print ()

print (gemiddelde(uitgaven))



# Na bedrag in de formatted string, : dus dubbele punt, dan een . dus een punt, dan een 2 en f, 
# dat rond af tot de 2 decimalen.
# de :.2f is een formatterende code voor een float, om het netter af te ronden.

# En nu de code voor vraag 11.

invoer_lijst = [15, 18, 14, 12, 2, 3, 4, 6, 5, 10]

def meervoudig(invoer_lijst):
                laagst = min (invoer_lijst)
                hoogste = max (invoer_lijst)
                return (laagst,hoogste)
                
print ()
               
print (laagste_hoogste(invoer_lijst))