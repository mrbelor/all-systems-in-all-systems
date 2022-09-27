def convert(chislo,number_system,target_system):
    #chislo(str); number_system(int);target_system(int)
    i10 = int(str(chislo),number_system)
    
    alfabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    while i10>0:
        k = i10%target_system   #очередная цифра
        result = alfabet[k]+result #приклеиваем спереди в соответствии с алфавитом
        i10 = i10//target_system
    return result
#---------------------------------------------------------
quite_or_not = "y"
while True:
    if quite_or_not == "y":
        x = input("Введите число\n")
        y = int(input("В какой системе это число? (>= 2 и <= 36)\n"))
        z = int(input("В какую систему хотите первести? (>= 2 и <= 36)\n"))
        #позже z будет изменено на меняющуюся i

        print(f"В {z} это",convert(x,y,z))

    elif quite_or_not == "n":
        break
    else:
        print("\nЕщё раз спрашиваю!")
    
    quite_or_not = input("Хотите преобразовать ещё одно число? (y/n)")
