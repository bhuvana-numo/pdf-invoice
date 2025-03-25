from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
import os

SCOPES = ["https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

def upload_docx(file_path):
    """Uploads DOCX to Google Drive and returns file ID."""
    service = build("drive", "v3", credentials=CREDS)
    file_metadata = {"name": os.path.basename(file_path), "mimeType": "application/vnd.google-apps.document"}
    media = MediaFileUpload(file_path, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    return uploaded_file.get("id")

def convert_to_pdf(file_id, output_pdf_path):
    """Converts Google Docs file to PDF and downloads it."""
    service = build("drive", "v3", credentials=CREDS)
    request = service.files().export_media(fileId=file_id, mimeType="application/pdf")
    with open(output_pdf_path, "wb") as pdf_file:
        pdf_file.write(request.execute())
    print(f" PDF saved: {output_pdf_path}")

def docx_to_pdf(docx_path, pdf_output_path):
    """Uploads DOCX, converts to PDF, and downloads it."""
    file_id = upload_docx(docx_path)
    convert_to_pdf(file_id, pdf_output_path)

if __name__ == "__main__":
    FILLED_DOCX = "filled_invoice.docx"
    PDF_OUTPUT = "invoice.pdf"
    docx_to_pdf(FILLED_DOCX, PDF_OUTPUT)
