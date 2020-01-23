number_to_gess = 2    #cuando se usa un igual, es para asignar.

user_number = int(input("Adivina un numero: "))

if number_to_gess == user_number:   #Cuando se usan dos iguales es para comparar
    print("Has ganado")
else:
    print("Has perdido")