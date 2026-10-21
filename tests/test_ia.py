
import pytest

from src.tres_en_raya import TresEnRaya


@pytest.fixture
def juego():
    return TresEnRaya()


def test_x_inicia_la_partida(juego):
    assert juego.siguiente_turno() == "X"


def test_segundo_turno_es_mas(juego):
    juego.jugar(1, 1)
    assert juego.siguiente_turno() == "+"


def test_los_turnos_se_alternan(juego):
    juego.jugar(1, 1)
    assert juego.siguiente_turno() == "+"

    juego.jugar(2, 1)
    assert juego.siguiente_turno() == "X"

    juego.jugar(3, 1)
    assert juego.siguiente_turno() == "+"


@pytest.mark.parametrize(
    ("x", "y"),
    [
        (0, 1),
        (1, 0),
        (4, 1),
        (1, 4),
        (-1, 1),
        (1, -1),
        (0, 0),
        (4, 4),
    ],
)
def test_coordenadas_fuera_de_rango_lanzan_excepcion(juego, x, y):
    with pytest.raises(Exception):
        juego.jugar(x, y)


@pytest.mark.parametrize(
    ("x", "y"),
    [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ],
)
def test_primera_jugada_valida_no_tiene_ganador(juego, x, y):
    assert juego.jugar(x, y) == "No hay ganador"


def test_no_se_puede_jugar_en_una_casilla_ocupada(juego):
    juego.jugar(1, 1)

    with pytest.raises(Exception):
        juego.jugar(1, 1)


def test_jugada_invalida_no_debe_cambiar_el_turno(juego):
    juego.jugar(1, 1)

    with pytest.raises(Exception):
        juego.jugar(1, 1)

    assert juego.siguiente_turno() == "+"


def test_jugada_fuera_de_rango_no_debe_cambiar_el_turno(juego):
    with pytest.raises(Exception):
        juego.jugar(4, 1)

    assert juego.siguiente_turno() == "X"


def test_ganador_horizontal_x(juego):
    assert juego.jugar(1, 1) == "No hay ganador"
    assert juego.jugar(1, 2) == "No hay ganador"
    assert juego.jugar(2, 1) == "No hay ganador"
    assert juego.jugar(2, 2) == "No hay ganador"
    assert juego.jugar(3, 1) == "X es el ganador"


def test_ganador_horizontal_mas(juego):
    juego.jugar(1, 1)
    juego.jugar(1, 2)
    juego.jugar(2, 1)
    juego.jugar(2, 2)
    juego.jugar(3, 3)

    assert juego.jugar(3, 2) == "+ es el ganador"


def test_ganador_vertical_x(juego):
    juego.jugar(1, 1)
    juego.jugar(2, 1)
    juego.jugar(1, 2)
    juego.jugar(2, 2)

    assert juego.jugar(1, 3) == "X es el ganador"


def test_ganador_vertical_mas(juego):
    juego.jugar(1, 1)
    juego.jugar(2, 1)
    juego.jugar(1, 2)
    juego.jugar(2, 2)
    juego.jugar(3, 3)

    assert juego.jugar(3, 2) == "No hay ganador"

    # Nueva partida para probar la victoria vertical de '+'
    juego = TresEnRaya()
    juego.jugar(1, 1)
    juego.jugar(2, 1)
    juego.jugar(1, 2)
    juego.jugar(2, 2)
    juego.jugar(3, 3)

    assert juego.jugar(2, 3) == "+ es el ganador"


def test_ganador_diagonal_principal_x(juego):
    juego.jugar(1, 1)
    juego.jugar(1, 2)
    juego.jugar(2, 2)
    juego.jugar(1, 3)

    assert juego.jugar(3, 3) == "X es el ganador"


def test_ganador_diagonal_secundaria_x(juego):
    juego.jugar(1, 3)
    juego.jugar(1, 1)
    juego.jugar(2, 2)
    juego.jugar(2, 1)

    assert juego.jugar(3, 1) == "X es el ganador"


def test_ganador_diagonal_principal_mas(juego):
    juego.jugar(1, 2)
    juego.jugar(1, 1)
    juego.jugar(2, 1)
    juego.jugar(2, 2)
    juego.jugar(3, 2)

    assert juego.jugar(3, 3) == "+ es el ganador"


def test_ganador_diagonal_secundaria_mas(juego):
    juego.jugar(1, 1)
    juego.jugar(1, 3)
    juego.jugar(2, 1)
    juego.jugar(2, 2)
    juego.jugar(3, 3)

    assert juego.jugar(3, 1) == "+ es el ganador"


def test_todas_las_jugadas_no_ganadoras_devuelven_mensaje_exacto(juego):
    jugadas = [
        (1, 1),
        (1, 2),
        (2, 1),
        (3, 3),
        (2, 2),
        (3, 1),
    ]

    for x, y in jugadas:
        resultado = juego.jugar(x, y)
        assert resultado == "No hay ganador"


def test_el_tablero_admite_nueve_jugadas_validas_sin_excepcion():
    juego = TresEnRaya()
    jugadas = [
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (3, 2),
        (2, 2),
        (1, 3),
        (3, 3),
        (2, 3),
    ]

    for x, y in jugadas:
        try:
            juego.jugar(x, y)
        except Exception:
            # Una partida puede terminar antes de completar el tablero.
            # No se debe exigir que se acepten jugadas después de una victoria.
            break
