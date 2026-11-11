# WORKFLOW.md: gate dan alur ticket untuk {{PROJECT_NAME}}

Berlaku sejak setup ({{SETUP_DATE}}). Aturan project di `CLAUDE.md` tetap berlaku penuh; file ini menambahkan gate produksi dan cara membagi kerja. Papan kerjanya `TODO.md`, satu file per ticket di `tickets/`.

## Starting a producer session
Profil producer adalah `.claude/agents/producer.md`. Alurnya sama di setiap surface; yang berbeda hanya cara memulainya.
- **Terminal (macOS, Linux, Windows):** dari root project, `claude --agent producer --model {{PRODUCER_MODEL}} --effort high`. Sesi `claude` biasa tetap bekerja seperti sebelumnya.
- **Desktop app** (atau surface lain yang tidak bisa memberi `--agent`): taruh key berikut di `.claude/settings.local.json` (pribadi, tidak di-commit), lalu buka sesi baru di folder project:
  ```json
  {
    "agent": "producer",
    "model": "{{PRODUCER_MODEL}}",
    "effortLevel": "high",
    "env": { "WORKFLOW_SURFACE": "desktop" }
  }
  ```
  Selama key itu ada, setiap sesi baru di project ini pada mesin ini dimulai sebagai producer. Hapus keempat key untuk kembali ke sesi biasa.

## Peran
| Peran | Model / effort | Tugas | Batas |
|---|---|---|---|
| producer (sesi utama) | {{PRODUCER_MODEL}} / high | merencanakan gate dan ticket, menulis brief, dispatch, verify, melapor ke pemilik | satu-satunya penulis `TODO.md`, `HANDOFF.md`, `DECISIONS.md`, `REFERENCES.md`, `tickets/`; di `PRD.md` hanya Status dan Bukti; `STYLE.md` hanya setelah gate yang disetujui pemilik |
| asset-builder | {{BUILDER_MODEL}} / medium | mengerjakan satu ticket: art, karakter, scene, cue audio | hanya file di Allow, tanpa commit; satu builder pada satu waktu |
| visual-reviewer | {{REVIEWER_MODEL}} / high | review read-only atas frame dan file terhadap ticket, `STYLE.md`, `PRD.md`, dan referensi yang disebut | tidak mengubah file project; frame grab disimpan di `.review/` |
| researcher | {{RESEARCHER_MODEL}} / medium | membaca sumber luar dan menulis satu catatan bersumber | hanya menulis `docs/research/<topic>.md` dan clone di `.research/` |
| Explore | {{EXPLORE_MODEL}} / low | mencari lokasi file dan baris | tidak menilai |

## Gates
Produksi melewati gate berikut secara berurutan. Gate bertanda **approval** menghentikan producer sampai pemilik setuju, dengan bukti di depan mereka (frame, sheet, rough cut). Status setiap gate ada di `TODO.md`, bagian "Gates".

| Gate | Hasil | Pemilik |
|---|---|---|
| Brief | `PRD.md` disepakati | **approval** |
| Script dan storyboard | naskah dikunci sesuai rekaman; satu panel per shot dengan time code, framing, aksi, teks di layar | laporan |
| Style frames | 2 sampai 4 still frame berwarna penuh dari shot kunci, ditampilkan di samping referensi yang dijawabnya | **approval** |
| Character sheets | per karakter: turnaround, expression sheet, mouth chart, pose sheet, warna (skill `character-design`) | **approval** |
| Animatic | rough cut berwaktu dengan audio asli | **approval** |
| Shots | setiap shot dibangun dan di-review per ticket | laporan per pasang ticket |
| Final | render penuh, audio diukur, caption dicek, ditonton pemilik dengan suara | **approval** |

Gate hanya boleh dilewati lewat keputusan project (D-xx) beserta alasannya, misalnya "tidak ada karakter di project ini".

## Alur ticket
1. Ambil item berikutnya dari "Execution order" di `TODO.md`. Lewati item dengan `Blocked by` atau `Waiting decision` yang masih terbuka, atau yang berada di balik gate yang belum disetujui.
2. Isi ticket dari `tickets/_TEMPLATE.md`: tujuan, persyaratan (`R-xx`), referensi (`REF-xx`) dan apa yang diambil dari masing-masing, glob Allow, perintah verify, frame yang harus dicek reviewer. Ukurannya satu shot, satu asset, atau satu sheet.
3. Dispatch satu `asset-builder` dengan path ticket. Builder bekerja di folder project (tanpa worktree: render dan art berukuran besar), jadi hanya satu builder berjalan pada satu waktu; researcher, visual-reviewer, dan Explore boleh berjalan bersamaan.
4. Saat kembali, laporannya adalah klaim. Jalankan sendiri `tools/scope.sh <ticket>` (hanya di git) dan `tools/verify.sh <ticket>`.
5. Dispatch `visual-reviewer` dengan path ticket. Reviewer mengambil frame yang disebut di ticket dan melaporkan setiap butir cek sebagai `seen` atau `inferred`, beserta file frame-nya.
6. Putaran perbaikan maksimal dua; setelah itu diagnosis (`systematic-debugging`) atau pecah ticket. Tidak ada percobaan ketiga yang buta.
7. Selesai: perbarui ticket, `TODO.md`, Status dan Bukti persyaratan di `PRD.md`, dan "Dipakai di" di `REFERENCES.md`. Di repo git, commit file ticket dan dokumen. Push hanya dengan persetujuan pemilik, kecuali keputusan project mengizinkan.
8. Lapor ke pemilik sekali per gate dan sekali per pasang ticket shot, dengan frame-nya.

