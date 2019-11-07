from sudoku_game import Sudoku


class interfaz():

    def validar(self, fila, columna, numero):
        try:
            if int(fila) >= 0 and int(fila) < 9:
                if int(columna) >= 0 and int(columna) < 9:
                    if numero != "x":
                        if int(numero) > 0 and int(columna) < 9:
                            return True
        except:
            return False

    def __init__(self):
        self.table = [["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                      ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                      ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                      ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                      ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                      ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                      ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                      ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                      ["x", "x", "x", "x", "8", "x", "x", "7", "9"]]
        self.game = Sudoku(self.table)

    def PrintTable(self):
        table = ""
        for fila in self.table:
            for elemento in fila:
                table += elemento + " "
            table += "\n"
        return table

    def jugar(self):
        print(self.PrintTable())
        while not self.game.gano():
            self.n = input("ingrese un numero ")
            self.i = input("ingrese la fila ")
            self.j = input("ingrese la columna ")

            if self.validar(self.i, self.j, self.n):
                self.i = int(self.i)
                self.j = int(self.j)
                if self.game.validar(self.i, self.j, self.n) and self.game.checkeo_zona(self.i, self.j, self.n):
                    if not (self.i, self.j) in self.game.tablero_original:
                        self.game.intercambio_numero(self.i, self.j, self.n)

            print(self.PrintTable())


#x = interfaz()

#x.jugar()
