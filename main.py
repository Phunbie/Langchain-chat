from flask import Flask, render_template, request #, jsonify
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.utilities import PythonREPL
from langchain.utilities import WikipediaAPIWrapper
import openai
#import config
import os


#os.environ['OPENAI_KEY'] = 'sk-'
#get Openapi key
#api_key= config.DevelopmentConfig.OPENAI_KEY
api_key = os.getenv('OPENAI_KEY')
openai.api_key = api_key


#Create tools that will be used

#Duck Duck go search engine
search = DuckDuckGoSearchRun()
Duck=Tool( name = "Current Search",  func=search.run,    description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term.")

#Python repl
python_repl = PythonREPL()
Python = Tool(      name = "python repl",  func=python_repl.run,description="useful for when you need to use python to answer a question. You should input python code")

#Wikipedia
wikipedia = WikipediaAPIWrapper()
wikipedia_tool = Tool(    name='wikipedia',    func= wikipedia.run, description="Useful for when you need to look up a topic, country or person on wikipedia")

# append all tools to tools
tools = []
tools.append(Duck)
tools.append(Python)
tools.append(wikipedia_tool)



#create memory for the chatbot
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# create agent
llm=ChatOpenAI(temperature=0, openai_api_key=api_key)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory, )#return_intermediate_steps=True



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
   ans= agent_chain.run(text)
   try:
     answer = ans.replace('\n', '<br>')
   except:
     answer = "opps no response"
   print(answer)
   return answer
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
