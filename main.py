from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    largo = 11
    for i in range(0, 28):
        largo = largo + 10
        pdf.line(10, largo, 200, largo)

    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        largo = 11
        for i in range(0, 28):
            largo = largo + 10
            pdf.line(10, largo, 200, largo)

        pdf.ln(279)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")



