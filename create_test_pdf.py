from fpdf import FPDF
import os

# Testtext für die PDF
text = """Protokoll vom März-Meeting

Projekt X wurde im Zusammenhang mit der Budgetplanung für Q2 diskutiert.
Vorgeschlagen wurde, die Mittel umzuverteilen, um Personalressourcen effizienter einzusetzen.
Ein weiteres Meeting dazu ist für April angesetzt.
"""

# Zielordner vorbereiten
output_dir = "data/uploads"
os.makedirs(output_dir, exist_ok=True)

# PDF erstellen
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

for line in text.split("\n"):
    pdf.multi_cell(0, 10, line, new_x="LMARGIN", new_y="NEXT")

# PDF speichern
pdf_path = os.path.join(output_dir, "test.pdf")
pdf.output(pdf_path)

print("✅ Test-PDF wurde erstellt unter:", pdf_path)
