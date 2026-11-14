# DESIGN.md: UI dan design system untuk {{PROJECT_NAME}}

Terakhir diperbarui: {{SETUP_DATE}}. Status: **{{DESIGN_STATUS}}**.
Router dan designer memperbarui file ini pada 3-mockup design gate; begitu statusnya `Locked`, worker wajib memakai token dan component yang sudah dikunci di bawah dan dilarang mengarang warna hex baru, font family baru, atau gaya card baru di setiap ticket.

## 1. Archetype produk dan mode ruang kerja
{{DESIGN_ARCHETYPE}}

## 2. Standar kualitas numerik (99.99% proportional fidelity)
Setiap mockup dan ticket UI dinilai menggunakan angka keras, bukan kata sifat yang kabur:
- **Rasio warna:** 92% sampai 95% permukaan netral (`--bg`, `--surface`, `--surface-subtle`), 4% sampai 6% ink dan garis batas (`1px solid` pada opasitas ink 10% sampai 14%), dan maksimal 3% accent (`--accent`, hanya dipakai pada tombol aksi utama dan indikator state aktif). Jangan pernah memakai warna ungu/lavender generik AI (OKLCH hue 270 sampai 330) kecuali diwajibkan oleh logo brand pemilik.
- **Skala spacing:** hanya `4, 8, 12, 16, 24, 32, 48, 64px` (`--s-1` sampai `--s-8`). Batas kiri dan kanan container harus sama rata di setiap viewport.
- **Tipografi dan kontras:** teks isi dan data `14px` sampai `16px` (`line-height: 1.5`, kontras `>= 7:1`), label muted dan metadata `12px` sampai `13px` (`font-weight: 500`, kontras `>= 4.5:1`), lebar bacaan `<= 65ch`, tinggi elemen interaktif `40px` sampai `44px`.
- **Batas bawah dan batas atas (floor & ceiling):** setiap layar menampilkan data domain realistis dari `PRD.md` (5 sampai 8 baris atau item, dilarang `Lorem ipsum`), maksimal 4 kelompok component utama per layar, maksimal 2 tingkat box nesting, dan 0 widget dekoratif yang tidak diminta.

## 3. Design tokens yang dikunci
{{DESIGN_TOKENS}}

## 4. Layout shell dan base components yang dikunci
{{DESIGN_COMPONENTS}}

## 5. Inventaris referensi dan mockup (`references/`)
File disimpan di `references/brand/` (logo, aset brand), `references/inspiration/` (referensi pemilik atau screenshot yang diambil `designer` lewat `agent-browser`), dan `references/mockups/` (`option-1.html`, `option-2.html`, `option-3.html` beserta screenshot browser-nya).

| ID | Path atau URL | Jenis | Apa yang diambil / status |
|---|---|---|---|
{{DESIGN_REFERENCES}}
