# CLAUDE.md: {{PROJECT_NAME}}

Sengaja pendek. Detail ada di dokumen yang dirujuk; jangan disalin ke sini.
Terakhir diverifikasi: {{SETUP_DATE}}. **Sesi baru atau setelah compact: baca `HANDOFF.md` dulu.** Angka status (jumlah test, versi) tidak ditulis di sini; ambil dari output perintah.

## Apa ini
{{PROJECT_SUMMARY}}

| Alias repo | Path | Stack | Working branch |
|---|---|---|---|
{{REPO_TABLE}}

Sumber kebenaran nama (tabel, kolom, route, type): {{SOURCE_OF_TRUTH}}.

## Cara bekerja dengan saya (pemilik: {{OWNER_ROLE}})
1. **Diskusi vs eksekusi.** Default-nya diskusi: kalau saya bertanya, berdiskusi, atau membandingkan, jawab saja dan jangan mengubah file. Eksekusi hanya setelah ada perintah kerja yang jelas. Ragu? Tanyakan dalam satu kalimat.
2. **Task yang jelas dan bisa dibatalkan: kerjakan, jangan minta persetujuan per langkah.** Persetujuan hanya untuk yang tidak bisa dibatalkan: lihat "Still needs owner approval" di `WORKFLOW.md`. Dalam alur router, merge ke working branch dan push dilakukan router sendiri (W-06).
3. **Ubah hanya yang diminta.** Temuan lain dilaporkan, tidak dikerjakan. **Ganti** kode lama, jangan menumpuk versi baru di sampingnya; hapus yang jadi mati. **YAGNI:** setiap baris harus punya pemakai nyata hari ini (persyaratan di `PRD.md` atau pemanggil di kode); jangan menambah fitur, abstraksi, opsi, atau cadangan "untuk nanti". Pertanyaan yang sama berlaku saat meninjau kode yang sudah ada (W-02).
4. **Jangan mengarang** nama tabel, kolom, fungsi, file, atau angka. Verifikasi di sumber kebenaran di atas dan di kode.
5. **Verifikasi lewat tool, bukan laporan.** Klaim "selesai" atau "lulus" hanya dengan output perintah yang baru dijalankan (skill `verification-before-completion`). Laporan agent dan dokumen lama bukan bukti. Jangan melemahkan atau melewati test supaya lulus. **Test yang sudah ada tidak dianggap asli (W-01).** Untuk setiap perubahan: (a) buktikan red-green: test baru harus gagal pada kode sebelum perbaikan; (b) untuk logika otorisasi atau keamanan, jalankan mutation check (rusak pengecekannya sebentar, test harus gagal), lalu kembalikan dan bandingkan dengan backup; (c) bersihkan sisa test; (d) jalankan seluruh suite di akhir. Perubahan teks, dokumen, atau config tanpa logika tidak perlu test baru, cukup suite yang relevan.
6. **Jangan commit atau push kecuali diminta**, kecuali router dalam alur ticket (W-06). Conventional Commits, subject maksimal 72 karakter. Cek `git status` dulu; jangan menyentuh perubahan lokal di luar task.
7. **Ringkasan singkat untuk saya dalam bahasa sederhana (maksimal 8 sampai 10 baris)**: selalu tulis `<ID> (<judul singkat>)`, jangan pernah menulis ID saja (`T-xx`, `FR-xx`, `D-xx`). Sebutkan apa yang berubah, risikonya, dan keputusan apa yang dibutuhkan dari saya (tanpa dump log perintah atau daftar panjang path file). Kalau perubahan UI belum dicek di browser, katakan.
8. Bahasa: balas saya dalam {{OWNER_LANGUAGE}}, mengikuti "Istilah" di bawah. Dokumen dalam Bahasa Indonesia. Kode, identifier, komentar, dan commit dalam bahasa Inggris. Tanpa em dash di dokumen.

## Istilah (Terms)
Berlaku untuk balasan, laporan, dan dokumen. Gunakan Bahasa Indonesia yang natural untuk penjelasan, tetapi **seluruh istilah workflow dan istilah teknis software engineering wajib tetap dalam bahasa Inggris** (jangan diterjemahkan secara kaku): ticket, task, worktree, branch, commit, merge, push, router, scoper, designer, worker, tester, reviewer, guard, verify, Inbox, Allow, done criteria, blocked by, nilai status (`Ready`, `In progress`, `Planned`, `Met`, `Locked`, dan seterusnya), PRD, ID (`FR-01`, `W-01`, `D-01`, `REF-01`), nama bagian (misalnya "Execution order"), serta istilah teknis pemrograman dan UI seperti endpoint, route, middleware, payload, request, response, query, schema, migration, index, state, props, component, hook, context, render, build, bundle, lint, type-check, runtime, auth, session, token, mock, mockup, viewport, layout, density, assertion, regression, dan refactor. Istilah project yang disepakati dengan pemilik:

| Pakai | Jangan campur dengan |
|---|---|
{{PROJECT_TERMS}}

## Perintah (diverifikasi {{SETUP_DATE}})
{{COMMANDS}}

## Jebakan yang sudah terbukti (jangan ditebak ulang)
Tambahkan entri hanya setelah terbukti oleh output perintah, dengan tanggal.
{{PITFALLS}}

## Skill
- Di `.claude/skills/`, tanpa hook: `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `receiving-code-review`, `writing-plans`, `ui-design`. Alasan: `DECISIONS.md` W-08, W-10; lisensi: `.claude/skills/NOTICE`.
- TDD hanya untuk logika bisnis (lokasinya di `AGENTS.md`). Desain UI mengikuti `DESIGN.md` dan `ui-design` (3-mockup gate sebelum ticket UI, standar numerik 99.99%, diverifikasi lewat `agent-browser`).
- Perintah review bawaan: `/code-review`, `/simplify`, `/security-review`.
- Jangan menambah skill atau hook yang memaksa ritual sebelum setiap balasan, atau skill worktree atau subagent terpisah; alur ticket sudah mencakupnya (W-04, W-08).
- **Alur ticket (W-04):** membagi kerja ke worktree dan subagent hanya lewat `WORKFLOW.md`, dalam sesi router (terminal atau desktop, lihat di sana). Di luar alur itu, subagent dibuat hanya kalau saya minta. Aturan 1 sampai 8 berlaku untuk setiap agent.

## Peta dokumen (baca yang dibutuhkan task, bukan semuanya)
`PRD.md` (apa dan mengapa) · `DESIGN.md` (design system UI, 3-mockup gate, `references/`) · `WORKFLOW.md` (alur ticket) · `TODO.md` (satu-satunya papan kerja) · `HANDOFF.md` (status sesi terakhir, mulai dari sini) · `DECISIONS.md` (keputusan dan yang menunggu) · `AGENTS.md` (aturan kode dan test untuk semua agent){{EXTRA_DOCS}}
