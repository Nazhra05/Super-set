# DECISIONS: log keputusan untuk {{PROJECT_NAME}}

Dua seri. **C-xx** adalah keputusan workflow yang diwarisi dari plugin Content Project Workflow; isinya menjelaskan mengapa aturan di `CLAUDE.md`, `WORKFLOW.md`, dan agent berbentuk seperti sekarang. Ubah hanya dengan menulis keputusan project baru yang menggantikannya, beserta alasannya. **D-xx** adalah keputusan project ini sendiri, mulai dari D-01.

Format per entri: judul dengan status dan tanggal, lalu Alasan, Keputusan, Konsekuensi (file yang berubah).

## A. Keputusan workflow (diwarisi saat setup, {{SETUP_DATE}})
Setiap aturan menjawab kegagalan yang terlihat dalam pekerjaan konten nyata dengan Claude Code.

### C-01 Lihat dulu, baru tafsirkan
- **Alasan:** screenshot feedback ditindaklanjuti dengan tafsiran karangan. Dokumentasi Anthropic sendiri menyebut penalaran spasial Claude terbatas (posisi dan tata letak yang persis) dan menyarankan tafsiran gambar diverifikasi.
- **Keputusan:** untuk setiap gambar, tulis apa yang terlihat (`seen`) dan tafsirannya (`inferred`) secara terpisah, ulangi permintaan dalam satu kalimat, dan tanyakan kalau dua tafsiran menghasilkan pekerjaan berbeda. Posisi, ukuran, dan warna diukur (crop, zoom, sampel piksel, frame grab di time code), bukan diperkirakan.

### C-02 Selesai berarti dicek dan dilihat
- **Alasan:** "selesai" diklaim untuk scene yang belum dilihat siapa pun, dan cek tool yang lulus tidak mengatakan apa pun tentang tampilan frame.
- **Keputusan:** klaim butuh output perintah yang baru dijalankan dan frame yang sudah dilihat. Laporan agent adalah klaim. Yang belum dilakukan disebut terus terang: belum di-render, belum ditonton dengan suara, belum dicek di HP.

### C-03 Gate persetujuan
- **Alasan:** pekerjaan mahal (karakter, scene penuh) dimulai dari desain yang belum disetujui pemilik, lalu diulang.
- **Keputusan:** brief, style frames, character sheets, animatic, dan final butuh persetujuan pemilik dengan bukti ditunjukkan; script dan storyboard, serta shot, cukup dilaporkan. Gate hanya dilewati lewat keputusan project beserta alasannya.

### C-04 Setiap referensi diperhitungkan
- **Alasan:** referensi yang diberikan pemilik tidak dipakai.
- **Keputusan:** `REFERENCES.md` mendaftar setiap referensi dengan ID, apa yang terlihat, apa yang diambil, dan di mana dipakai. Ticket menyebut referensi yang dipakainya; visual-reviewer melaporkan referensi yang seharusnya dipakai sebuah gate tetapi tidak.

### C-05 Riset membaca sumbernya
- **Alasan:** "cek repository ini" dijawab dari ringkasan halaman depannya, dan tidak ada hasil yang berguna.
- **Keputusan:** researcher meng-clone atau membaca file-nya sendiri dan menulis catatan di `docs/research/` berisi apa yang dibaca, diambil, tidak diambil, dan tidak bisa dibaca. Sumber yang tidak bisa dibaca dilaporkan, tidak pernah diisi karangan.

### C-06 Giliran pendek, kerja berat di subagent
- **Alasan:** satu giliran berjalan hampir satu jam dengan puluhan perintah dan banyak gambar ukuran penuh, sampai konteks penuh dan harus di-compact.
- **Keputusan:** satu ticket per dispatch, seukuran satu shot, asset, atau sheet; producer berhenti di setiap gate; membangun, review frame, dan riset berjalan di subagent dengan laporan maksimal 40 baris; gambar dicek sebagai contact sheet yang diperkecil dulu. Penjaga pemakaian dan compact di batas ticket seperti di `WORKFLOW.md`.

### C-07 Upaya desain dan orisinalitas
- **Alasan:** sebuah karakter dibuat dengan mewarnai ulang maskot brand yang sudah ada, dan karakter yang digambar dengan sedikit detail ditolak.
- **Keputusan:** desain baru dimulai dari referensi dan skill `character-design`: beberapa opsi berdampingan dengan referensi, character sheet disetujui sebelum animasi apa pun, dan tidak ada desain yang didasarkan pada karakter, maskot, atau asset brand yang sudah ada tanpa persetujuan pemilik. Secara default asset-builder berjalan dengan effort medium di model terkuat.

### C-08 Pengetahuan sebelum produksi
- **Alasan:** pengetahuan dasar konten, motion, dan desain (hook, safe zone, easing, kontras, hierarki) tidak ada dalam pekerjaan.
- **Keputusan:** project membawa skill pengetahuan (`content-fundamentals`, `motion-principles`, `design-basics`, `character-design`) beserta sumbernya, dan menyarankan skill agent resmi dari tool video yang dipakai. Agent membaca skill yang sesuai dengan ticket.

### C-09 Satu tempat untuk status; file instruksi pendek
- **Keputusan:** status kerja hanya ada di `TODO.md` dan `HANDOFF.md`; dokumen lain tidak memuat angka status. `CLAUDE.md` tetap pendek dan merujuk dokumen alih-alih menyalinnya. Tidak ada aturan yang mewajibkan agent membaca semua dokumen.

## B. Keputusan project
{{PROJECT_DECISIONS}}

## C. Menunggu pemilik
{{WAITING_DECISIONS}}
