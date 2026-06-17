from langchain_community.document_loaders import (
    TextLoader,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings,
)


loader = TextLoader(
    "data/tokyo_guide.md"
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = splitter.split_documents(
    documents
)

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./db/travel",
)