# PDF to JPG Converter

>Este script converte cada página de um arquivo PDF em uma imagem JPG de alta qualidade, utilizando as bibliotecas PyMuPDF (fitz) e Pillow.

## Requisitos
> Certifique-se de que você tem as seguintes bibliotecas instaladas antes de executar o script:

- PyMuPDF (fitz): Para manipulação de arquivos PDF.

- Pillow: Para manipulação de imagens.
Você pode instalar as dependências necessárias usando pip:

> Abra o terminal e digite:
```bash
> pip install PyMuPDF Pillow
```
## Como Usar
- Clone ou faça o download do repositório:

```bash
> git clone git@github.com:Kuhaiku/Pdf-to-PNG.git 

> cd seu-repositorio`
```
1. Coloque o arquivo PDF que deseja converter na pasta do projeto.

2. Edite o script pdf_to_jpg.py para ajustar o caminho do PDF e o diretório de saída:

```python
# Exemplo de uso
pdf_file = "endereçopdf.pdf"
# Caminho para o seu arquivo PDF
output_folder = "./endereçodesaida"  
# Pasta onde as imagens serão salvas
```
#### Execute o script:
```bash
> python pdf_to_jpg.py
```

#### Resultado:

Cada página do PDF será convertida em uma imagem JPG e salva na pasta especificada. As imagens serão nomeadas como page_1.jpg, page_2.jpg, etc.

Durante o processo, mensagens serão exibidas no terminal indicando o progresso da conversão.

## Personalização
Qualidade da imagem: A qualidade da imagem gerada pode ser ajustada no parâmetro quality dentro da função img.save. O valor padrão é 95.
Exemplo de Uso
Aqui está um exemplo de como o script pode ser configurado e executado:

```python
# Exemplo de uso
pdf_file = "meu_arquivo.pdf"
output_folder = "./imagens"
pdf_to_jpg(pdf_file, output_folder)
```
Após a execução, todas as páginas do **meu_arquivo.pdf** serão convertidas para imagens JPG e salvas na pasta imagens.

#### Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra um pull request ou reporte um problema.