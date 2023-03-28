#Sistema de Cafeteria

#Recebe Cupons

#Sempre tenta vender o maior café que seu cupom pode pagar

pequeno = 2
medio = 5
grande = 6
extraGrande = 8

print("Qual o valor do seu cupom?")
cupom = input()

if not cupom.isdigit():
  print("Insira um cupum válido")
  exit()
else:
  cupom = int(cupom)
  if cupom >= extraGrande:
    print("Você consegue pagar pelo café extra grande")
    if cupom == extraGrande:
      print("Compra concluída")
    else:
      print("Seu troco é", cupom - extraGrande)
  elif cupom >= grande:
    print("Você consegue pagar pelo café grande")
    if cupom == grande:
      print("Compra concluída")
    else:
      print("Seu troco é", cupom - grande)
  elif cupom == medio:
    print("Você consegue pagar pelo café médio")
    print("Compra concluída")
  elif cupom >= pequeno:
    print("Você consegue pagar pelo café pequeno")
    if cupom == pequeno:
      print("Compra concluída")
    else:
      print("Seu troco é", cupom - pequeno)

class Cafe():
  def __init__(self, tamanho, preco):
    self.tamanho = tamanho
    self.preco = preco

  def checaCupom(self, cupom):
    if not cupom.isdigit():
      print("Insira um cupom válido")
      exit()
    else:
      cupom = int(cupom)
      return cupom

  def darTroco(self, cupom):
    troco = cupom - self.preco
    return troco

  def vender(self, cupom):
    cupom = self.checaCupom(cupom)
    if cupom >= self.preco:
      print("Você pode pagar pelo café", self.tamanho)
      if cupom == self.preco:
        print("Compra concluida")
        cupom = 0
      else:
        cupom = self.darTroco(cupom)
        print("Seu troco é", cupom)
    return str(cupom)

cafe0 = Cafe("menorzin", 1)
cafe1 = Cafe("pequeno", 2)
cafe2 = Cafe("médio", 5)
cafe3 = Cafe("grande", 6)
cafe4 = Cafe("extra grande", 8)

print("Digite o valor do seu cupom")
cupom = input()

for i in [cafe4, cafe3, cafe2, cafe1, cafe0]:
  cupom = i.vender(cupom)

