from PyPDF2 import PdfReader
from io import BytesIO


class ResumeService:
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> str:
        """Extract text from PDF file"""
        try:
            pdf_reader = PdfReader(BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text.strip()
        except Exception as e:
            raise ValueError(f"Failed to extract PDF text: {str(e)}")
    
    @staticmethod
    def validate_resume_text(text: str) -> bool:
        """Validate that extracted text is meaningful"""
        return len(text.strip()) > 50


resume_service = ResumeService()
