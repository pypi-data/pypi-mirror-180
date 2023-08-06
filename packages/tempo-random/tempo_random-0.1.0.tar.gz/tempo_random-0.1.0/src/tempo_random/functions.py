# -*- coding: utf-8 -*-
"""
Functons for typer CLI.
"""
import secrets
from enum import Enum


class Tempo(list, Enum):
    """
    Basic tempos.
    """

    # Changed to title instead of all caps. Will test.
    Andante = [73, 77]
    Moderato = [86, 97]
    Allegretto = [98, 109]
    Allegro = [110, 132]


class TempoList(Enum):
    """
    List of tempos represented in string format.
    """

    ANDANTE = "Andante"
    MODERATO = "Moderato"
    ALLEGRETTO = "Allegretto"
    ALLEGRO = "Allegro"


def tempo_generate(first: int = 50, second: int = 100) -> int:
    """
    Simple random number function.
    """

    random_tempo = [_ for _ in range(first, second)]
    return secrets.choice(random_tempo)
