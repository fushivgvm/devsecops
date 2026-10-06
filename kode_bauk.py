"""
Modul perhitungan sederhana.
"""


def calculate_sum(val_a, val_b):
    """
    Menhitung jumlah dua angka.
    """
    total = val_a + val_b
    return total


if __name__ == "__main__":
    RESULT = calculate_sum(10, 20)
    print(f"Hasil: {RESULT}")
    
