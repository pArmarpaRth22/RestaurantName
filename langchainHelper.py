import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain









def generate_content(cuisine,api_key):
    
    os.environ["GROQ_API_KEY"]=api_key
    
    llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
    )
    
    
    template = ChatPromptTemplate([
    ("system", "You are a helpful assistant that simply suggest something. suggest only one name."),
    ("human", "I want to open resturant for {cuisine} food.Suggest me a fancy name for this."),
    ])
    
    name_chain=LLMChain(llm=llm,prompt=template)
    
    template2 = ChatPromptTemplate([
    ("system", "You are a helpful assistant that simply suggest menu items based on resturant name selected."),
    ("human", "Suggest some menu items for {resturnat_name}."),
    ])
    
    food_Items_chain=LLMChain(llm=llm,prompt=template2)
    
    chain=SimpleSequentialChain(chains=[name_chain,food_Items_chain])
    res=chain.run(cuisine)
    
    return res
    
    
