# CLAUDE.md: {{PROJECT_NAME}}

Sengaja pendek. Detail ada di dokumen yang dirujuk; jangan disalin ke sini.
Terakhir diverifikasi: {{SETUP_DATE}}. **Sesi baru atau setelah compact: baca `HANDOFF.md` dulu.** Angka status (durasi, jumlah, versi) tidak ditulis di sini; ambil dari output perintah.

## Apa ini
{{PROJECT_SUMMARY}}

| Bagian | Path |
|---|---|
{{FOLDER_TABLE}}

Tool: {{TOOLCHAIN}}. Brief: `PRD.md`. Tampilan dan suara: `STYLE.md`. Referensi: `REFERENCES.md`.

## Cara bekerja dengan saya (pemilik: {{OWNER_ROLE}})
1. **Diskusi vs eksekusi.** Default-nya diskusi: kalau saya bertanya, berdiskusi, membandingkan, atau hanya mengirim gambar, jawab saja dan jangan mengubah file. Eksekusi hanya setelah ada perintah kerja yang jelas. Ragu? Tanyakan dalam satu kalimat.
2. **Task yang jelas dan bisa dibatalkan: kerjakan, jangan minta persetujuan per langkah.** Persetujuan hanya untuk yang tidak bisa dibatalkan dan di gate: lihat "Gates" dan "Still needs owner approval" di `WORKFLOW.md`.
3. **Ubah hanya yang diminta.** Temuan lain dilaporkan, tidak dikerjakan. **Ganti** versi lama, jangan menumpuk versi baru di sampingnya; hapus yang jadi mati. **YAGNI:** setiap file dan setiap elemen di layar harus punya alasan hari ini (persyaratan di `PRD.md`, baris di `STYLE.md`, atau pemanggil di kode).
4. **Jangan mengarang** fakta, angka, dialog, nama, atau isi sebuah referensi. Fakta di layar hanya dari naskah atau sumber yang disebut di `PRD.md`. Teks di layar sama dengan rekaman; mengubah dialog berarti rekam ulang, jadi tanyakan dulu.
5. **Lihat dulu, baru tafsirkan (C-01).** Untuk setiap gambar (screenshot saya, referensi, frame): tulis dulu apa yang terlihat, tandai `seen`, lalu tafsiran Anda, tandai `inferred`, dan ulangi permintaan saya dalam satu kalimat. Kalau tafsiran menentukan pekerjaan, tanyakan sebelum bertindak. Jangan mengklaim posisi, ukuran, atau warna persis dari melihat; ukur (crop, zoom, sampel piksel, frame grab di time code tertentu).
6. **Verifikasi lewat tool, bukan laporan (C-02).** Klaim "selesai" hanya dengan output perintah yang baru dijalankan **dan** frame sudah dilihat (skill `verification-before-completion`). Laporan agent dan dokumen lama bukan bukti. Katakan terus terang yang belum dilakukan: belum di-render, belum ditonton dengan suara, belum dicek di HP.
7. **Jangan commit atau push kecuali diminta**, kecuali producer yang commit dalam alur ticket (`WORKFLOW.md`). Conventional Commits, subject maksimal 72 karakter.
8. **Ringkasan untuk saya dalam bahasa sederhana**: apa yang berubah, tampilannya (dengan frame), risikonya, keputusan apa yang dibutuhkan dari saya.
9. Bahasa: balas saya dalam {{OWNER_LANGUAGE}}, mengikuti "Istilah" di bawah. Dokumen dalam Bahasa Indonesia. Kode, identifier, komentar, dan commit dalam bahasa Inggris. Tanpa em dash di dokumen.

## Istilah (Terms)
Berlaku untuk balasan, laporan, dan dokumen. Istilah ini tetap dalam bahasa Inggris, satu bentuk saja: ticket, task, gate, brief, storyboard, style frame, animatic, character sheet, turnaround, render, frame, shot, scene, asset, reference, producer, asset-builder, visual-reviewer, researcher, Inbox, Allow, verify, nilai status (`Ready`, `In progress`, `Planned`, `Met`, dan seterusnya), ID (`R-01`, `REF-01`, `C-01`, `D-01`), dan nama bagian yang dirujuk agent (misalnya "Execution order"). Istilah project yang disepakati dengan pemilik:

| Pakai | Jangan campur dengan |
|---|---|
{{PROJECT_TERMS}}

## Perintah (diverifikasi {{SETUP_DATE}})
{{COMMANDS}}

## Jebakan yang sudah terbukti (jangan ditebak ulang)
Tambahkan entri hanya setelah terbukti oleh output perintah, dengan tanggal.
{{PITFALLS}}

## Skill
- Di `.claude/skills/`: `content-fundamentals`, `motion-principles`, `design-basics`, `character-design` (pengetahuan, dibaca saat task membutuhkannya), `verification-before-completion`, `systematic-debugging`. Lisensi: `.claude/skills/NOTICE`.
- Skill untuk tool video: {{TOOL_SKILLS}}.
- **Alur ticket:** membagi kerja ke subagent hanya lewat `WORKFLOW.md`, dalam sesi producer. Di luar alur itu, subagent dibuat hanya kalau saya minta. Aturan 1 sampai 9 berlaku untuk setiap agent.

## Peta dokumen (baca yang dibutuhkan task, bukan semuanya)
`PRD.md` (brief: apa dan mengapa) · `STYLE.md` (tampilan dan suara) · `REFERENCES.md` (setiap referensi dan kegunaannya) · `WORKFLOW.md` (gate dan alur ticket) · `TODO.md` (satu-satunya papan kerja) · `HANDOFF.md` (status sesi terakhir, mulai dari sini) · `DECISIONS.md` (keputusan dan yang menunggu) · `docs/research/` (catatan riset bersumber){{EXTRA_DOCS}}
