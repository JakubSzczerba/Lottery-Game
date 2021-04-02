#Duży lotek moja wlasna koncepcja

import random

los = random.sample(range(1,49), k= 6)
los.sort()

try:
    
    print('Witamy w grze LOTTO. Wylosuj liczbe od 1 do 49')
   
    l1 = int(input(f'Liczba numer 1: '))
    if l1 <= 49:
        True
    else:
        print(f'{l1} jest poza zakresem')
        exit() 
    l2 = int(input(f'Liczba numer 2: ')) 
    if l2 <= 49 and l2 !=l1:
        True
    else:
        print(f'{l2} jest poza zakresem')
        exit()    
    l3 = int(input(f'Liczba numer 3: ')) 
    if l3 <= 49 and l3 !=l2:
        True
    else:
        print(f'{l3} jest poza zakresem')
        exit()    

    l4 = int(input(f'Liczba numer 4: '))   
    if l4 <= 49 and l4 !=l3:
        True
    else:
        print(f'{l4} jest poza zakresem')
        exit()    

    l5 = int(input(f'Liczba numer 5: '))  
    if l5 <= 49 and l5 !=l4:
        True
    else:
        print(f'{l5} jest poza zakresem')
        exit()    

    l6 = int(input(f'Liczba numer 6: '))
    if l6 <= 49 and l6 !=l5:
        True
    else:
        print(f'{l6} jest poza zakresem')
        exit()    
      
except ValueError:
    print ('Błędne dane')
    exit()

mynum = [l1, l2, l3, l4, l5, l6]
mynum.sort()
print(f"WYLOSOWANE LICZBY: {los}")
print(f"TWOJE LICZBY:      {mynum}")
c = [i for i in mynum if i in los]
print(f'Twoje trafienia:   {c}')

if len(c) == 0:
    print(f'Próbój dalej :)')
elif len(c) == 1:
    print(f'Jedna trafiona liczba. Od teraz {len(c)} to twój szczęśliwy numer.')
elif len(c) == 2:
    print(f'Dwa trafienia, brawo!')
elif len(c) == 3:
    print('GRATULACJE! Wygrywasz 20 zł')
elif len(c) == 4:
    print('GRATULACJE! Wygrywasz 58 zł')
elif len(c) == 5:
    print('GRATULACJE! Wygrywasz 1000 zł')
elif len(c) == 6:
    print(f'Udało się Tobie trafić 6 liczb. Wygrywasz 3 000 000 zł')
