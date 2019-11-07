import math

class Sudoku():

    def __init__(self, lista):
        self.table = lista

        self.tablero_original = []
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                if (self.table[i][j] != "x"):
                    self.tablero_original.append((i, j))

    def validar(self, fila, columna, numero):
        #verifica si se repite algun numero en alguna fila o columna
        
            for elemento in range(9):
                if self.table[fila][elemento] == numero:
                    return False
                if self.table[elemento][columna] == numero:
                        return False
            return True
        
        #verifica si se repite algun numero en alguna zona

    def checkeo_zona(self, fila, columna, valor):
        fila = (fila // 3) * 3
        columna = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if (self.table[int(fila + i)][int(columna + j)] == str(valor)):
                    return False
        return True

    
    def intercambio_numero(self,fila,columna,valor):

        if self.checkeo_zona(fila,columna,valor) and self.validar(fila,columna,valor):
            self.table [fila][columna] = valor
            return True
        else:
            return False

    def gano(self):
        for fila in self.table:
            if "x" in fila:
                return False
            else:
                return True

    


    


