sexo = input("INFORME O SEU SEXO(Masculino:M) (Feminino:F)")
print(sexo)
altura = float(input("INFORME A SUA ALTURA"))
print(altura)
peso = float(input("INFORME O SEU PESO"))
print(peso)
alt2 = (float(altura) * float(altura))
imc = (float(peso) / float(alt2))
print("seu IMC e de", imc)
homem = (float(72.7) * float (altura)) - 58
print("HOMEM, seu PESO IDEAL seria de", homem)
mulher = (float(62.1) * float (altura)) - 44.7
print("MULHER, seu PESO IDEAL seria de", mulher)