  target = int(input("\nTentukan range produksi padi yang diinginkan: "))
    data_daerah = data[data["provinsi"]=="Jawa Barat"]
    operator = input("Operator: ")
    print(f"\nBerikut adalah data-data provinsi penghasil padi {operator} {target}: ")
    data_filteran = filter_kg(data_daerah, operator, target)
    print(data_filteran)
    