import pytest
from src.tres_en_raya import TresEnRaya


@pytest.fixture
def juego():
    return TresEnRaya()



def test_cuando_fuera_x_lanzar_excepcion(juego):
    with pytest.raises(Exception):
        juego.jugar(5, 2)


def test_cuando_fuera_y_lanzar_excepcion(juego):
    with pytest.raises(Exception):
        juego.jugar(2, 5)


def test_cuando_lugar_ocupado_lanzar_excepcion(juego):
    juego.jugar(1, 3)
    with pytest.raises(Exception):
        juego.jugar(1, 3)


def test_si_primer_turno_entonces_juega_x(juego):
    assert juego.siguiente_turno() == 'X'


def test_si_primer_turno_x_siguiente_mas(juego):
    juego.jugar(2, 1)  
    assert juego.siguiente_turno() == '+'
    juego.jugar(2, 2)  
    assert juego.siguiente_turno() == 'X'



def test_cuando_no_hay_ganador(juego):
    resultado = juego.jugar(2, 1)
    assert resultado == "No hay ganador"


def test_si_llena_columna_entonces_gana(juego):
    juego.jugar(1, 1)  
    juego.jugar(1, 2)  
    juego.jugar(2, 1)  
    juego.jugar(2, 2)  
    resultado = juego.jugar(3, 1)  
    assert resultado == "X es el ganador"


def test_si_llena_fila_entonces_gana(juego):
    juego.jugar(2, 1)  
    juego.jugar(1, 1)  
    juego.jugar(3, 1)  
    juego.jugar(1, 2)  
    juego.jugar(2, 2)  
    resultado = juego.jugar(1, 3)  
    assert resultado == "+ es el ganador"


def test_si_llena_diagonal_entonces_gana(juego):
    juego.jugar(1, 1)  
    juego.jugar(1, 2)  
    juego.jugar(2, 2)  
    juego.jugar(1, 3)  
    resultado = juego.jugar(3, 3)  
    assert resultado == "X es el ganador"


def test_si_llena_diagonal_opuesta_entonces_gana(juego):
    juego.jugar(1, 2)  
    juego.jugar(1, 3)  
    juego.jugar(1, 1)  
    juego.jugar(2, 2)  
    juego.jugar(2, 3)  
    resultado = juego.jugar(3, 1)
    assert resultado == "+ es el ganador"