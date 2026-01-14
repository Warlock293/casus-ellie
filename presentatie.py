def presenteer(dict, totaal):
    for key in dict:
        print (key, ':' , dict [key], 'euro')
    print ("============================")
    print ('totaal:' , totaal, 'euro')
   


mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50

for item, bedrag in mijn_dict.items():
    print(f"{item} : {bedrag} euro")

print("=" * 26)
print(f"totaal : {totaal} euro")
print()