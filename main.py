import pandas as pd

from script.data_loader import baca_data
from script.data_analysis import hitung_total_produksi, filter_tahun
from script.data_exporter import simpan_laporan

def main():
    print("=== ANALISIS PRODUKSI PADI ===")
    data = baca_data()
    hasil_panen = hitung_total_produksi(data)

    print("Berikut adalah data-data produksi padi beberapa tahun terakhir:")
    print(data)

    print("\nBerikut adalah total produksi panen pada setiap provinsi:")
    print(hasil_panen)

    simpan_laporan(hasil_panen)

    pertanyaan = input("\nApakah tertarik untuk melihat data pada tahun tertentu? ")
    if pertanyaan == "ya":
        tahun = int(input("Tahun berapa? "))
        filter_data_tahun = filter_tahun(data, tahun)
        print(hitung_total_produksi(filter_data_tahun))
    elif pertanyaan == "tidak":
        print("Semoga harimu menyenangkan!")
    else:
        print("Saya tidak paham, coba ulang.")

if __name__ == "__main__":
    main()