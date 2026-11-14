# DECISIONS: log keputusan untuk {{PROJECT_NAME}}

Dua seri. **W-xx** adalah keputusan workflow yang diwarisi dari plugin App Project Workflow; isinya menjelaskan mengapa aturan di `AGENTS.md`, `WORKFLOW.md`, dan subagent berbentuk seperti sekarang. Ubah hanya dengan menulis keputusan project baru yang menggantikannya, beserta alasannya. **D-xx** adalah keputusan project ini sendiri, mulai dari D-01.

Format per entri: judul dengan status dan tanggal, lalu Alasan, Keputusan, Konsekuensi (file yang berubah).

## A. Keputusan workflow (diwarisi saat setup, {{SETUP_DATE}})
Setiap aturan ditambahkan setelah kegagalan nyata dalam pemakaian. Buktinya ditulis singkat supaya alasannya tidak diperdebatkan ulang.

### W-01 Verifikasi lewat tool; test tidak dianggap asli
- **Alasan:** agent melaporkan "selesai" dan "lulus" untuk pekerjaan yang ternyata belum. Dalam pemakaian nyata, mematikan verifikasi tanda tangan sepenuhnya tetap membuat seluruh suite hijau, dan seorang tester dua kali melaporkan escape string yang tidak ada di file.
- **Keputusan:** klaim butuh output perintah yang baru dijalankan. Laporan agent dan dokumen lama bukan bukti. Angka status dikutip dari output perintah beserta tanggal, atau tidak ditulis. Setiap test baru dibuktikan merah sebelum perbaikan; logika otorisasi dan keamanan juga mendapat mutation check (rusak pengecekannya, test harus gagal, kembalikan, bandingkan dengan backup). Test yang sudah ada diaudit bertahap saat menjadi relevan.

### W-02 YAGNI untuk kode baru dan lama
- **Alasan:** agent sebelumnya menambahkan banyak baris yang tidak dipakai siapa pun. Mengaudit test saja tidak menyentuh kode berlebih yang masih berjalan.
- **Keputusan:** setiap baris harus punya pemakai nyata hari ini: persyaratan di `PRD.md` atau pemanggil di kode. Tiga pertanyaan per kandidat: (1) siapa yang memanggil atau memakainya (dibuktikan dengan grep atau test)? (2) ID persyaratan mana di `PRD.md` yang dilayaninya? (3) apa yang rusak kalau dihapus (dibuktikan dengan suite hijau)? Tanpa jawaban untuk (1) dan (2), kode itu menjadi kandidat penghapusan. Tidak ada refactor besar atas nama YAGNI. Daftar "fungsi tanpa referensi" dari tool hanya titik awal (banyak positif palsu dari template dan entry point framework).

### W-03 Kode lama: kunci perilaku dulu; TDD untuk logika baru
- **Keputusan:** sebelum mengubah kode lama yang kualitasnya tidak diketahui: pahami perilaku pentingnya, kunci dengan test yang terbukti jujur lewat mutation (W-01), ubah dalam langkah kecil, review diff dengan YAGNI (W-02), jalankan seluruh suite. Logika baru dengan aturan jelas: TDD murni (test gagal dulu). Test tidak menggantikan code review: test menjawab "apakah perilakunya benar", review menjawab "apakah kode ini layak dipertahankan".

### W-04 Alur ticket dengan router, worktree, dan subagent
- **Alasan:** bekerja satu item per satu item lambat begitu papan sudah berbentuk ticket, tetapi agent tanpa pengawasan membuat banyak kesalahan.
- **Keputusan:** sesi utama router (`.agents/skills/router/`) merencanakan dan memverifikasi; subagent worker, tester, reviewer, dan Explore (`.agents/agents/`) masing-masing mengerjakan satu ticket di git worktree yang dibuat `tools/wt.sh`. `tools/guard.sh` mengecek lingkup dan integritas test secara deterministik; `tools/verify.sh` menjalankan done criteria ticket. Laporan subagent adalah klaim; router menjalankan ulang guard dan verify. Di luar alur router, subagent dibuat hanya kalau pemilik meminta.

