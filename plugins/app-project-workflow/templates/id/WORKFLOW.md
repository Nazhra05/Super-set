# WORKFLOW.md: alur ticket untuk {{PROJECT_NAME}}

Berlaku sejak setup ({{SETUP_DATE}}, W-04). Aturan project di `CLAUDE.md` tetap berlaku penuh; file ini hanya menambahkan cara membagi kerja. Papan kerjanya `TODO.md`, satu file per ticket di `tickets/`.

## Starting a router session
Profil router adalah `.claude/agents/router.md`. Alurnya sama di setiap surface; yang berbeda hanya cara memulai router.
- **Terminal (macOS, Linux, Windows):** dari root project, `claude --agent router --model {{ROUTER_MODEL}} --effort high`. Sesi `claude` biasa tetap bekerja seperti sebelumnya.
- **Desktop app** (atau surface lain yang tidak bisa memberi `--agent`): nyalakan router mode dengan menaruh key berikut di `.claude/settings.local.json` (pribadi, tidak di-commit), lalu buka sesi baru di folder project:
  ```json
  {
    "agent": "router",
    "model": "{{ROUTER_MODEL}}",
    "effortLevel": "high",
    "env": { "WORKFLOW_SURFACE": "desktop" }
  }
  ```
  Selama key itu ada, setiap sesi baru di project ini pada mesin ini dimulai sebagai router. Hapus keempat key untuk kembali ke sesi biasa. Minta Claude di sesi biasa untuk menyalakan atau mematikannya; cukup mengubah satu file.

