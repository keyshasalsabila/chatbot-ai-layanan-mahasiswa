# Data pertanyaan dan jawaban (kamus)
data = {
    "Kapan jadwal kuliah": "Jadwal kuliah dapat dilihat di portal akademik.",
    "Bagaimana cara bayar ukt": "Pembayaran UKT melalui bank yang ditentukan kampus.",
    "Kapan pengisian KRS dilakukan": "Dilakukan setiap awal semester sesuai kalender akademik.",
    "Apakah kampus menyediakan beasiswa": "Ya, kampus menyediakan berbagai jenis beasiswa berdasarkan prestasi dan ekonomi.",
    "Dimana saya bisa lihat nilai akhir": "Nilai dapat dilihat melalui portal akademik mahasiswa.",
    "Bagaimana cara cetak KRS": "Cetak KRS bisa melalui SIAKAD setelah KRS disetujui dosen wali.",
    "Bagaimana cara mengajukan cuti kuliah": "Pengajuan cuti kuliah dilakukan dengan mengisi formulir cuti dan menyerahkannya ke bagian akademik."
}

print("Chatbot Layanan Informasi Mahasiswa")
print("Ketik 'exit' untuk keluar")

data = {k.lower(): v for k, v in data.items()}

while True:
    user = input("Anda: ").lower()

    if user == "exit":
        print("Terima kasih telah menggunakan chatbot!")
        break

    if user in data:
        print("Bot:", data[user])
    else:
        print("Bot: Maaf, saya belum paham pertanyaan Anda.")
