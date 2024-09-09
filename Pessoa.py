class Pessoa:
  def __init__(self, nome, dataNascimento, cpf, rg, status):
    self.__nome = nome  
    self.__dataNascimento = dataNascimento  
    self.__cpf = cpf  
    self.__rg = rg  
    self.__status = status  

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def dataNascimento(self):
    return self.__dataNascimento

  @dataNascimento.setter
  def dataNascimento(self, dataNascimento):
    self.__dataNascimento = dataNascimento

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf):
    self.__cpf = cpf

  @property
  def rg(self):
    return self.__rg

  @rg.setter
  def rg(self, rg):
    self.__rg = rg

  @property
  def status(self):
    return self.__status

  @status.setter
  def status(self, status):
    self.__status = status