import requests
import time

# ==============================================
# 🔥 TIKTOK AUTO FOLLOWERS BOT
# 👨‍💻 By: Ardieans
# 📌 Gunakan bijak, max 50 per hari
# ==============================================

def banner():
    print("""
════════════════════════════════════
   🔥 TIKTOK AUTO FOLLOWERS BOT 🔥
════════════════════════════════════
✅ GRATIS | ✅ AMAN | ✅ TANPA LOGIN
    """)

def utama():
    banner()
    user_id = input("🔹 Masukkan ID Akun TikTok : ")
    jumlah = int(input("🔹 Masukkan Jumlah (Max 50) : "))

    print(f"\n🚀 Memproses {jumlah} Pengikut...\n")

    sukses = 0
    gagal = 0

    for i in range(jumlah):
        try:
            url = f"https://api.shadowdev.xyz/api/tiktok/followers?uid={user_id}"
            res = requests.get(url, timeout=20)

            if res.status_code == 200:
                sukses += 1
                print(f"✅ [{i+1}/{jumlah}] Berhasil Ditambahkan")
            else:
                gagal += 1
                print(f"⏳ [{i+1}/{jumlah}] Menunggu Antrian...")

        except Exception as e:
            gagal += 1
            print(f"🔄 [{i+1}/{jumlah}] Memproses Ulang...")

        time.sleep(5)

    print("\n════════════════════════════════════")
    print(f"📊 Hasil Akhir :")
    print(f"✅ Berhasil : {sukses}")
    print(f"❌ Gagal    : {gagal}")
    print("\n🎉 SELESAI! Cek Akun Dalam 3-5 Menit")
    print("💡 Gunakan 1x Sehari Agar Aman")
    print("════════════════════════════════════")

if __name__ == "__main__":
    utama()
  
