class Calculadora:
  def __init__(self):
    self._valorA = 0
    self._valorB = 0
    self._operacao = ''

  @property
  def valorA(self):
    return self._valorA

  @valorA.setter
  def valorA(self, valor):
    self._valorA = valor

  @property
  def valorB(self):
    return self._valorB

  @valorB.setter
  def valorB(self, valor):
    self._valorB = valor

  @property
  def operacao(self):
    return self._operacao

  @operacao.setter
  def operacao(self, operacao):
    self._operacao = operacao

  def validarOperacao(self, simbolo):
    if simbolo in ['+', '-', '*', '/']:
      return True
    else:
      return False

  def calcular(self):
    if not self.validarOperacao(self._operacao):
      print("Operação inválida!")
      return 

    if self._operacao == "+":
        return self._valorA + self._valorB
    elif self._operacao == "-":
        return self._valorA - self._valorB
    elif self._operacao == "*":
        return self._valorA * self._valorB
    elif self._operacao == "/":
        if self._valorA == 0 or self._valorB == 0:
          print("Não é possível dividir por zero!")
          return
        else:
          return self._valorA / self._valorB
          
  def mostrarResultado(self):
    print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))