# WORKFLOW.md: alur ticket untuk {{PROJECT_NAME}}

Berlaku sejak setup ({{SETUP_DATE}}, W-04). Aturan project di `AGENTS.md` tetap berlaku penuh; file ini hanya menambahkan cara membagi kerja. Papan kerjanya `TODO.md`, satu file per ticket di `tickets/`.

## Starting a router session
Skill router adalah `.codex/skills/router/SKILL.md`. Alurnya sama di OpenAI Codex CLI (`codex`) maupun Codex desktop/IDE:
- Panggil skill `router` (`$router` atau minta Codex untuk "mulai sesi router dan kerjakan `TODO.md`"). Gunakan model sesi utama pilihan Anda (`{{ROUTER_MODEL}}` disarankan). Sesi biasa tanpa memanggil `router` tetap bekerja seperti biasa untuk diskusi atau pekerjaan singkat.

## Peran
| Peran | Model tier (`codex exec -m`) | Tugas | Batas |
|---|---|---|---|
| router (sesi utama) | {{ROUTER_MODEL}} | merencanakan, menulis brief, dispatch, verify, merge, menulis `TODO.md` | satu-satunya penulis `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/`; di `PRD.md` hanya Status dan Bukti sebuah persyaratan |
| worker | {{WORKER_MODEL}} | mengerjakan satu ticket di worktree | hanya file di Allow, tanpa commit |
| tester | {{TESTER_MODEL}} | test red-green, mutation check | hanya file test |
| reviewer | `gpt-5-codex` atau `codex-mini-latest`, sesuai tingkat risiko (di bawah) | review read-only atas ticket dan diff | `--sandbox read-only`, tidak menulis, tidak menjalankan test |
| Explore | {{EXPLORE_MODEL}} | mencari lokasi (`path:line`) | `--sandbox read-only`, bukan untuk menilai logika atau keamanan |

## Siklus ticket
`Ready` → `In progress` (worktree dibuat) → `Review` (worker/tester selesai) → `Verified` (guard, verify, reviewer bersih) → `Merged` → `Done`. Dua kali gagal: router mengambil alih, memecah ticket, atau mendiagnosis lalu menulis brief perbaikan baru (menaikkan model worker ke `gpt-5-codex` kalau perlu); tidak ada percobaan ketiga yang sama tanpa diagnosis, dan router tidak berhenti untuk menunggu pemilik (W-06).

### Antrian, merge, dan push (W-06)
- Router menjalankan "Execution order" di `TODO.md` sampai kosong, tanpa `Ready` per ticket. Item Inbox atau `Proposed` boleh dinaikkan menjadi ticket berikutnya kalau tidak butuh keputusan pemilik dan bisa dibatalkan; alasannya ditulis satu baris di antrian.
- Merge `--no-ff` ke working branch tanpa persetujuan setelah guard, verify, dan reviewer bersih. Merge dianggap berhasil kalau suite setelah merge hijau, worktree sudah dihapus, dan data test sudah dibersihkan; baru setelah itu ticket lain di repo yang sama boleh di-merge atau dimulai.
- Push otomatis setelah satu ticket kalau repo punya remote. Ticket kecil boleh berbagi push dengan ticket berikutnya; tidak boleh ada commit working branch yang belum di-push di akhir sesi. Dokumen di-commit di akhir setiap ticket.
- Laporan ke pemilik: satu ringkasan per pasang ticket, dan satu ketika antrian kosong.

### Tingkat risiko reviewer (W-05)
| Jenis ticket | Reviewer (`codex exec -m`) |
|---|---|
| Auth, session, otorisasi, keamanan | `gpt-5-codex` |
| E2E, test, logika biasa | `codex-mini-latest` |
| Hanya teks atau dokumen | tidak ada |

Satu putaran perbaikan atas temuan reviewer boleh diverifikasi router tanpa review kedua, asalkan setiap temuan punya bukti (output perintah atau baris kode). Pengecualian: ticket auth, session, otorisasi, dan keamanan selalu di-review ulang.

### Bukti test
- Router menimbang kedalaman test per ticket (W-06): teks, dokumen, atau config tanpa logika tidak perlu test baru, cukup suite yang relevan; test baru hanya di tempat perilakunya bisa salah. Alasannya ditulis satu baris di ticket.
- Logika auth/keamanan: red-green dan mutation check (aturan 5 di `AGENTS.md`).
- E2E: setiap assertion baru dibuktikan merah dengan merusak alurnya sebentar; test harus gagal. Hijau saja bukan bukti (assertion kosong tetap lulus).

