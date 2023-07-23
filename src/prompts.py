# Make sure to follow the exact spacing and indentation in the prompt template for Llama-2-7B-Chat. 
# It's sensitive to changes in whitespace! 
# Incorrect spacing might cause issues in generating a summary from the provided context.

qa_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
