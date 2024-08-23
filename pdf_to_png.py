import fitz  # PyMuPDF
from PIL import Image
def pdf_to_jpg(pdf_path, output_folder):
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)
    
    # Iterar sobre cada página do PDF
    for page_num in range(len(pdf_document)):
        # Obter a página atual
        page = pdf_document.load_page(page_num)
        
        # Converter a página para imagem
        image = page.get_pixmap()
        
        # Criar objeto de imagem usando Pillow
        img = Image.frombytes("RGB", [image.width, image.height], image.samples)
        
        # Salvar a imagem como JPEG numerado com qualidade máxima
        image_path = f"{output_folder}/page_{page_num + 1}.jpg"
        img.save(image_path, "JPEG", quality=95)  # Ajustar a qualidade conforme necessário
        
        print(f"Página {page_num + 1} convertida e salva como {image_path}")
    
    # Fechar o arquivo PDF
    pdf_document.close()

# Exemplo de uso
pdf_file = "endereçopdf.pdf"
output_folder = "./endereçodesaida"

pdf_to_jpg(pdf_file, output_folder)
