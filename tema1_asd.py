from Classes.fraction import Fraction
from Classes.polynomial import Polynomial
from Classes.number import Number
from Classes.phrase import Phrase
from Classes.networking import Networking
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

print("Hai sa convertim un numar!")
number = input("Numar: ")
number = Number(number)

print "Baza 2", number.to_base2()

# Serii
e = 0.00005
x = 0.5


def term(i):
    if x <= i:
        if i == 1:
            return x - 1
        return term(i - 1) * (1 - x) * (1 - 1/i)
    else:
        if i == 1:
            return (x - 1) / x
        return term(i - 1) * ((x - 1) / x) * (1 - 1/i)


def series_sum():
    i = 1
    sum_series = 0

    while abs(term(i)) > e:
        sum_series += term(i)
        i += 1

    return sum_series, i-1


print "Suma seriei: ", series_sum()

# Criptare fraza
print "Hai sa criptam o fraza !"
time.sleep(1)
phrase = raw_input("Fraza: ")
phrase = Phrase(phrase)

print "Avem ", phrase.get_words_count(), " cuvinte"
print "Cuvintele sunt:", phrase.get_words()
phrase.encrypt_phrase()
print "Fraza criptata este: ", ' '.join(phrase.get_words())

# Generare ip
networking = Networking()
networking.generate_ip()

print "IP random: ", networking.get_ip()
