#versie 1.0
#auteur Teun van Dorp
#telt de basen en laat het CG% zien
gen = input("Wat is de sequentie? ")

aantal = len(gen)

print("Het aantal basen is: ", aantal)

c = gen.count('C')
g = gen.count('G')


print ("Het aantal CG basen is: ", c+g)

print ('Het CG prcentage is: ', (c+g)/aantal*100, '%')
