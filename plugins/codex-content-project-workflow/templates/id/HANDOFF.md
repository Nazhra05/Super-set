# HANDOFF: status sesi terakhir

Mulai dari sini saat membuka sesi baru. Buka Codex dari root project `{{PROJECT_ROOT}}` supaya `AGENTS.md`, `.codex/skills/`, dan `.codex/agents/` ikut termuat.
Diperbarui: {{SETUP_DATE}} (setup workflow). File ini hanya memuat status saat ini; riwayat ada di Done log `TODO.md`.

## Status saat ini (dicek dengan perintah, {{SETUP_DATE}})
{{CURRENT_STATE}}

## Langkah berikutnya
{{NEXT_STEP}}

## Cara bekerja
- Gate dan alur ticket: `WORKFLOW.md`. Producer: panggil skill `producer` (`$producer` atau minta untuk memulai sesi producer; model utama yang disarankan `{{PRODUCER_MODEL}}`, lihat `WORKFLOW.md`, "Starting a producer session"). Sesi diskusi boleh berjalan tanpa producer.
- Laporan sesi untuk pemilik: `{{SESSION_REPORT_DIR}}`.

## Menunggu pemilik
{{WAITING_OWNER}}

## Belum dilihat atau didengar pemilik
Frame, render, atau perubahan audio yang belum dilihat atau didengar pemilik. Hapus barisnya setelah dilihat.

