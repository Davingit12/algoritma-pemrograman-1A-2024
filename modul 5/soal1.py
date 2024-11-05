def calculate_discount(total_belanja, keanggotaan):
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    else:
        diskon = 0.0  
    if total_belanja > 1000000:
        diskon += 0.05
    
    total_diskon = total_belanja * diskon
    harga_setelah_diskon = total_belanja - total_diskon
    
    return harga_setelah_diskon

total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")
harga_akhir = calculate_discount(total_belanja, keanggotaan)
print("Total yang harus dibayar setelah diskon:", harga_akhir)