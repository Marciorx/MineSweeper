# from random import randint

# COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
# JOGADA_SEGURA = "Jogada Segura"
# GAME_OVER = "Game Over"

# class CampoMinado:

#     def criar_novo_jogo(self, linha, coluna):
#         """ Inicializando campo minado com linha X coluna posicoes """
#         self.__linha = int(linha)
#         self.__coluna = int(coluna)
#         self.jogadas_restantes = self.__calcular_total_jogadas(linha, coluna)
#         self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
#         self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)

#     def jogada(self, linha, coluna):
#         """ 1. Verifica se as coordenadas são válidas
#             2. Validar se acertei uma mina: 
#                 caso sim:
#                     Game Over 
#                 caso não: 
#                     marcar a posição escolhida no tabuleiro com a quantidade de 
#                     bombas existentes nos nós vizinhos """
#         linha = int(linha)
#         coluna = int(coluna)

#         if not self.__validar_coordenadas(linha, coluna):
#             return COORDENADAS_INVALIDAS
        
#         if  (linha, coluna) in self.__coordenadas_bombas:
#             return GAME_OVER
        
#         self.__tabuleiro[linha][coluna] = str(self.__conta_bombas_vizinhos(linha, coluna))
#         self.jogadas_restantes -=1
#         return JOGADA_SEGURA

#     def imprimir_tabuleiro(self):
#         for posicao in self.__tabuleiro:
#             print(str(posicao))
    
#     def jogo_incompleto(self):
#         return False

#     def __inicializar_tabuleiro(self, linha, coluna):
#         return [[str('X') for x in range(coluna)] for j in range(linha)]

#     def __distribuir_bombas(self, linha, coluna):
#         """ Consulta o total de bombas permitidas e aleatoriamente definie as coordenadas de cada bomba"""
#         coordenadas_bombas = [(randint(0, linha - 1), randint(0, coluna - 1)) for x in range(self.__total_bombas())]
#         print(coordenadas_bombas)
#         return coordenadas_bombas

#     def __total_bombas(self):
#         return int((self.__linha*self.__coluna)/3)
    
#     def __calcular_total_jogadas(self,linha, coluna):
#         return (linha*coluna) - self.__total_bombas()

#     def __validar_coordenadas(self, linha, coluna):
#         if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
#             return True
#         return False
    
#     def __coordenada_e_bomba(self, coordenada):
#         """ Verifica se a coodenada informada possui uma bomba """
#         return coordenada in self.__coordenadas_bombas

#     def __conta_bombas_vizinhos(self, linha, coluna):
#         """ Soma -1,0 e 1 em linha e coluna e verifica se elas possuem uma bomba, caso sim, essa coordenada entra em uma lista """
#         return len([(linha + x, coluna + y) for x in (-1,0,1) for y in (-1,0,1) if self.__coordenada_e_bomba((linha + x, coluna + y))])

from random import randint

COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
JOGADA_SEGURA = "Jogada Segura"
GAME_OVER = "Game Over"
VITORIA = "Parabéns você venceu"


class CampoMinado:

    def criar_novo_jogo(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = linha
        self.__coluna = coluna
        self.__matriz = self.__inicializar_matriz(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas()
        self.jogadas_restantes = self.__calcular_total_jogadas()

    def jogada(self, linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina:
                caso sim:
                    Game Over
                caso não:
                    marcar a posição escolhida no matriz com a quantidade de
                    bombas existentes nos nós vizinhos """

        if not self.__validar_coordenadas(linha, coluna):
            return COORDENADAS_INVALIDAS

        if self.__procurar_bomba(linha, coluna):
            return GAME_OVER

        self.__marcar_posicao_jogada(linha, coluna, self.__contar_bombas_adjacentes(linha, coluna))
        # self.imprimir_matriz()
        self.jogadas_restantes -=1

        if self.jogadas_restantes == 0:
            return VITORIA
        else:
            return JOGADA_SEGURA

    def retornar_matriz(self):
        return self.__matriz

    def imprimir_matriz(self):
        for posicao in self.__matriz:
            print(str(posicao))

    def jogadas_restantes(self):
        return self.jogadas_restantes

    def __inicializar_matriz(self, linha, coluna):
        # return [[str(x) + "," + str(j) for x in range(coluna)] for j in range(linha)]
        return [["X" for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self):
        quantidade_bombas = self.__total_bombas()
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, self.__linha - 1), randint(0, self.__coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                print("("+str(coordenada[0]+1)+","+ str(coordenada[1]+1)+")")
                quantidade_bombas -= 1
        return coordenadas_bombas

    def __total_bombas(self):
        return int((self.__linha * self.__coluna) / 3)

    def __validar_coordenadas(self, linha, coluna):
        if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
            return True
        return False

    def __procurar_bomba(self, linha, coluna):
        return (linha, coluna) in self.__coordenadas_bombas

    def __contar_bombas_adjacentes(self, linha, coluna):
        linha_adjacente = linha - 1
        total_bombas = 0
        while linha_adjacente <= linha + 1:
            coluna_adjacente = coluna - 1
            while coluna_adjacente <= coluna + 1:
                if self.__procurar_bomba(linha_adjacente, coluna_adjacente):
                    total_bombas += 1
                coluna_adjacente += 1
            linha_adjacente += 1
        return total_bombas

    def __marcar_posicao_jogada(self, linha, coluna, quantidade_bombas):
        self.__matriz[linha][coluna] = str(quantidade_bombas)

    def __calcular_total_jogadas(self):
        return (self.__linha * self.__coluna) - self.__total_bombas()