 # LLM-LangChain Project

## Overview
This project demonstrates how to use **LangChain** with **LLMs (Large Language Models)** to interact with AI models like OpenAIs GPT and Googles Gemini. It includes different **prompt templates**, **chains**, and integration with **e-commerce-related queries**.

## Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)
- OpenAI API key (if using OpenAI models)
- Google Gemini API key (if using Gemini models)

### Installation
Clone the repository and install the required dependencies:
```sh
# Clone the repository
git clone https://github.com/ChinmayBhattt/LLM-LangChain.git
cd LLM-LangChain

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scriptsctivate  # For Windows

# Install dependencies
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root and add your API keys:
```sh
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

## Usage

### 1️⃣ Find the Capital of a City
```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

def get_capital(place):
    prompt = PromptTemplate.from_template("What is the capital of {place}?")
    llm = OpenAI(temperature=0.3)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(place)

print(get_capital("India"))
```

### 2️⃣ Get E-Commerce Store from Product Name
```python
prompt = PromptTemplate.from_template("What is the name of the e-commerce store that sells {product}?")
llm = OpenAI(temperature=0.3)
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("iPhone"))
```

### 3️⃣ Get Products from an E-Commerce Store
```python
prompt = PromptTemplate.from_template("What are the names of the products at {store}?")
llm = OpenAI(temperature=0.3)
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("Amazon"))
```

## Contributing
Feel free to contribute by opening issues or submitting pull requests!

## License
This project is licensed under the MIT License.


