# <ID>: <judul singkat>

- **Repo:** <alias repo dari tools/workflow.conf>
- **Requirement:** <FR-xx dari PRD.md, atau `-` untuk test, hygiene, dokumen>
- **Executor:** router | worker | tester (lalu reviewer)
- **Model:** (default subagent dari `WORKFLOW.md`; tulis hanya kalau berbeda, dengan alasannya)
- **Budget:** maxTurns = batas agent (tester/worker 40, reviewer 30), target sekitar 60%; laporan paling lambat di tool call (batas - 8); retry maksimal 2 (W-07)
- **Status:** Ready | In progress | Review | Verified | Merged | Done | Blocked
- **Blocked by:** -
- **Test depth:** (satu baris: mengapa test baru perlu atau tidak, W-06)

## Goal
Satu paragraf: apa yang harus berbeda setelah ticket ini, dan mengapa.

## Context
Hanya yang dibutuhkan agent: path file dan rentang baris, jebakan relevan dari `AGENTS.md`, rujukan `DECISIONS.md`. Subagent tidak melihat percakapan.

## Allow
Satu glob per baris dalam backtick (relatif terhadap root repo). Apa pun di luar daftar ini adalah pelanggaran bagi `tools/guard.sh`.
- `src/example.ts`
- `src/example.test.ts`

Checklist router sebelum dispatch:
- [ ] Setiap file output (screenshot, laporan, file yang dibuat ulang oleh dev server) ada di Allow.
- [ ] Ticket E2E: Report harus menunjukkan bukti merah untuk setiap assertion baru.
- [ ] Reviewer sesuai tingkat risiko di `WORKFLOW.md` (`pro`, `flash`, atau tidak ada).

## Forbidden
- Jangan membuka atau menyalin `.env`.
- Jangan menghapus atau melemahkan test.
- Temuan lain: tulis di Report sebagai kandidat Inbox, jangan dikerjakan.

## Verify
Setiap baris dijalankan di worktree lewat `bash tools/verify.sh`. Exit 0 = lulus.
```verify
{{DEFAULT_VERIFY}}
```

## Report (diisi agent, maksimal 40 baris)
- Ringkasan diff:
- Output verify:
- Temuan Inbox:
- Mutation/red-green (logika auth/keamanan):
- Bukti merah per assertion E2E baru (ticket E2E):

## Router result
- guard:
- verify (dijalankan ulang router):
- reviewer:
- Merge:

