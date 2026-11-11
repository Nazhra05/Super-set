# AGENTS.md: {{PROJECT_NAME}}

Aturan kerja lengkap ada di `CLAUDE.md`. File ini hanya memuat aturan kode yang berlaku untuk semua agent.

## Anti-bloat
1. Tulis hanya yang diminta. Tidak ada elemen UI tambahan, fitur spekulatif, event listener khusus, atau state yang tidak diminta.
2. Tidak ada abstraksi prematur: tidak ada fungsi pembungkus sekali pakai, subkomponen sekali pakai, atau prop `variant` yang tidak dipakai di lebih dari satu tempat nyata.

## Test
3. Fokus pada logika bisnis. Lokasi test: {{TEST_LOCATIONS}}.
4. Tidak ada test negatif untuk fitur atau label yang sudah dihapus (misalnya memastikan teks yang dihapus tidak ada).
5. Tidak ada test rendering UI rapuh yang hanya menyimpan snapshot markup.{{TEST_RULES}}

## Dokumen
6. Baca hanya dokumen yang relevan dengan task (petanya di `CLAUDE.md`). Tidak wajib membaca semuanya atau melaporkan skill di setiap balasan; sebut skill atau dokumen hanya kalau memengaruhi hasil.
