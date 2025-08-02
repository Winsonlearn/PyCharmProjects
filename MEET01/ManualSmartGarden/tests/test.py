import math

from triangle_formula import type_of_triangle
from root_formula import calculate_root, calculate_divide
import pytest

def test_segitiga_sama_sisi():
    assert type_of_triangle(5, 5, 5) == "segitiga sama sisi"
    assert type_of_triangle(10, 10, 10) == "segitiga sama sisi"

def test_segitiga_sama_kaki():
    assert type_of_triangle(5, 5, 3) == "segitiga sama kaki"
    assert type_of_triangle(3, 5, 5) == "segitiga sama kaki"
    assert type_of_triangle(5, 3, 5) == "segitiga sama kaki"

def test_segitiga_sembarang():
    assert type_of_triangle(3, 4, 5) == "segitiga sembarang"
    assert type_of_triangle(10, 12, 14) == "segitiga sembarang"

def test_bukan_segitiga():
    assert type_of_triangle(1, 2, 4) == "bukan segitiga"

def test_pembagian():
    assert calculate_divide(1, 1) == 1

def test_akar_kuadrat():
    assert calculate_root(4) == 2

def test_akar_kuadrat_input_negatif():
    with pytest.raises(ValueError):
        calculate_root(-1)