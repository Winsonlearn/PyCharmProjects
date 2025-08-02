# triangle_formula.py

def type_of_triangle(a, b, c):
    """
    Menerima tiga sisi (a, b, c) dan mengembalikan jenis segitiga.
    """
    # Validasi input dasar (opsional, tapi praktik yang baik)
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Semua sisi harus berupa angka")
    if not all(x > 0 for x in [a, b, c]):
        raise ValueError("Sisi segitiga harus lebih besar dari nol")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "bukan segitiga"

    if a == b == c:
        return "segitiga sama sisi"
    elif a == b or b == c or a == c:
        return "segitiga sama kaki"
    else:
        return "segitiga sembarang"