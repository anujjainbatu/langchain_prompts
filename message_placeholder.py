from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful Customer Support Agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
#load chat hisrtory
with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())

#create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund?'})

print(prompt)