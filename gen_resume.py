from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_resume(summary):
    filename = "KundanResume.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=10, bottomMargin= 2)
    styles = getSampleStyleSheet()
    
    # Define custom styles
    title_style = ParagraphStyle('TitleStyle', fontSize=16, fontName='Helvetica-Bold', alignment=TA_CENTER, spaceAfter=12)
    header_style = ParagraphStyle('HeaderStyle', fontSize=11, fontName='Helvetica-Bold', spaceAfter=4, textColor=colors.black)
    subheader_style = ParagraphStyle('SubHeaderStyle', fontSize=10, fontName='Helvetica-Bold', spaceAfter=2)
    body_style = ParagraphStyle('BodyStyle', fontSize=8, leading=8, spaceAfter=6, alignment=TA_LEFT, keepWithNext=True)
    bullet_style = ParagraphStyle('BulletStyle', fontSize=8, leading=8, leftIndent=20, bulletIndent=8, spaceAfter=4, alignment=TA_LEFT, keepWithNext=True)
    
    elements = []
    
    # Header Section (Name and Contact Info)
    elements.append(Paragraph("SAI KUNDAN SUDDAPALLI", title_style))
    # elements.append(Paragraph("Atlanta, Georgia, USA", body_style))
    elements.append(Paragraph("☎ 706-300-2779 ✉ kundan16@hotmail.com 🌐 linkedin.com/in/saikundan github.com/Ironman20121",ParagraphStyle('BodyStyle', fontSize=10, leading=14, spaceAfter=6, alignment=TA_CENTER, keepWithNext=True) ))
    elements.append(Spacer(1, 12))
    
    # Summary Section
    elements.append(Paragraph("SUMMARY", header_style))
    summary_text =summary
    elements.append(KeepTogether(Paragraph(summary_text, body_style)))
    elements.append(Spacer(1, 12))
    
    # Education Section
    elements.append(Paragraph("EDUCATION", header_style))
    elements.append(Paragraph("University of North Georgia", subheader_style))
    elements.append(Paragraph("M.S. in Computer Science (GPA: 4.0/4.0)", body_style))
    elements.append(Paragraph("Jan 2024 - Dec 2024", body_style))
    elements.append(Spacer(1, 12))
    
    # Experience Section
    elements.append(Paragraph("EXPERIENCE", header_style))
    
    elements.append(Paragraph("Graduate Research Assistant", subheader_style))
    elements.append(Paragraph("University of North Georgia", body_style))
    elements.append(Paragraph("May 2024 – Dec 2024", body_style))
    elements.append(Paragraph("• Contributed to the development of an advanced version of the CrystaLLM library, focusing on interpretability and explainability.", bullet_style))
    elements.append(Paragraph("• Utilized LoRA to fine-tune existing open-source LLM models for specific chemical tasks.", bullet_style))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph("C++ & Python Developer", subheader_style))
    elements.append(Paragraph("Tata Consultancy Services", body_style))
    elements.append(Paragraph("Nov 2021 – Nov 2023", body_style))
    elements.append(Paragraph("• Developed and customized a trading platform for a BFSI sector client, ensuring high efficiency and scalability.", bullet_style))
    elements.append(Paragraph("• Engineered a low-latency Info Feed for alpha clients, surpassing performance benchmarks.", bullet_style))
    elements.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(elements)
    print(f"Resume saved ")

