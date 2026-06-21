#from ollama import embed, chat
#embeddings = embed(model="custom_deepseek_fake", input=["Here is an example sentence","Here's a second one!"])
#print(len(embeddings['embeddings'][0]))

#response = embed(model="custom_deepseek_fake", messages=[ { 'role' : 'user', 'content': 'Why did the chicken cross the road?' }])
#print(response.message.content)

"""
curl http://localhost:11434/api/embed -d '{
  "model":"embeddinggemma",
  "input":"hello"
}'
"""



from ollama import embed,chat

"""embeddings = embed(
    model="embeddinggemma",
    #input=[ "Here is an example sentence", "Here's a second one!" ]
    input= "hello"
)
#print(embeddings.embeddings)
vector = embeddings.embeddings[0]
print(f"Dimention: {len(vector)}")
print(vector[:2])"""

embeddings = embed(model="deepseek-r1:8b",input=["hello"])
print(len(embeddings['embeddings'][0]))

"""response = chat(model="deepseek-r1:8b", messages=[
    {'role':'user', 'content' : 'Why did the chicken cross the road?'}
])
print(response.message.content)"""
