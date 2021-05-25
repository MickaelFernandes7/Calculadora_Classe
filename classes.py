class Calculadora :
    def __init__(self):
        self.numeros = []
        self.operacao = int(input('Qual operação matemática deseja realizar? | 1 - Soma, 2 - Subtração, 3-Divisão, 4 - Multiplicação, 5 - Raiz, 6 - Potência    '))

          
    def insere_numeros(self):
        for x in range(0,2):
            self.numeros.append(int(input('Digite os números que deseja calcular : ')))
      
            def soma(self):
                print('Soma :', self.numeros[0] + self.numeros[1], '\n')
            
            def subtracao(self):
                print('Subtração : ', self.numeros[0] - self.numeros[1], '\n')
            
            def divisao(self):
                print('Divisão : ', self.numeros[0] / self.numeros[1] , '\n')

            def multiplicacao(self):
                print('Multiplicação : ', self.numeros[0] * self.numeros[1], '\n')
            
            def raiz(self):
                print('Raiz Quadrada : ', self.numeros[0] ** 0.5)
                print('Raiz Quadrada : ', self.numeros[1] ** 0.5, '\n')
                
            def potencia(self):
                print('Potencia :', self.numeros[0] ** self.numeros[1], '\n')

        if self.operacao == 1:
            soma(self)
        elif self.operacao == 2:
            subtracao(self)
        elif self.operacao == 3:
            divisao(self)
        elif self.operacao == 4:
            multiplicacao(self)
        elif self.operacao == 5:
            raiz(self)
        elif self.operacao == 6:
            potencia(self)

    
    
        
        
