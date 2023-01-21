"""
Ratkaistaan rekursiivinen yhtälö xn=rxn(1−xn)


"""
import matplotlib.pyplot as plt

# Määritellään alkuarvo
x0=0.5 # alkuarvo X0 
xn =x0 # alkuarvo XN (lopullinen vastaus)
r =2.9 # r-kertoimen arvo
n=50  # iteraatioiden määrä
x_values = [] # lista, johon tallennetaan iteraatioiden tulokset
x_values.append(x0) # Lisätään alkuarvo listaan"
for n in range(n):
    xn=r*xn*(1-xn)
    x_values.append(xn) # Lisätään lopullinen arvo listaan
# Tulostetaan lopullinen arvo
#print(xn)



print(x_values)

