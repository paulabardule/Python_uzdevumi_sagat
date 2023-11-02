"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.
5...V
Datu struktūra - {} tā tukša vārdnīca, dict()
atslēga...vērtība - vārdnīca
cipari 1,2,3,4,5,6,7,8,9
       I, IV, V, IX..
    1984
"""

class AAA: # klasi definē "class" nosaukums AAA, aiz nosaukuma vienmer :
    def __init__(self): #klasei ir konstruktors (__init__) un metodes (funkcijas) iekavas tiek rakstiti parametri (klasesiekšējais mainīgais)
        self.rom_cip={ # self.rom_cip definēts iekšējais mainīgais { norada ka ta ir datu struktura} ja tas ir tuksas tad ta ir tuksa vardnica ar vardnicu jasaprot tabulu (1 kolonna ir atslega otra vertiba)
            1: 'I',
            4:'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    def uz_romu(self, num):
       result="" # result ir ieksejais mainigais "" - saraksts bet "tuksa simbolu virkne"
       for value, sk in sorted(self.rom_cip.items(),key=lambda x:x[0], reverse=True): # value un sk ir cikla skaititaji in norada ka tie darbosies apganala sorted norada ka pagabals ir sakartots lambda 
           while num>=value:
               result+=sk
               num-=value
       return result

skaitlis=2 # var likt jebkuru skaitli kuru grib izdrukat
konvertet=AAA()# define jaunu objektu jauns objekts ar nosaukumu konvertet objektus var izveidot tikai tad kad ir klase
rom_sks=konvertet.uz_romu(skaitlis) # mainigais ir ar nosaukumu roma_sks mainigajam pieksir vertibu objektam tiek izsaukta metode ar . 
print(f"{skaitlis} romiešu ciparos ir {rom_sks}.")
    
