Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> py
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    py
NameError: name 'py' is not defined
>>> 2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3

# Verander <JOUW NAAM HIER> in je eigen naam
print('Mijn naam is Vincent')
naam = 'Vincent'

print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])

# Verander dit in je eigen leeftijd
leeftijd = 17
print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
leeftijd = leeftijd + 1
leeftijd
leeftijd-=1
leeftijd

if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

# Willekeurige getallen genereren
from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

# Datum en tijd
from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %B %Y')

# Nu in een andere taal
import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Vincent')
Mijn naam is Vincent
>>> naam = 'Vincent'
>>> print(naam)
Vincent
>>> print(naam.upper())
VINCENT
>>> print(naam[0:2])
Vi
>>> print(naam[::-1])
tnecniV
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Vincent ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

Over 1 jaar wordt je 18
>>> randint(0,1000)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    randint(0,1000)
NameError: name 'randint' is not defined
>>> from random import randint
>>> randint(0,1000)
751
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
761
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 761
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 14:26:32.309935
>>> datum.strftime('%A %d %B %Y')

'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 