## Gambar dari pemilik (C-01)
Saat pemilik mengirim screenshot atau frame: tulis apa yang terlihat (`seen`), tafsiran Anda (`inferred`), dan permintaannya dalam satu kalimat. Kalau gambar bisa berarti dua perbaikan berbeda, tanyakan sebelum membangun. Temukan masalahnya dengan pengukuran atau frame grab di waktu yang tepat, bukan dengan perkiraan mata.

## Research
Sumber dibaca, bukan diringkas dari halaman depannya (C-05).
- **Repository:** clone dangkal ke `.research/<name>` (`git clone --depth 1`), atau daftar dan baca file dengan `gh api repos/<owner>/<repo>/contents/<path>`. Baca README, struktur folder, dan file yang penting.
- **Halaman web:** ambil halamannya; untuk halaman panjang baca lanjut dengan offset sampai bagian yang relevan terbaca.
- **Catatan:** `docs/research/<topic>.md` berisi file atau halaman yang dibaca, apa yang diambil (dengan path atau URL), apa yang tidak diambil dan alasannya, dan apa yang tidak bisa dibaca. Sumber yang tidak bisa dibaca dilaporkan apa adanya, tidak pernah diisi karangan.
- Lisensi: menyalin kode atau art butuh cek lisensi dan persetujuan pemilik; membaca untuk ide tidak.

## Context and tokens
- Producer membaca `TODO.md`, ticket aktif, dan laporan subagent (maksimal 40 baris). Producer tidak membaca transkrip atau diff lengkap.
- Gambar mahal. Lihat contact sheet yang diperkecil dulu; buka frame penuh hanya di tempat detailnya penting.
- Satu ticket per dispatch, satu gate per rentang kerja: lapor di gate alih-alih berjalan terus berjam-jam.
- **Pemakaian (terminal):** baca `.claude/usage.json` (ditulis `tools/statusline.js`) sebelum dispatch. Di atas 90% batas 5 jam atau 7 hari, atau file tidak ada atau lebih tua dari 10 menit: hanya kerja yang pasti selesai dengan bersih; kalau tidak ada, berhenti, perbarui ticket, `TODO.md`, dan `HANDOFF.md`, lalu lapor. Konteks 60% atau lebih: siapkan compact di batas ticket dan minta pemilik menjalankan `/compact`.
- **Desktop app:** status line tidak berjalan di sana (`WORKFLOW_SURFACE=desktop`). Jaga setiap batas ticket siap compact, dan ketika app menampilkan pemberitahuan batas pemakaian, selesaikan bagian yang sedang dipegang saja, perbarui file di atas, lalu berhenti dengan laporan.
- **Laporan sesi:** di akhir sesi tulis `{{SESSION_REPORT_DIR}}/Session_<date>_<topic>.md`: ticket yang selesai, gate yang dilewati, keputusan, temuan Inbox, dan biaya (token per agent, run yang terpotong).

## Frame checks
Frame grab: {{FRAME_COMMAND}}. Frame untuk review disimpan di `.review/` (tidak di-commit). Setiap ticket shot menyebut time code yang dicek: frame pertama, setiap pergantian teks, setiap pergantian ekspresi karakter, dan frame terakhir.

## Still needs owner approval
{{IRREVERSIBLE_ACTIONS}}, gate bertanda **approval**, mengubah dialog atau fakta, memakai asset pihak ketiga (lisensi), mendasarkan karakter atau desain baru pada karakter, maskot, atau asset brand yang sudah ada, mengirim materi project ke layanan AI eksternal, menghapus file di luar output test sendiri, instalasi global, biaya, dan setiap item berstatus `Waiting decision`. Subagent tidak pernah commit, push, atau publish.

## Batasan yang diketahui
- Tanpa git, `tools/scope.sh` tidak bisa mengecek file mana yang diubah builder; producer lalu mendaftar file yang berubah menurut waktu modifikasi dan menyebut bahwa cek dilewati.
- Tool Edit/Write milik producer tidak bisa dibatasi per path; disiplinnya ada di prompt.
- Claude membaca gambar dengan presisi terbatas untuk posisi, ukuran, dan jumlah yang persis; aturan 5 di `CLAUDE.md` adalah jawabannya, bukan jaminan.
