#Miguel Arthur 
#211062320

class FormaGeometrica:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Retangulo(FormaGeometrica):
    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FormaGeometrica):
    def __init__(self, nome, cor, base, altura, lado):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.lado

class Circulo(FormaGeometrica):
    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

formas = []

while True:
    print("1 - Retangulo")
    print("2 - Triangulo")
    print("3 - Circulo")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        forma = Retangulo("Retângulo", "Amarelo", base, altura)
        formas.append(forma)
        print("Área:", forma.calcular_area(), ", Perímetro:", forma.calcular_perimetro())
    elif opcao == 2:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        lado = float(input("Digite o lado: "))
        forma = Triangulo("Triângulo", "Vermelho", base, altura, lado)
        formas.append(forma)
        print("Área:", forma.calcular_area(), ", Perímetro:", forma.calcular_perimetro())
    elif opcao == 3:
        raio = float(input("Digite o raio: "))
        forma = Circulo("Círculo", "Azul", raio)
        formas.append(forma)
        print("Área:", forma.calcular_area(), ", Perímetro:", forma.calcular_perimetro())
    elif opcao == 0:
        break
    else:
        print("Opção inválida")

