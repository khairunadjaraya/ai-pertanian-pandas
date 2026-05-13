import pandas as pd

def hitung_total_produksi(data):
    """Menghitung total produksi tiap provinsi"""
    hasil_panen = data.groupby("provinsi")["produksi_kg"].sum().reset_index()
    return hasil_panen

def filter_tahun(data, tahun):
    filter_data_tahun = data[data["tahun"] == tahun]
    return filter_data_tahun

def filter_kg(data, operator, target):
    """Memfilter data berdasarkan jumlah produksi"""

    if operator == ">=":
        hasil = data[data["produksi_kg"] >= target]

    elif operator == "<=":
        hasil = data[data["produksi_kg"] <= target]

    elif operator == ">":
        hasil = data[data["produksi_kg"] > target]

    elif operator == "<":
        hasil = data[data["produksi_kg"] < target]

    elif operator == "==":
        hasil = data[data["produksi_kg"] == target]

    else:
        print("Operator tidak valid")
        return None

    return hasil