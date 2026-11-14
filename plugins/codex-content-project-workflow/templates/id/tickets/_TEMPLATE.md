# <ID>: <judul singkat>

- **Gate:** <gate dari WORKFLOW.md, misalnya Style frames atau Shots>
- **Requirement:** <R-xx dari PRD.md, atau `-` untuk tooling dan dokumen>
- **References:** <REF-xx dari REFERENCES.md, masing-masing dengan apa yang diambil>
- **Executor:** producer | asset-builder (lalu visual-reviewer)
- **Model:** (default subagent dari `WORKFLOW.md`; tulis hanya kalau berbeda, dengan alasannya)
- **Budget:** maxTurns = batas agent (asset-builder 40, visual-reviewer 30), target sekitar 60%; laporan paling lambat di tool call (batas - 8); putaran perbaikan maksimal 2
- **Status:** Ready | In progress | Review | Done | Blocked
- **Blocked by:** -

## Goal
Satu paragraf: apa yang harus ada atau terlihat berbeda setelah ticket ini, dan mengapa.

## Context
Hanya yang dibutuhkan agent: path file, rentang waktu shot, baris naskah, jebakan relevan dari `AGENTS.md`, bagian `STYLE.md` yang berlaku. Subagent tidak melihat percakapan.

## Allow
Satu glob per baris dalam backtick (relatif terhadap root project). Apa pun di luar daftar ini adalah pelanggaran bagi `tools/scope.sh`.
- `path/to/scene-1.html`
- `path/to/assets/scene-1/*`

## Forbidden
- Jangan menimpa atau menghapus file asli (naskah, rekaman, art sumber) atau apa pun di `REFERENCES.md`.
- Jangan mengubah dialog, fakta, atau teks di layar yang berasal dari naskah.
- Jangan mendasarkan desain pada karakter, maskot, atau asset brand yang sudah ada, kecuali ticket ini menyebut pemilik sudah menyetujuinya.
- Jangan membuka atau menyalin `.env`. Temuan lain: tulis di Report sebagai kandidat Inbox.

## Verify
Setiap baris dijalankan dari root project lewat `bash tools/verify.sh`. Exit 0 = lulus.
```verify
{{DEFAULT_VERIFY}}
```

## Review
Frame yang harus diambil dan dicek visual-reviewer (time code), dan apa yang harus terlihat di masing-masing:
- 

## Report (diisi agent, maksimal 40 baris)
- File yang diubah:
- Output verify:
- Referensi yang dipakai dan caranya:
- Frame yang dihasilkan (path):
- Yang belum dikerjakan atau belum dicek:
- Temuan Inbox:

## Producer result
- scope:
- verify (dijalankan ulang producer):
- visual-reviewer:
- Ditunjukkan ke pemilik (tanggal):

