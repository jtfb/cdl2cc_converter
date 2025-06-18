# 🎬 CDL to CC Converter

A simple Python tool to convert `.cdl` (Color Decision List) files to `.cc` (Color Correction) format, following ASC CDL XML schema standards.

This is useful in color pipelines, VFX workflows, or post-production processes that require `.cc` instead of `.cdl` files.

---

## 📦 Features

- ✅ Converts all `.cdl` files in a folder to `.cc`
- ✅ Supports multiple `<ColorCorrection>` blocks per file
- ✅ Outputs clean, individual `.cc` files using the correction ID
- ✅ Creates a `converted_cc` subfolder automatically
- ✅ Pure Python — no extra libraries required

---

## 📂 Example Input/Output

**Input Folder:**

/project_folder/
├── look1.cdl
├── look2.cdl


**Output Folder:**

/project_folder/converted_cc/
├── look1.cc
├── look2.cc

** How to run the script **

python convert_cdl.py /path/to/your/folder

** How It Works **

Parses .cdl using xml.etree.ElementTree

Extracts each <ColorCorrection> block

Writes a clean .cc file per block

Appends the correction id to the filename if multiple corrections are found