## Peran
| Peran | Model / effort | Tugas | Batas |
|---|---|---|---|
| router (sesi utama) | {{ROUTER_MODEL}} / high | merencanakan, menulis brief, dispatch, verify, merge, menulis `TODO.md` | satu-satunya penulis `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `tickets/`; di `PRD.md` hanya Status dan Bukti sebuah persyaratan; tidak membaca file kode mentah |
| scoper | {{EXPLORE_MODEL}} / low | mencari `path:line` dan mengembalikan draf ticket siap pakai | read-only, laporan maksimal 35 baris |
| designer | {{WORKER_MODEL}} / high | memeriksa `references/` + `agent-browser`, membuat 3 mockup HTML di `references/mockups/`, mengunci `DESIGN.md` | hanya mengubah `DESIGN.md` dan `references/`; standar numerik 99.99% |
| worker | {{WORKER_MODEL}} / low | mengerjakan satu ticket di worktree | hanya file di Allow, tanpa commit |
| tester | {{TESTER_MODEL}} / medium | test red-green, mutation check | hanya file test |
| reviewer | opus atau sonnet / high, sesuai tingkat risiko (di bawah) | review read-only atas ticket dan diff | tidak menulis, tidak menjalankan test |
| Explore | {{EXPLORE_MODEL}} / low | mencari lokasi (`path:line`) | bukan untuk menilai logika atau keamanan |

## Siklus ticket
`Ready` → `In progress` (worktree dibuat) → `Review` (worker/tester selesai) → `Verified` (guard, verify, reviewer bersih) → `Merged` → `Done`. Dua kali gagal: router mengambil alih, memecah ticket, atau mendiagnosis lalu menulis brief perbaikan baru (menaikkan model kalau perlu); tidak ada percobaan ketiga yang sama tanpa diagnosis, dan router tidak berhenti untuk menunggu pemilik (W-06).

### Antrian, merge, dan push (W-06)
- Router menjalankan "Execution order" di `TODO.md` sampai kosong, tanpa `Ready` per ticket. Item Inbox atau `Proposed` boleh dinaikkan menjadi ticket berikutnya kalau tidak butuh keputusan pemilik dan bisa dibatalkan; alasannya ditulis satu baris di antrian.
- Merge `--no-ff` ke working branch tanpa persetujuan setelah guard, verify, dan reviewer bersih. Merge dianggap berhasil kalau suite setelah merge hijau, worktree sudah dihapus, dan data test sudah dibersihkan; baru setelah itu ticket lain di repo yang sama boleh di-merge atau dimulai.
- Push otomatis setelah satu ticket kalau repo punya remote. Ticket kecil boleh berbagi push dengan ticket berikutnya; tidak boleh ada commit working branch yang belum di-push di akhir sesi. Dokumen di-commit di akhir setiap ticket.
- Laporan ke pemilik: satu ringkasan singkat (maksimal 8 sampai 10 baris) per pasang ticket dan satu ketika antrian kosong, selalu menulis `<ID> (<judul singkat>)` (bukan ID saja), dengan 3 butir: (1) **Done**, (2) **Next** (ditambah pengingat `/compact` setiap selesai sepasang ticket), dan (3) **Needs your decision**.

### Gate desain UI (3 mockup sebelum ticket UI, W-10)
- Ketika status `DESIGN.md` adalah `Proposed (awaiting 3-mockup gate)`, router belum men-dispatch `worker` untuk ticket fitur UI. Sebagai gantinya, router men-dispatch `designer` dengan **brief ringkas (maksimal 6 sampai 8 baris)**: layar utama dan ID persyaratan dari `PRD.md`, file atau URL di `references/brand/` dan `references/inspiration/`, serta batasan viewport/mode. Jangan menulis karangan teks panjang untuk menjelaskan jarak atau gaya visual di brief; `designer` melihat langsung gambar referensi dan menerapkan aturan numerik keras di `.claude/skills/ui-design/SKILL.md`.
- `designer` mencari inspirasi lewat `agent-browser` bila `references/inspiration/` kosong, membangun `references/mockups/option-1.html`, `option-2.html`, dan `option-3.html`, serta memverifikasinya di `agent-browser` pada ukuran `1440x900` dan `390x844`.
- Router menunjukkan ketiga opsi mockup dan screenshot-nya kepada pemilik. Setelah pemilik memilih satu opsi (atau gabungan layout + palet/tipografi), router men-dispatch `designer` untuk mengunci `DESIGN.md` (`Status: Locked`) dan menjalankan ticket pondasi UI pertama (tokens + base components) sebelum ticket fitur UI lainnya.

### Tingkat risiko reviewer (W-05)
| Jenis ticket | Reviewer |
|---|---|
| Auth, session, otorisasi, keamanan | opus |
| E2E, test, logika biasa | sonnet |
| Hanya teks atau dokumen | tidak ada |

Satu putaran perbaikan atas temuan reviewer boleh diverifikasi router tanpa review kedua, asalkan setiap temuan punya bukti (output perintah atau baris kode). Pengecualian: ticket auth, session, otorisasi, dan keamanan selalu di-review ulang.

### Bukti test
- Router menimbang kedalaman test per ticket (W-06): teks, dokumen, atau config tanpa logika tidak perlu test baru, cukup suite yang relevan; test baru hanya di tempat perilakunya bisa salah. Alasannya ditulis satu baris di ticket.
- Logika auth/keamanan: red-green dan mutation check (aturan 5 di `CLAUDE.md`).
- E2E: setiap assertion baru dibuktikan merah dengan merusak alurnya sebentar; test harus gagal. Hijau saja bukan bukti (assertion kosong tetap lulus).

## Tools (`tools/`)
- `workflow.conf`: repo (alias, path, working branch), file yang disalin ke worktree, perintah install, pola guard.
- `wt.sh add|rm|check|land <repo-alias> <ID> [argumen...]`:
  - `add`: membuat worktree di `_wt/<ID>-<alias>`, branch `t/<ID>` dari working branch, menyalin `COPY_FILES` tanpa membacanya, menjalankan `INSTALL_CMD`.
  - `check`: menjalankan `guard.sh`, `verify.sh`, dan `git diff --stat` dalam satu perintah sebelum commit apa pun.
  - `land "<pesan-commit>"`: mengecek `guard.sh`, commit di branch `t/<ID>`, merge `--no-ff` ke working branch, menghapus worktree dan branch ticket, serta menjalankan ulang `verify.sh` di working branch dalam satu perintah.
  - `rm`: menolak worktree dengan perubahan yang belum di-commit (`WT_DISCARD=1` untuk sengaja membuangnya), lalu menghapusnya dan menjalankan `branch -d` (menolak kalau belum di-merge).
- `guard.sh <wt> <base> <ticket>`: gagal kalau ada file di luar Allow, test yang dihapus, penanda skip/only/todo yang ditambahkan, baris assertion yang berkurang, atau commit apa pun di branch ticket di atas base (subagent tidak boleh commit). Karena itu router menjalankan guard **sebelum** commit.
- `verify.sh <wt> <ticket>`: menjalankan blok `verify` ticket, mencetak 25 baris terakhir dan exit code setiap baris.
- `statusline.js`: status line yang menyimpan JSON status Claude Code ke `.claude/usage.json` untuk pengecekan pemakaian di bawah. Hanya berjalan di terminal.

## Batas paralel dan sumber daya bersama
- Maksimal 2 subagent sekaligus, hanya untuk ticket yang benar-benar independen. Ticket kecil (teks, satu baris) dikerjakan router langsung (`Executor: router`).
- Sumber daya bersama (masing-masing hanya boleh dipakai satu ticket pada satu waktu): {{SHARED_RESOURCES}}
- Verifikasi akhir (seluruh suite sebelum merge) hanya berjalan ketika tidak ada ticket lain yang berjalan.
- Kegagalan yang hilang saat dijalankan ulang masuk Inbox di `TODO.md`; tidak diabaikan.

## Pengecekan sebelum mulai
Tambahkan satu baris di sini untuk setiap prasyarat yang dibuktikan oleh run yang gagal; hapus setelah penyebabnya diperbaiki.
- Jangan `cd` ke worktree di shell utama; pakai subshell `( cd ... && ... )` atau `git -C`. Shell yang masih berada di folder itu membuat `wt.sh rm` gagal (folder terkunci di Windows).
- Commit ticket dan `wt.sh rm` dijalankan sebagai perintah terpisah; cek `git log` di worktree dulu.

## Context and tokens
- Router membaca `TODO.md`, ticket aktif, dan laporan subagent (maksimal 40 baris). Router tidak membaca transkrip atau diff lengkap.
- Status terkini ada di file ticket, jadi compact atau `/clear` di batas ticket tidak menghilangkan apa pun.
- Subagent tidak melihat percakapan; semua konteks ada di ticket.
- Budget per ticket ada di ticket (`maxTurns`, retry maksimal 2). Ukuran ticket mengikuti W-07: muat dalam sekitar 60% batas giliran agent (tester maksimal 6 sampai 8 mutasi, worker sekitar 8 file, reviewer 5 butir cek eksplisit); brief menyebut batas tool call untuk laporan.
- **Pemakaian dan konteks (W-06):** di terminal, baca `.claude/usage.json` (ditulis oleh `tools/statusline.js`) sebelum memulai ticket dan sebelum dispatch, misalnya `node -e "const u=require('./.claude/usage.json');console.log(u.savedAt,u.context_window?.used_percentage,u.rate_limits)"`.
  - Pemakaian 5 jam atau 7 hari di atas 90%: hanya kerja yang pasti selesai dengan bersih, tanpa dispatch baru dan tanpa run panjang. Kalau tidak ada: berhenti, siapkan handoff, laporkan waktu reset. File tidak ada atau lebih tua dari 10 menit = tidak diketahui, perlakukan sebagai di atas 90%.
  - Konteks 60% atau lebih: siapkan compact di batas ticket (ticket, `TODO.md`, `HANDOFF.md` terkini; dokumen sudah di-commit; tidak ada subagent berjalan), lalu minta pemilik menjalankan `/compact`.
  - **Desktop app tidak menjalankan status line** (dicek 2026-11-11: sesi desktop tidak mengubah `usage.json`), jadi file itu tidak diperbarui di sana (`WORKFLOW_SURFACE=desktop`). Router tidak menganggap file yang basi sebagai "di atas 90%". Sebagai gantinya, router menjaga setiap batas ticket siap compact (file di atas terkini, dokumen sudah di-commit), dan ketika app menampilkan pemberitahuan batas pemakaian, router menyelesaikan bagian yang sedang dipegang saja, memperbarui ticket, `TODO.md`, dan `HANDOFF.md`, meng-commit dokumen, lalu berhenti dengan laporan sisa pekerjaan.
- **Laporan sesi:** di akhir sesi router menulis `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: ticket yang selesai, keputusan, temuan Inbox, dan rincian biaya (token per agent dari pemberitahuan selesai, biaya USD dari `.claude/usage.json` atau `/cost`), termasuk token dari run yang terpotong dan jumlah spawn per ticket (W-07).

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, `reset --hard`, force-push, penghapusan massal di luar data test sendiri, menghapus atau melemahkan test, instalasi global, biaya, dan setiap item berstatus `Waiting decision`. Merge ke working branch dan push dilakukan router. Subagent tidak pernah commit, push, atau merge.

## Batasan yang diketahui
- `.claude/settings.json` menolak tool Read untuk `.env`, `.env.local`, `.env.production`. Ini tidak mencakup `cat` lewat Bash; itu tetap memunculkan prompt. Commit oleh subagent ditangkap `guard.sh`, bukan oleh deny global, karena deny global juga akan memblokir commit yang diperintahkan pemilik di sesi utama.
- Tool Edit/Write milik router tidak bisa dibatasi per path; disiplinnya ada di prompt.
- `effort` di frontmatter agent tidak terdokumentasi berlaku untuk sesi utama, jadi `--effort high` menjadi bagian dari perintah peluncuran.
