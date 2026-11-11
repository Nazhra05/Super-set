# TODO.md: satu-satunya papan kerja untuk {{PROJECT_NAME}}

Satu-satunya daftar kerja yang hidup. Keputusan ada di `DECISIONS.md`, status sesi di `HANDOFF.md`.

## Aturan pakai
1. **Temuan baru masuk Inbox dulu, tidak langsung dikerjakan.** Detailnya cukup: apa, bukti (frame, time code, file), dampak.
2. **Gate dulu.** Pekerjaan di balik gate yang belum disetujui menunggu. Producer menjalankan "Execution order" sampai gate berikutnya yang bertanda approval, lalu berhenti dan melapor.
3. **Status:** `Inbox` · `Proposed` · `Ready` · `In progress` · `Done` · `Waiting decision` (butuh jawaban pemilik) · `Blocked` (menunggu task lain).
4. **Batas lingkup.** Temuan di tengah task masuk Inbox dan kerja berlanjut. Tidak ada perluasan lingkup diam-diam, tidak ada instalasi tool yang tidak tertulis di task.
5. **Setiap task punya done criteria berupa perintah atau cek frame.** Klaim selesai hanya dengan output dan frame yang sudah dilihat (aturan 6 di `CLAUDE.md`).
6. **Owner:** `Owner` (persetujuan, rekaman, akun, publikasi) atau `Claude`.
7. **Eksekusi ticket** mengikuti `WORKFLOW.md`; ticket ada di `tickets/`.

## Gates
| Gate | Status | Disetujui (tanggal) | Bukti |
|---|---|---|---|
{{GATES}}

## Execution order
| # | Task | Owner | Alasan urutan |
|---|---|---|---|
{{EXECUTION_ORDER}}

## Tasks
| ID | Task | Persyaratan | Referensi | Owner | Status | Blocked by | Done criteria |
|---|---|---|---|---|---|---|---|
{{TASKS}}

## Inbox (belum dipilah; jangan dikerjakan)
{{INBOX}}

## Done log
Terbaru di atas: tanggal, ID, satu baris, commit atau file.
