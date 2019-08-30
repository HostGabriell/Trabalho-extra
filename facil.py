valor = int(input("INSIRA O VALOR"))
print(valor)
prct = int(input("INSIRA O DESCONTO"))
print(prct)
dsct = (valor * prct / 100)
vf = valor - dsct
print("o produto de", valor, "ficou por", vf, "com desconto de", prct, "porcento")