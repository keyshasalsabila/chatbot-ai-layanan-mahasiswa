# Data pertanyaan dan jawaban (kamus)
data = {
    "kapan jadwal kuliah": "Jadwal kuliah dapat dilihat di portal akademik.",
    "bagaimana cara bayar ukt": "Pembayaran UKT melalui bank yang ditentukan kampus.",
    "kapan pengisian KRS dilakukan": "Dilakukan setiap awal semester sesuai kalender akademik.",
    "apakah kampus menyediakan beasiswa": "Ya, kampus menyediakan berbagai jenis beasiswa berdasarkan prestasi dan ekonomi.",
    "dimana saya bisa lihat nilai akhir": "Nilai dapat dilihat melalui portal akademik mahasiswa."
}

print("Chatbot Layanan Informasi Mahasiswa")
print("Ketik 'exit' untuk keluar")

while True:
    user = input("Anda: ").lower()

    if user == "exit":
        print("Terima kasih telah menggunakan chatbot!")
        break

    if user in data:
        print("Bot:", data[user])
    else:
        print("Bot: Maaf, saya belum paham pertanyaan Anda.")
