#versie 1.1
#auteur Teun van Dorp
#telt de basen en laat het GC% zien
gen = input("Wat is de sequentie? ")

aantal = len(gen)

print("Het aantal basen is: ", aantal)

c = gen.count('C')
g = gen.count('G')


print ("Het aantal GC basen is: ", c+g)

print ('Het GC prcentage is: ', (c+g)/aantal*100, '%')
