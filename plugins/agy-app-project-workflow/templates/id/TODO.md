# TODO.md: satu-satunya papan kerja untuk {{PROJECT_NAME}}

Satu-satunya daftar kerja yang hidup. Keputusan ada di `DECISIONS.md`, status sesi di `HANDOFF.md`.

## Aturan pakai
1. **Temuan baru masuk Inbox dulu, tidak langsung dikerjakan.** Detailnya cukup: apa, bukti, dampak. Router boleh memilah item yang tidak butuh keputusan pemilik dan bisa dibatalkan (W-06); sisanya didiskusikan dengan pemilik.
2. **Router menjalankan "Execution order" sampai kosong** tanpa `Ready` per ticket (W-06), lalu menambahkan item Inbox atau `Proposed` yang cocok ke antrian dengan alasan satu baris. `In progress` maksimal dua, sesuai batas paralel di `WORKFLOW.md`. Item dengan `Blocked by` atau `Waiting decision` yang masih terbuka dilewati.
3. **Status:** `Inbox` · `Proposed` (disarankan; router boleh menaikkannya kalau tidak butuh keputusan pemilik) · `Ready` · `In progress` · `Done` · `Waiting decision` (butuh jawaban pemilik) · `Blocked` (menunggu task lain).
4. **Batas lingkup.** Temuan di tengah task berhenti di batas task, masuk Inbox, dan kerja berlanjut. Tidak ada perluasan lingkup diam-diam, tidak ada instalasi dependensi atau perubahan config yang tidak tertulis di task.
5. **Setiap task punya done criteria berupa perintah verifikasi.** Klaim selesai hanya dengan output perintah (aturan 5 di `AGENTS.md`). Perubahan yang tidak bisa dibatalkan selalu minta persetujuan terpisah (`WORKFLOW.md`).
6. **Owner:** `Owner` (aksi di server, akun, layanan eksternal) atau `Agent`.
7. **Eksekusi ticket** mengikuti `WORKFLOW.md`. Task yang dikerjakan worker/tester mendapat `tickets/<ID>.md` dari `tickets/_TEMPLATE.md`; papan ini tetap satu-satunya daftar.

## Execution order
| # | Task | Owner | Alasan urutan |
|---|---|---|---|
{{EXECUTION_ORDER}}

## Tasks
Kelompokkan per jalur saat papan membesar (misalnya Security, Tests, Product, Hygiene, Deploy). Prefix ID = huruf jalur.
| ID | Task | Owner | Status | Blocked by | Done criteria |
|---|---|---|---|---|---|
{{TASKS}}

## Inbox (belum dipilah; jangan dikerjakan)
{{INBOX}}

## Done log
Terbaru di atas: tanggal, ID, satu baris, commit.

