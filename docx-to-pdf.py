from googleapiclient.discovery import build
from dotenv import load_dotenv
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
import os

SCOPES = ['https://www.googleapis.com/auth/drive']
load_dotenv()

# Get credentials path from environment variable
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not SERVICE_ACCOUNT_FILE:
    raise Exception("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")



creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

def upload_docx(file_path):
    """Uploads DOCX file to Google Drive."""
    file_metadata = {
        'name': 'Invoice',
        'mimeType': 'application/vnd.google-apps.document'
    }
    media = MediaFileUpload(file_path, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded DOCX File ID: {file.get('id')}")
    return file.get('id')

def export_pdf(file_id, output_path):
    """Exports Google Docs file as a PDF."""
    request = drive_service.files().export_media(fileId=file_id, mimeType='application/pdf')
    with open(output_path, 'wb') as f:
        f.write(request.execute())
    print(f"PDF saved as {output_path}")

docx_file_id = upload_docx("invoice_filled.docx")
export_pdf(docx_file_id, "invoice_filled.pdf")
