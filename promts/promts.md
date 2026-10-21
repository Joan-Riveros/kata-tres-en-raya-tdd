 **Prompt a utilizar:**
 "Actúa como un desarrollador experto en QA y TDD. Escribe una suite completa de pruebas unitarias en Python usando `pytest` para la kata del Tres en Raya (Tic-Tac-Toe), cumpliendo estrictamente con este contrato e interfaz:
 1. **Contrato de la clase:**
 * La clase se importa como `from src.tres_en_raya import TresEnRaya`.
 * El tablero es de 3x3, pero las coordenadas son 1-indexed (valores válidos del 1 al 3 para X y para Y).
 * Si se intenta jugar con coordenadas fuera de rango (ej. x > 3 o y > 3), el método `jugar(x, y)` debe lanzar una excepción.
 * Si se intenta jugar en una casilla ya ocupada, `jugar(x, y)` debe lanzar una excepción.
 
 
 2. **Reglas de turnos:**
 * El jugador `'X'` siempre inicia la partida.
 * El segundo jugador es `'+'` (utiliza el signo más en vez del círculo 'O').
 * El método `siguiente_turno()` debe devolver el símbolo del turno actual (`'X'` o `'+'`).
 
 
 3. **Condiciones de victoria y retornos:**
 * Cada jugada no ganadora a través de `jugar(x, y)` debe retornar exactamente el string: `"No hay ganador"`.
 * Cuando un jugador completa una línea (horizontal, vertical o diagonal), `jugar(x, y)` debe retornar: `"<jugador> es el ganador"` (ejemplo: `"X es el ganador"` o `"+ es el ganador"`).
 
 
 
 
 Proporciona únicamente el código listo para guardar en `tests/test_ia.py` con cobertura completa de todos los casos."

