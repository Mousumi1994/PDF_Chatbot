import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

os.environ["OPENROUTER_API_KEY"] = "Your API Key"

def load_and_preprocess_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, separators=["\n\n", "\n", ".", " "] ) # try to split at logical places
    chunks = splitter.split_documents(documents)
    return chunks


def create_or_load_vector_store(chunks=None):

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",  # or whatever model OpenRouter supports
        openai_api_key=os.environ["OPENROUTER_API_KEY"],
        openai_api_base="https://openrouter.ai/api/v1"
    )

    db = Chroma.from_documents(documents=chunks, embedding=embedding_model)
    return db


def answer_question(db, question: str):
    # Step 1: Search the most relevant document chunks
    results = db.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in results])
    # Step 2: Create a clear prompt with the context and question
    prompt_template = """
        Use ONLY the information in the context to answer the question.
        Do not make anything up or include external knowledge.
        Context:
        {context}
        Question:
        {question}
        Answer:
        """
    prompt = PromptTemplate.from_template(prompt_template).format(
        context=context,
        question=question
    )
    # Step 3: Send prompt to LLM
    model = ChatOpenAI(model="openai/gpt-oss-120b:free", api_key=os.environ["OPENROUTER_API_KEY"], base_url="https://openrouter.ai/api/v1",temperature=0, max_tokens=500) 
    response = model.invoke(prompt)
    return response.content

def main():
    pdf_path = "pythonlearn.pdf"

    print("Loading and processing PDF...")
    chunks = load_and_preprocess_pdf(pdf_path)

    print("Creating/loading vector store...")
    vectorstore = create_or_load_vector_store(chunks)

    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        try:
            answer = answer_question(vectorstore, query)
            print(answer)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
