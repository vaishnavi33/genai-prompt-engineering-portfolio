import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# ---------------- Configuration ----------------
DATA_DIR = "healthcare_docs"        # Folder for PDFs or cached HTML
VECTORSTORE_PATH = "faiss_index"    # FAISS index storage
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# URLs and local PDFs to process
urls = [
    "https://www.cdc.gov/heart-disease/about/index.html",
    "https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)"
]

pdf_files = []

os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- Step 1: Fetch HTML ----------------
documents = []
print("Fetching HTML pages...")
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join(soup.get_text(separator=" ").split())
        documents.append(text)
        print(f"Fetched {url} (length: {len(text)} characters)")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# ---------------- Step 2: Parse PDFs ----------------
print("\nParsing PDF files...")
for pdf_file in pdf_files:
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
        text = " ".join(text.split())
        if text:
            documents.append(text)
            print(f"Parsed PDF {pdf_file} (length: {len(text)} characters)")
    except Exception as e:
        print(f"Error reading {pdf_file}: {e}")

# Fallback placeholder if no documents found
if len(documents) == 0:
    print("\nNo documents found. Using placeholder text for testing.")
    documents = [
        "Chest pain can have various causes, some of which require immediate medical attention.",
        "Fatigue may be caused by lifestyle factors, stress, or underlying health conditions."
    ]

print(f"\nTotal documents collected: {len(documents)}")

# ---------------- Step 3: Split into chunks ----------------
print("\nSplitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = []
for doc in documents:
    for chunk_text in text_splitter.split_text(doc):
        chunks.append(Document(page_content=chunk_text))

print(f"Total chunks created: {len(chunks)}")

# ---------------- Step 4: Create embeddings ----------------
print("\nCreating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Quick test
try:
    test_vector = embeddings.embed_query("test")
    print(f"Embeddings working (vector length: {len(test_vector)})")
except Exception as e:
    print(f"Embeddings failed: {e}")

# ---------------- Step 5: Build or load FAISS ----------------
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

# ---------------- Step 6: Test retrieval ----------------
query = "What should I do if I experience chest discomfort?"
print(f"\nRunning similarity search for query: '{query}'")
results = vectorstore.similarity_search(query, k=3)

if not results:
    print("No results found. Check documents and embeddings.")
else:
    print("\nTop retrieved documents:")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r.page_content[:500]}...\n")  # Show first 500 chars
