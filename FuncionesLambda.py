numeros = [1,5,8,10]
restarNumero = list(map(lambda x: x - 1, numeros))   
mayoresCinco = list(filter(lambda x: x > 5 , numeros))

print(restarNumero)
print(mayoresCinco)