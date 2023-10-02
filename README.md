Document-based QA with LLaMa 2.
Download the LLaMa 2 model from the following link: https://drive.google.com/file/d/1km9TfoZ5Kl75L4SUEmdPgG6vWNvOnA0i/view?usp=sharing

Place the model (.bin) in models folder.

This project was an assignment for a recruitment test. The task was to create a Retrieval Augmented Generation (RAG) chatbot capable of answering user questions using information from a knowledge document. The architecture employs CTransformers for bindings (for transformer models), Langchain for extensive integration, sentence-transformers for embedding representations and Facebook AI Similarity Search (FAISS) for efficient similarity search and clustering of dense vectors (Embeddings).

There was an attempt to prevent the RAG from generating false information (hallucination) and ensure it provided accurate answers. 

The approach to this problem was to :

- Section the reference document into chunks and generate embeddings for them. 
- Generate embeddings for queries (via sentence-transformer, sbert)
- Storing generated embeddings in a vectordb, and using FAISS for efficient similarity search and indexing.
- Finally, use the closest context found via FAISS to the query and input to the LLM (Meta’s LLaMa v2 in this case). 
- A preemptive negative prompt discouraging hallucination and enforcing strict adherence to Question/Answer format also helps discourage hallucinations.


![Aspose Words 2cf35b86-9c18-4351-a98d-63a2f01d7493 001](https://github.com/Just-A-Dash/RAGwithLLAMAv2/assets/10814164/c48a87b3-a144-435e-bf8f-c363364f1a41)



The code consists mainly of the following parts:



1. db\_build.py – Preprocessing data and building the vector store.
- The vector store will be generated and saved in the local directory named 'vectorstore/db\_faiss'
- This will be the main db for semantic search and other operations.

2. prompts.py – Set up a template to prevent hallucination and reinforce question/answer format

- LLaMaV2 wasn’t my first choice, compared to GPT, but it is available to run offline.
- LLaMa, unlike GPT isn’t set up for Conversational Prompt-In Answer-Out, hence the need for this.

3. Models – Use the LLaMaV2 .bin, quantized to have 8-bit parameter values to reduce computational overhead. You can use 4/5/6 bit quantized bins as well, but the performance drops are significant.

4. llm.py – Construct LLM object (Langchain provided ctransformers wrapper for LLaMa)

- Wrapper allows for a simplified consistent interface to interact with the LLaMa.bin model.

5. utils.py – Enables performing document querying, broadly does the following:

  - Make a template for prompts in the form of [context, prompted\_question]
  - Define an object that will be used for searching vector store
  - Instantiate the objects.




