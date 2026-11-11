# HANDOFF: status sesi terakhir

Mulai dari sini saat membuka sesi baru. Buka Claude Code dari root project `{{PROJECT_ROOT}}` supaya `CLAUDE.md`, agent, dan skill project ikut termuat.
Diperbarui: {{SETUP_DATE}} (setup workflow). File ini hanya memuat status saat ini; riwayat ada di Done log `TODO.md` dan `git log`.

## Status saat ini (dicek dengan perintah, {{SETUP_DATE}})
{{CURRENT_STATE}}

## Langkah berikutnya
{{NEXT_STEP}}

## Cara bekerja
- Alur ticket: `WORKFLOW.md`. Router: `claude --agent router --model {{ROUTER_MODEL}} --effort high` dari root di terminal, atau router mode di `.claude/settings.local.json` untuk desktop app (`WORKFLOW.md`, "Starting a router session"). Sesi diskusi atau dokumen boleh berjalan tanpa router.
- Laporan sesi untuk pemilik: `{{SESSION_REPORT_DIR}}`.

## Menunggu pemilik
{{WAITING_OWNER}}

## Belum dicek di browser
Perubahan UI yang belum dilihat di browser sungguhan. Hapus barisnya setelah dicek.
