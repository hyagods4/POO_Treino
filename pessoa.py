class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, ano):
        if self.idade < 21:
            self.idade += ano
            self.altura += 0.5
        else:
            self.idade += ano
        print(f"{self.nome} envelheceu!")

    def engordar(self, kilos):
        self.peso += kilos
        print(f"{self.nome} engordou!")

    def emagrecer(self, kilos):
        self.peso -= kilos
        print(f"{self.nome} emagreceu!")

    '''def crescer(self, alt):
        self.altura += alt
        print(f"{self.nome} cresceu!")'''

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura/100:.2f}m")
        print(f"Peso: {self.peso:.2f}Kg")


def transform(numero, tipo):
    try:
        numero = tipo(numero)
        return True, numero
    except:
        return False, print("Erro! Não foi possivel converter em número.")


varEngloba = None   #Recebe dois dados, um numero e um valor Boleano. Confirma verdadeiramente se é um número nos valores de env, eng, emg, cres.

nome = input("Informe o nome da pessoa: ")
idade = int(input("Informe a idade da pessoa: "))
peso = float(input("Informe o peso(Kg) da pessoa: "))
altura = float(input("Informe a altura(cm) da pesso: "))

pessoa = Pessoa(nome, idade, peso, altura)

while True:
    print("\nStatus da pessoa:")
    pessoa.status()
    print()
    esc = input("""
env - Envelhecer
eng - Engordar
emg - Emagrecer
exit - Fechar programa
Opção: """)
    if esc.lower() == "exit":
        print("Thanks for using!")
        break
    elif esc.lower() == "env":
        varEngloba = input("Em quantos anos deseja envelhecer? ")
        varEngloba = transform(varEngloba, int)
        if varEngloba[0]:
            pessoa.envelhecer(varEngloba[1])

    elif esc.lower() == "eng":
        varEngloba = input("Em quantos quilos deseja engodar? ")
        varEngloba = tranform(varEngloba, float)
        if varEngloba[0]:
            pessoa.envenhecer(varEngloba[1])

    elif esc.lower() == "emg":
        varEngloba = input("Em quantos quilos deseja emagrecer? ")
        varEngloba = transform(varEngloba, float)
        if varEngloba[0]:
            pessoa.emagrecer(varEngloba[1])

    '''elif esc.lower() == "cres":
        varEngloba = input("Em quantos cm deseja crescer a pessoa? ")
        varEngloba = transform(varEngloba, float)
        if varEngloba[0]:
            pessoa.crescer(varEngloba[1])'''

print("INC. Developer: Hyago dos Santos Silva ( ͡° ͜ʖ ͡°)")
