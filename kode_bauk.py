"""
Modul untuk pengujian fungsi matematika sederhana.
"""


def calculate_sum(val_a, val_b):
    """
    Menghitung jumlah dua angka dan mengembalikan hasilnya.
    """
    total = val_a + val_b
    return total


if __name__ == "__main__":
    RESULT = calculate_sum(10, 20)
    print(f"Hasil penjumlahan: {RESULT}")
