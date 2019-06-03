class Pessoa:
    olhos = 2
  def __init__(self, *filhos, nome=None, idade=35):
      self.idade = idade
      self.nome = nome
      self.filhos = list(filhos)
  def cumprimentar(self):
      return f'ola{id(self)}'

  @staticmethod
  def metodo_estatico():
      return 42

  @classmethod
  def nome_e_atributos_de_classe(cls):
      return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    rafael = Homem(nome='Rafael')
    luciano = Homem(rafael, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'alves'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(rafael.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(rafael.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(rafael.olhos))
    print(Pessoa.metodo_estatico(), luciano.metado_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.metodo_estatico())
    pessoa=Pessoa('anonimo')
    print(isis)
