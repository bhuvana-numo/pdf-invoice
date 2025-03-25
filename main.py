import subprocess

print("Starting Invoice Generation Process...")


print("\n Generating DOCX invoice...")
subprocess.run(["python", "generate-doc.py"])


print("\n Converting DOCX to PDF...")
subprocess.run(["python", "docx-to-pdf.py"])

print("\n Invoice generation complete! PDF is ready.")
