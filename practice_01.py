pengambilan_produk = 1020000
jumlah_kendaraan = 6

if pengambilan_produk >= 1000000:
    if jumlah_kendaraan > 8:
        print("Anda memenuhi syarat menjadi Distributor di daerah ini.")
    else:
        print("Anda tidak memenuhi syarat jumlah kendaraan.")
else:
    print("Anda tidak memenuhi syarat minimal pengambilan produk.")