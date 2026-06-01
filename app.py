import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import tempfile

load_dotenv()

# Page config
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 RAG Chatbot")
st.write("Upload a PDF and ask questions about it!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# Sidebar
with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Processing PDF... ⏳"):
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                f.write(uploaded_file.read())
                tmp_path = f.name

            # Load and split
            loader = PyPDFLoader(tmp_path)
            documents = loader.load()
            
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )
            chunks = splitter.split_documents(documents)

            # Embeddings
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            vectorstore = FAISS.from_documents(chunks, embeddings)
            retriever = vectorstore.as_retriever()

            # LLM
            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                temperature=0.5,
                api_key=os.environ["GROQ_API_KEY"]
            )

            # Chain
            prompt = ChatPromptTemplate.from_template("""
            Answer the question based on the context below.
            Context: {context}
            Question: {question}
            Answer:
            """)

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            st.session_state.qa_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

        st.success(f"✅ {len(chunks)} chunks ready!")

# Chat history display
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if question := st.chat_input("Ask a question about your PDF..."):
    if st.session_state.qa_chain is None:
        st.warning("Please upload a PDF first!")
    else:
        # Show user message
        with st.chat_message("user"):
            st.write(question)
        st.session_state.chat_history.append({"role": "user", "content": question})

        # Get answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking... ⏳"):
                answer = st.session_state.qa_chain.invoke(question)
                st.write(answer)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})