#MIGUEL ARTHUR – 211062320
#MINIPROJETO 1 - PSEUDOCÓDIGO

classe FormaGeometrica: 

    funcao iniciar (nome, cor): 
        nome = nome 
        cor = cor

Classe retangulo (herda FormaGeométrica):

    Funcao iniciar(nome, cor, base altura):
        Chame o construtor da classe pai com nome e cor
        Base = base
        Altura = altura
    Funcao calcular_area(self)
        Retorne base vezes altura
    Funcao calcular_perimetro(self)
        Retorne 2 vezes base mais 2 vezes altura
Classse trinagulo (herda FormaGeométrica):
    Funcao iniciar(self, nome, cor, base, altura, lado):
        chame o construtor da classe pai com o nome e cor
        base = base
        altura = altura
        lado = lado
    Funcao calcular_area(self)
        retorne base vezes altura dividido por 2
    Funcao calcular_perimetro(self)
        retorne base mais altura mais lado
Classe circulo (herda FormaGeometrica):
    Funcao iniciar(self, nome, cor, raio):
        chame o construtor da classe pai com nome e cor
        Raio= raio 
    Funcao calcular_area(self)
        Retorne 3.14 vezes o raio elevado a 2
    Funcao calcular_perimetro(self)
        Retorne 2 vezes 3.14 vezes o raio
Formas = []

Enquanto verdadeiro:
Imprimir "1- retangulo"
Imprimir "2 - quadrado"
Imprimir "3- circulo"
Imprimir "0 - sair"
Ler opcao como inteiro
Se opção for igual a 1:
Ler base
Ler altura
Forma = retangulo("retangulo”, “amarelo”, base, altura)
Adicionar forma a lista formas
Imprimir "area" + forma de calcular_area() +, "perimetro:" + forma de
Calcular_perimetro()
Senão, se opção fopr igual a 2:
Ler lado
    Forma = quadrado("quadrado", "vermelho",lado)
    Adicionar forma a lista formas
    Imprimir "area:" +forma de calcular_area() + "perimetro"+ forma de 
calcular_perimetro()
Senão, se opção fopr igual a 3:
Ler raio
    Forma = circulo("circulo", "azul",raio)
    Adicionar forma a lista formas
    Imprimir "area:" +forma de calcular_area() + "perimetro"+ forma de 
calcular_perimetro()
Se não, se opcao for igual a 0:
interromper o laço
Se não:
imprimir "opção Invalida"
