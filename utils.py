from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain


def chat(input_message, open_ai_key, memory):
    model = ChatOpenAI(base_url="https://jiekou.wlai.vip/v1", openai_api_key=open_ai_key)
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [MessagesPlaceholder(variable_name="history"), ("human", "{input}")])
    chain = ConversationChain(llm=model, memory=memory, prompt=chat_prompt_template)
    response = chain.invoke({"input": input_message})
    return response["response"]


def initialize(api_key):
    model = ChatOpenAI(
        base_url="https://jiekou.wlai.vip/v1",
        openai_api_key=api_key
    )
    memory = ConversationSummaryBufferMemory(llm=model, max_token_limit=1000, return_messages=True)
    return memory
