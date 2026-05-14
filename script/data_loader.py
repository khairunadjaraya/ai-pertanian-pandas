import pandas as pd

def raw_data(data):
    """Membaca data"""
    hasil = pd.read_csv(f"data/{data}.csv")
    return hasil

def cleaning_data (data):

    for kolom in data.columns:
        total_null = data[kolom].isnull().sum()
        if total_null > 0:
            if pd.api.types.is_numeric_dtype(data[kolom]):
                data[kolom] = data[kolom].fillna(data[kolom].mean())
    return data

def merge_data (data1, data2):
    hasil = pd.merge(data1, data2, on="kabupaten", how=left)
    return hasil

def show_data():
    data_kotor = raw_data("produksi_padi_fiktif")
    tanah_kotor = raw_data("sensor_tanah")
    tanah = cleaning_data(tanah_kotor)
    data_padi = cleaning_data(data_kotor)

    data = pd.merge(data_padi, tanah, on="kabupaten", how="left")
    return data
    
def sort_data (data, target):
    hasil = data.sort_values(by = target, ascending = False)
    return hasil



