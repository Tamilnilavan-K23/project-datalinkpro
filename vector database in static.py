#installing and importing the required lllm model and library
import json
import os
#import pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from InstructorEmbedding import INSTRUCTOR
from langchain.chains.question_answering import load_qa_chain
import os
from pinecone import Pinecone
from dotenv import load_dotenv

import json

import json

def read_json_file(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        documents = json.load(file)

    # Initialize an empty string to store the concatenated text
    all_texts = []

    # Check if documents is a list (i.e., multiple documents)
    if isinstance(documents, list):
        for doc in documents:
            # Convert each document to a string format
            if isinstance(doc, dict):
                text = (
                    f"Employee ID: {str(doc.get('employee_id', 'N/A'))}\n"
                    f"Name: {doc.get('name', 'N/A')}\n"
                    f"Gender: {doc.get('gender', 'N/A')}\n"
                    f"Date of Birth: {str(doc.get('date_of_birth', 'N/A'))}\n"
                    f"Marital Status: {doc.get('marital_status', 'N/A')}\n"
                    f"Nationality: {doc.get('nationality', 'N/A')}\n"
                    f"Address: {doc.get('address', 'N/A')}\n"
                    f"Contact Number: {doc.get('contact_number', 'N/A')}\n"
                    f"Email: {doc.get('email', 'N/A')}\n"
                    f"Department: {doc.get('department', 'N/A')}\n"
                    f"Job Title: {doc.get('job_title', 'N/A')}\n"
                    f"Date of Hire: {str(doc.get('date_of_hire', 'N/A'))}\n"
                    f"Employment Type: {doc.get('employment_type', 'N/A')}\n"
                    f"Work Location: {doc.get('work_location', 'N/A')}\n"
                    f"Supervisor: {doc.get('supervisor', 'N/A')}\n"
                    f"Work Authorization: {doc.get('work_authorization', 'N/A')}\n"
                    f"Background Check: {doc.get('background_check', 'N/A')}\n"
                    f"Employment Agreement: {doc.get('employment_agreement', 'N/A')}\n"
                    f"Education: {doc.get('education', 'N/A')}\n"
                    f"Certifications: {', '.join(doc.get('certifications', []))}\n"
                    f"Previous Experience: {', '.join(doc.get('previous_experience', []))}\n"
                    f"References: {', '.join(doc.get('references', []))}\n"
                    f"Salary: ${doc.get('salary', 'N/A')}\n"
                    f"Bonus: ${doc.get('bonus', 'N/A')}\n"
                    f"Commission: ${doc.get('commission', 'N/A')}\n"
                    f"Total Working Days: {doc.get('total_working_days', 'N/A')}\n"
                    f"Total Worked Days: {doc.get('total_worked_days', 'N/A')}\n"
                    f"Leaves Taken: {', '.join([f'{month}: {len(days)} days' for month, days in doc.get('leaves_taken', {}).items()])}\n"
                    f"---\n"
                )
                all_texts.append(text)

    # Combine all document strings into a single string
    combined_text = '\n'.join(all_texts)

    return combined_text



file_path = "/content/employee_data.json"
documents= read_json_file(file_path)
from google.colab import userdata
userdata.get("HUGGINGFACE_API_KEY")
userdata.get("PINECONE_API_KEY")
#api_key=os.getenv("HUGGINGFACE_API_KEY")
#os.environ["PINECONE_API_KEY"] ="PINECONE_API_KEY"
def get_text_chunk(document):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    text_chunks = text_splitter.split_text(document)
    print(f"Number of text chunks: {len(text_chunks)}")
    print(text_chunks)
    return text_chunks

#converting the JSON file into single string ,converting the single string into text chuncks
text_chunks = get_text_chunk(documents)
# Set up the embeddings
embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl')
embeddings
def get_vectorstore(text_chunks):

    index_name = "llm23"
    pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

    index = pc.Index(host='https://llm3-g9ak0ib.svc.aped-4627-b74a.pinecone.io')

    # Convert text chunks to embeddings and flatten the list
    vector_embeddings = [embeddings.embed_documents(text)[0] for text in text_chunks] # Flatten the list of lists

    # Create upsert payload, use string ids
    upsert_payload = [(str(i), vector_embeddings[i]) for i in range(len(text_chunks))]
    print(upsert_payload)

    # Upsert (insert) the vectors into the Pinecone index
    index.upsert(vectors=upsert_payload)
    return index

#Embedding the chunks of data into vector database
vectorstore = get_vectorstore(text_chunks)
print(documents)
##cosine similarity retreive Results from VectorDB
def retreive_results(query,k=2):
  matching_results=vectorstore.similarity_search(query,k=k)
  return matching_results

from langchain.llms import HuggingFaceHub
from langchain.chains.question_answering
