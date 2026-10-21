class TresEnRaya:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self._turno_actual = 'X'

    def siguiente_turno(self) -> str:
        return self._turno_actual

    def jugar(self, x: int, y: int) -> str:
        if not (1 <= x <= 3) or not (1 <= y <= 3):
            raise ValueError(f"Coordenadas fuera de rango: ({x}, {y})")

        fila = x - 1
        columna = y - 1

        if self.tablero[fila][columna] != ' ':
            raise ValueError(f"Casilla ({x}, {y}) ya ocupada")

        jugador_que_jugo = self._turno_actual
        self.tablero[fila][columna] = jugador_que_jugo

        self._turno_actual = '+' if self._turno_actual == 'X' else 'X'

        if self._hay_ganador(jugador_que_jugo):
            return f"{jugador_que_jugo} es el ganador"

        return "No hay ganador"

    def _hay_ganador(self, j: str) -> bool:
        for i in range(3):
            if all(self.tablero[i][c] == j for c in range(3)):
                return True
            if all(self.tablero[f][i] == j for f in range(3)):
                return True

        if all(self.tablero[i][i] == j for i in range(3)):
            return True
        if all(self.tablero[i][2 - i] == j for i in range(3)):
            return True

        return False

    def __str__(self):
        return str(self.tablero)