from Classes.fraction import Fraction
from Classes.polynomial import Polynomial
import time

numerator = input("Numarator: ")
denominator = input("Numitor: ")

first_fraction = Fraction(numerator, denominator)

print "Fractia ireductibila este: ", \
    first_fraction.get_fraction(), "\n"

numerator = input("Numarator2: ")
denominator = input("Numitor2: ")

second_fraction = Fraction(numerator, denominator)

print "Fractia ireductibila este: ", \
    second_fraction.get_fraction(), "\n"

question = input("Alege operatie:\n"
                 "1) Adunare\n"
                 "2) Scadere\n"
                 "3) Inmultire\n"
                 "4) Impartire\n")

result = -1
if question == 1:
    result = first_fraction + second_fraction
elif question == 2:
    result = first_fraction - second_fraction
elif question == 3:
    result = first_fraction * second_fraction
elif question == 4:
    result = first_fraction / second_fraction
else:
    exit(0)

print "Rezultatul este: ", \
    result.get_fraction(), "\n"

print "Ok..."
time.sleep(1)
print "Hai sa ne jucam cu polinoame !"
time.sleep(1)

coefficients_number = input("Numar coeficienti: ")
print "Ok, am inteles ca ai cerut sa citim un polinom cu ", coefficients_number, " coeficienti"
time.sleep(1)
print "Sa trecem la treaba, hai sa il citim: "

coefficients = list(range(coefficients_number))

for i in range(coefficients_number):
    print "Coeficient ", i, ": "
    coefficients[i] = input()

time.sleep(1)
print "Acum astept o valoare pentru x"
numerator = input("Numarator x: ")
denominator = input("Numitor x: ")

polynomial = Polynomial(coefficients, Fraction(numerator, denominator))
print "Am obtinut valoarea: ", polynomial.get_value().get_fraction()
print "Radacini:", polynomial.get_roots()