## Tools (`tools/`)
Di Windows, jika shell adalah PowerShell, selalu jalankan skrip `.sh` dengan `bash tools/<script>.sh ...`.
- `workflow.conf`: repo (alias, path, working branch), file yang disalin ke worktree, perintah install, pola guard.
- `wt.sh add|rm <repo-alias> <ID>`: worktree di `_wt/<ID>-<alias>`, branch `t/<ID>` dari working branch, menyalin `COPY_FILES` tanpa membacanya, menjalankan `INSTALL_CMD`. `rm` menolak worktree dengan perubahan yang belum di-commit (`WT_DISCARD=1` untuk sengaja membuangnya), lalu menghapusnya dan menjalankan `branch -d` (menolak kalau belum di-merge).
- `guard.sh <wt> <base> <ticket>`: gagal kalau ada file di luar Allow, test yang dihapus, penanda skip/only/todo yang ditambahkan, baris assertion yang berkurang, atau commit apa pun di branch ticket di atas base (subagent tidak boleh commit). Karena itu router menjalankan guard **sebelum** commit.
- `verify.sh <wt> <ticket>`: menjalankan blok `verify` ticket, mencetak 25 baris terakhir dan exit code setiap baris.

## Batas paralel dan sumber daya bersama
- Maksimal 2 subagent sekaligus, hanya untuk ticket yang benar-benar independen. Ticket kecil (teks, satu baris) dikerjakan router langsung (`Executor: router`).
- Sumber daya bersama (masing-masing hanya boleh dipakai satu ticket pada satu waktu): {{SHARED_RESOURCES}}
- Verifikasi akhir (seluruh suite sebelum merge) hanya berjalan ketika tidak ada ticket lain yang berjalan.
- Kegagalan yang hilang saat dijalankan ulang masuk Inbox di `TODO.md`; tidak diabaikan.

## Pengecekan sebelum mulai
Tambahkan satu baris di sini untuk setiap prasyarat yang dibuktikan oleh run yang gagal; hapus setelah penyebabnya diperbaiki.
- Selalu jalankan skrip shell lewat `bash tools/<script>.sh`. Jangan `cd` ke worktree dan bertahan di sana; pakai `git -C <wt>` atau `codex exec -C <wt>`. Proses yang masih berada di folder itu membuat `wt.sh rm` gagal (folder terkunci di Windows).
- Commit ticket dan `bash tools/wt.sh rm` dijalankan sebagai perintah terpisah; cek `git -C <wt> log` dulu.

## Context and tokens
- Router membaca `TODO.md`, ticket aktif, dan laporan subagent (maksimal 40 baris). Router tidak membaca log lengkap atau diff lengkap.
- Status terkini ada di file ticket, jadi `/compact` di batas ticket tidak menghilangkan apa pun.
- Subagent berjalan di sesi `codex exec` terisolasi dan tidak melihat percakapan; semua konteks ada di ticket.
- Budget per ticket ada di ticket (`maxTurns`, retry maksimal 2). Ukuran ticket mengikuti W-07: muat dalam sekitar 60% batas giliran agent (tester maksimal 6 sampai 8 mutasi, worker sekitar 8 file, reviewer 5 butir cek eksplisit); brief menyebut batas tool call untuk laporan.
- **Batas ticket siap-berhenti (W-06):** jaga setiap batas ticket siap compact (`TODO.md`, ticket, dan `HANDOFF.md` terkini; dokumen sudah di-commit; tidak ada subagent berjalan). Ketika percakapan mulai panjang, minta pemilik menjalankan `/compact`. Ketika platform menampilkan pemberitahuan batas kuota atau pemakaian, selesaikan bagian yang sedang dipegang saja, perbarui ticket, `TODO.md`, dan `HANDOFF.md`, commit dokumen, lalu berhenti dengan laporan sisa pekerjaan.
- **Laporan sesi:** di akhir sesi router menulis `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: ticket yang selesai, keputusan, temuan Inbox, dan jumlah spawn/retry per ticket (W-07).

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, `reset --hard`, force-push, penghapusan massal di luar data test sendiri, menghapus atau melemahkan test, instalasi global, biaya, dan setiap item berstatus `Waiting decision`. Merge ke working branch dan push dilakukan router. Subagent tidak pernah commit, push, atau merge.

## Batasan yang diketahui
- `reviewer` dan `Explore` berjalan dengan `codex exec --sandbox read-only` sehingga OS/sandbox menegakkan akses read-only. Commit atau pengeditan di luar lingkup oleh `worker` atau `tester` ditangkap secara deterministik oleh `tools/guard.sh`.
- File `.env` dilindungi oleh aturan ketat di `AGENTS.md` dan di setiap prompt peran dalam `.codex/agents/`.

