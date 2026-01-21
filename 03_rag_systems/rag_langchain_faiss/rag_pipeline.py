"""
RAG Pipeline: LangChain + FAISS + Local LLM

This module implements an end-to-end Retrieval-Augmented Generation (RAG)
pipeline for grounding LLM responses in authoritative healthcare information.

Pipeline stages:
1. Data ingestion (CDC / WHO)
2. Text cleaning and preprocessing
3. Chunking and overlap control
4. Embedding generation
5. FAISS vector store creation / loading
6. Similarity-based retrieval
7. Context-grounded answer generation

"""
import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from transformers import pipeline


# Centralized Configuration

DATA_DIR = "healthcare_docs"
VECTORSTORE_PATH = "faiss_index"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

URL_SOURCES = [
    "https://www.cdc.gov/heart-disease/about/index.html",
    "https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)"
]

PDF_FILES = []  # Optional local PDFs


# Data Ingestion


os.makedirs(DATA_DIR, exist_ok=True)

raw_documents = []
print("Fetching HTML pages...")

for url in URL_SOURCES:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join(soup.get_text(separator=" ").split())

        raw_documents.append(text)
        print(f"Fetched {url} (length: {len(text)} characters)")

    except Exception as e:
        print(f"Error fetching {url}: {e}")


# PDF Parsing (Optional)


print("\nParsing PDF files...")

for pdf_file in PDF_FILES:
    try:
        reader = PdfReader(pdf_file)
        pdf_text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text += page_text + " "

        pdf_text = " ".join(pdf_text.split())

        if pdf_text:
            raw_documents.append(pdf_text)
            print(f"Parsed PDF {pdf_file} (length: {len(pdf_text)} characters)")

    except Exception as e:
        print(f"Error reading {pdf_file}: {e}")


# Fallback for local testing
if not raw_documents:
    print("\nNo external documents found. Using placeholder content.")
    raw_documents = [
        "Chest pain can have many causes, some of which require immediate medical attention.",
        "Cardiovascular diseases affect the heart and blood vessels."
    ]

print(f"\nTotal documents collected: {len(raw_documents)}")

# Chunking Strategy
print("\nSplitting documents into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = []
for doc in raw_documents:
    for chunk_text in text_splitter.split_text(doc):
        chunks.append(Document(page_content=chunk_text))

print(f"Total chunks created: {len(chunks)}")


# Embedding Generation

print("\nCreating embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Sanity check
test_vector = embeddings.embed_query("test")
print(f"Embeddings initialized (vector length: {len(test_vector)})")

# Vector Store Creation / Loading

if os.path.exists(VECTORSTORE_PATH):
    print("\nLoading existing FAISS index...")
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("FAISS vector store loaded")
else:
    print("\nCreating new FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTORSTORE_PATH)
    print("FAISS vector store created and saved")

print(f"Number of vectors in FAISS: {len(vectorstore.docstore._dict)}")

# LLM Initialization (Generation Layer)

print("\nLoading language model for generation...")

generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=150
)

print("Language model loaded.")


# Interactive RAG Loop

print("\nRAG system ready.")
print("Type a healthcare-related question.")
print("Type 'exit' to quit.\n")

while True:
    user_query = input("Enter your query: ").strip()

    if user_query.lower() in {"exit", "quit"}:
        print("Exiting RAG system.")
        break

    if not user_query:
        print("Please enter a non-empty query.\n")
        continue

    print(f"\nRunning similarity search for query: '{user_query}'\n")

    results = vectorstore.similarity_search(user_query, k=3)

    if not results:
        print("No relevant documents found.\n")
        continue

    # Combine retrieved context
    context = "\n\n".join([doc.page_content for doc in results])

    prompt = f"""
You are a healthcare information assistant.
You are NOT a medical professional.
Do NOT provide diagnoses or treatment plans.

Use the following retrieved context to answer the question.
If the context is insufficient, say you do not have enough information.

Context:
{context}

Question:
{user_query}

Answer:
"""

    response = generator(prompt)[0]["generated_text"]

    print("\nGenerated Answer:\n")
    print(response)
    print("\n" + "-" * 60 + "\n")