import os
import PyPDF2
from embedchain import App

os.environ["OPENAI_API_KEY"] = ''

pdf_bot = App()

# Get pdf text and store it in pdf_text variable
# Initialize the text variable
pdf_text = ""

# Open the PDF file
with open('./documentos/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages
    num_pages = len(pdf_reader.pages)

    # Loop through all the pages and extract text
    for page_num in range(num_pages):
        # Get a page object
        page = pdf_reader.pages[page_num]

        # Extract text from the page
        page_text = page.extract_text()

        # Append the text to pdf_text variable
        pdf_text += page_text
     
# Embed content of pdf document

pdf_bot.add(pdf_text, data_type='text')
#pdf_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")

while True:
    question = input("Enter your question, or 'quit' to stop the program.\n >>")

    if question == 'quit':
        break

    response = pdf_bot.query(question)
    print(f"\n{response}\n")
