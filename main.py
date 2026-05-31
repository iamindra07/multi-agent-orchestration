from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from google import genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
import os

load_dotenv()
app = FastAPI()
ai = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
client = chromadb.Client()
model = SentenceTransformer("all-MiniLM-L6-v2")
collection = client.create_collection(name="knowledge_base")
class Request(BaseModel):
    question:str

def generator_agent(question:str, context:str):
    prompt = f"""
        please generate relavent asnwer based on the question and the context below:
        
        context:{context}
        
        question:{question}
    """
    answer = ai.models.generate_content(
        model="gemini-3.5-flash",
        contents= prompt
    )
    final_ans = answer.text
    return final_ans

def critic_agent(question:str,context:str, ans:str):
    prompt = f"""
        Check whether this answer is grounded in the context. If weak, improve it.
        question : {question}
    
        context :{context}
    
        answer : {ans}
    """
    critic = ai.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    critic_ans = critic.text
    return critic_ans

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    with open(file.filename,"wb") as f:
        content = await file.read()
        f.write(content)
    reader = PdfReader(file.filename)
    text = ""
    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text
    chunks = text.split(".")
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    embeddings = model.encode(chunks).tolist()
    for i,chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embeddings[i]]
        )
    return{
        "Messege":"File Uploaded Successfully",
        "Total Chunks":len(chunks)
    }
@app.post("/chat")
def chat(req:Request):
    query = req.question
    query_embedding = model.encode([query]).tolist()[0]
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    context = "\n".join(result["documents"][0])
    answer = generator_agent(query,context)
    critic_ans = critic_agent(query,context,answer)
    return{
        "Question":query,
        "Context":context,
        "Answer":answer,
        "Revised Answer":critic_ans
    }
    