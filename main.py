# LLM (Large Language Model)
import openai 
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def practise():
   prompt = PromptTemplate.from_template("What is the capital of {place}?") 
   llm = OpenAI(temperature=0.3)
   chain = LLMChain(llm=llm, prompt=prompt)
   for city in cities:
     output = chain.run(city)
     print(output)
     


#  LLM to get name of an e commerce store from a product name
prompt = PromptTemplate.from_template("What is the name of the e commerce store that sells {product}")

product = "iphone"
output = chain.run(product)
print(output)

#  LLM to get comma sepereted name of products an e commerce store name 
prompt = PromptTemplate.from_template("What are the names of the products at {store}")
llm = OpenAI(temperature=0.3)
chain2 = LLMChain(llm=llm, prompt=prompt)
# store = "Amazon"
# output = chain.run(store)
# print(output)

#  create a overall chain from simple sequential chain
chain = SimpleSequentialChain(chains=[chain, chain2], verbose=True)

output = chain.run("candles")
print(output)

    # cities = ["New York City", "Los Angeles", "Chicago", "Houston", 
  
    # cities = [
    #   "New York City",
    #   "Los Angeles",
    #   "Chicago",
    #   "Houston",
    #   "Phoenix",
    # ]
    
    # prompt = PromptTemplate.from_template("What is the capital of {place}?") 
    # llm = OpenAI(temperature=0.3)
    # chain = LLMChain(llm=llm, prompt=prompt)
    
    # for city in cities:
    #   output = chain.run(city)
    #   print(output)
    