### W-05 Reviewer sesuai tingkat risiko
- **Alasan:** dalam pemakaian nyata reviewer memakai 56% sampai 80% token dari agent yang di-review-nya, dan model reviewer yang lebih ringan cukup tajam untuk ticket test.
- **Keputusan:** `pro` untuk auth, session, otorisasi, keamanan; `flash` untuk E2E, test, logika biasa; tanpa reviewer untuk perubahan teks saja. Satu putaran perbaikan boleh diverifikasi router dengan bukti, kecuali ticket keamanan, yang selalu di-review ulang. Ini hanya mengukur kesalahan yang tertangkap; kesalahan yang lolos dari semua lapisan tidak terukur.

### W-06 Router berjalan sendiri; persetujuan hanya untuk yang tidak bisa dibatalkan
- **Alasan:** meminta pemilik menyetujui merge, push, dan commit dokumen menambah gesekan tanpa menambah keamanan, karena semuanya bisa dibatalkan.
- **Keputusan:** router mengerjakan execution order tanpa `Ready` per ticket, merge `--no-ff` ke working branch setelah guard, verify, dan reviewer bersih, push setelah setiap ticket, dan menaikkan item Inbox yang tidak butuh keputusan pemilik. Setelah dua kegagalan, router mendiagnosis atau mengambil alih, bukan menunggu. Kedalaman test ditimbang per ticket. Tetap butuh persetujuan: daftar di `WORKFLOW.md`. Batas ticket dijaga siap compact. Laporan sekali per pasang ticket, ditambah laporan sesi.

### W-07 Ticket diukur agar muat dalam batas giliran agent
- **Alasan:** agent berhenti di `maxTurns` tanpa laporan; pada satu hari yang diukur, 36% token subagent terbuang di run yang terpotong. Menaikkan batas hanya memperbesar run yang gagal.
- **Keputusan:** budget di ticket sama dengan `maxTurns` agent; pekerjaan diukur sekitar 60% darinya (tester maksimal 6 sampai 8 mutasi, worker sekitar 8 file, reviewer 5 butir cek eksplisit). Setiap brief menyebut tool call tempat laporan harus dikirim (batas dikurangi 8). Setiap spawn memakan sekitar 20k sampai 25k token untuk membaca ulang, jadi kerja kecil dikerjakan router langsung.

### W-08 Lima skill disiplin, satu skill desain UI, ditambah penjaga hook `.env`
- **Keputusan:** project membawa lima skill disiplin di `.agents/skills/` (`verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`), skill `ui-design`, skill `router`, dan penjaga `.env` `PreToolUse` di `.agents/hooks.json`. Sengaja tidak dipasang: skill atau hook `SessionStart` yang memaksa ritual sebelum setiap balasan (menghabiskan konteks dan bertabrakan dengan "diskusi vs eksekusi"). Lisensi dan perubahan: `.agents/skills/NOTICE`.

### W-09 Satu tempat untuk status; file instruksi pendek
- **Keputusan:** status kerja hanya ada di `TODO.md` dan `HANDOFF.md`; dokumen lain tidak memuat angka status. `AGENTS.md` tetap pendek dan merujuk dokumen alih-alih menyalinnya. Tidak ada aturan yang mewajibkan agent membaca semua dokumen atau melaporkan skill di setiap balasan; ritual seperti itu diabaikan atau menghabiskan konteks dalam pemakaian nyata.

### W-10 Gate desain UI: 3 mockup nyata, angka keras, dan verifikasi browser
- **Alasan:** deskripsi desain berbasis teks semata ("bersih, modern") menghasilkan antarmuka generik khas AI dan tidak konsisten antar-ticket, sementara prompt yang terburu-buru atau tanpa batas membuat agent menghasilkan halaman yang terlalu kosong atau justru berlebihan.
- **Keputusan:** sebelum ticket fitur UI dijalankan, `designer` memeriksa referensi visual di `references/` (atau mencari inspirasi lewat `vercel-labs/agent-browser`) dan membangun 3 mockup HTML yang kontras (`references/mockups/option-1.html` sampai `option-3.html`) dengan patokan angka keras yang diadaptasi dari `Leonxlnx/taste-skill` (99.99% proportional fidelity, rasio warna 92% sampai 95% netral / <=3% accent, skala spacing ketat, serta batas bawah dan batas atas anatomi layar) dan diverifikasi di `agent-browser` pada `1440x900` dan `390x844`. Setelah pemilik memilih satu opsi, `DESIGN.md` dikunci (`Status: Locked`) dan ticket UI pertama membangun shared tokens serta base components.

## B. Keputusan project
{{PROJECT_DECISIONS}}

## C. Menunggu pemilik
{{WAITING_DECISIONS}}

