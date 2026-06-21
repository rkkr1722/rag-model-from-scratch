**Useful Links**
- https://github.com/ollama/ollama-python
- https://ollama.com/library/qwen3.6
- wikkipedia - free encyclopediya

# Tokenization
**Tokenization** : Tokenization is the process of breaking words into the smallest segments that still have meaning.

#  embedding
An embedding is a way to convert text (or images, audio, etc.) into a list of numbers (a vector) that captures its meaning.

**Why do we need embeddings?**
Computers don't naturally understand meaning. They only work with numbers.
Embeddings transform text into numbers so that similar meanings end up close together in vector space.

For example:
Text	Meaning
"hello"	greeting
"hi"	greeting
"good morning"	greeting
"car"	vehicle

The embeddings for "hello" and "hi" will be closer to each other than "hello" and "car".

**Simple analogy - embedding**

`Imagine every sentence is a point on a huge map.
          vehicle
             *
             |
             | 
             |
 greeting *--* hello
             *
             hi`

**Your current flow**

```
text
  ↓
embed()
  ↓
vector
  ↓
store in vector DB
  ↓
similarity search
  ↓
retrieve relevant chunks
  ↓
send chunks to LLM
  ↓
answer
```
   
# LLM & Data

**Query: "why did the chicken cross the road ?"**
             |     |
             | LLM | (guessing most likely to next word)
             |     |
"why did the chicken cross the road ? The"
"why did the chicken cross the road ? The chicken"
"why did the chicken cross the road ? The chiken cross"

```
(py3_env) user@lab:~/Documents/rag-model-from-scratch$ ollama create custom_deepseek -f ModelFile 
pulling f64cd5418e4b 100% ▕███████████████████████████████████████████████████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success 
using existing layer sha256:e6a7edc1a4d7d9b2de136a221a57336b76316cfe53a252aeba814496c5ae439d 
using existing layer sha256:c5ad996bda6eed4df6e3b605a9869647624851ac248209d22fd5e2c0cc1121d3 
using existing layer sha256:6e4c38e1172f42fdbff13edf9a7a017679fb82b0fde415a3e8b3c31c6ed4a4e4 
creating new layer sha256:20e1276690c5572a432262c39e626edbcc5429280a3e234284344bb7fee0dadb 
writing manifest 
success 
(py3_env) user@lab:~/Documents/rag-model-from-scratch$ source py3_env/bin/activate
(py3_env) user@lab:~/Documents/rag-model-from-scratch$ pip install ollama
Collecting ollama
  Downloading ollama-0.6.2-py3-none-any.whl.metadata (5.8 kB)
Collecting httpx>=0.27 (from ollama)
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting pydantic>=2.9 (from ollama)
  Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.4/109.4 kB 5.1 MB/s eta 0:00:00
Collecting anyio (from httpx>=0.27->ollama)
  Downloading anyio-4.14.0-py3-none-any.whl.metadata (4.6 kB)
Collecting certifi (from httpx>=0.27->ollama)
  Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx>=0.27->ollama)
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx>=0.27->ollama)
  Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.27->ollama)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.9->ollama)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.4 (from pydantic>=2.9->ollama)
  Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: typing-extensions>=4.14.1 in ./py3_env/lib/python3.12/site-packages (from pydantic>=2.9->ollama) (4.15.0)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.9->ollama)
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Downloading ollama-0.6.2-py3-none-any.whl (15 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 6.1 MB/s eta 0:00:00
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 5.2 MB/s eta 0:00:00
Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 472.3/472.3 kB 9.9 MB/s eta 0:00:00
Downloading pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 14.8 MB/s eta 0:00:00
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading anyio-4.14.0-py3-none-any.whl (123 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.5/123.5 kB 10.6 MB/s eta 0:00:00
Downloading idna-3.18-py3-none-any.whl (65 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.5/65.5 kB 5.5 MB/s eta 0:00:00
Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 10.4 MB/s eta 0:00:00
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Installing collected packages: typing-inspection, pydantic-core, idna, h11, certifi, annotated-types, pydantic, httpcore, anyio, httpx, ollama
Successfully installed annotated-types-0.7.0 anyio-4.14.0 certifi-2026.6.17 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.18 ollama-0.6.2 pydantic-2.13.4 pydantic-core-2.46.4 typing-inspection-0.4.2


#curl http://localhost:11434/api/tags


#curl http://localhost:11434/api/generate -d '{
  "model":"deepseek-r1:8b",
  "prompt":"hello"
}'
************************
for m in $(ollama list | awk 'NR>1 {print $1}'); do
    echo "=== $m ==="
    ollama show --modelfile "$m" | grep "^FROM"
done
=== embeddinggemma:latest ===
FROM /home/user/.ollama/models/blobs/sha256-0800cbac9c2064dde519420e75e512a83cb360de3ad5df176185dc69652fc515
=== custom_deepseek_fake:latest ===
FROM /home/user/.ollama/models/blobs/sha256-e6a7edc1a4d7d9b2de136a221a57336b76316cfe53a252aeba814496c5ae439d
=== deepseek-r1:8b ===
FROM /home/user/.ollama/models/blobs/sha256-e6a7edc1a4d7d9b2de136a221a57336b76316cfe53a252aeba814496c5ae439d
************************
(py3_env) user@lab:~/Documents/rag-model-from-scratch$ ollama list
NAME                           ID              SIZE      MODIFIED       
embeddinggemma:latest          85462619ee72    621 MB    7 minutes ago     
custom_deepseek_fake:latest    6e3507269348    5.2 GB    10 minutes ago    
deepseek-r1:8b                 6995872bfe4c    5.2 GB    28 minutes ago    
(py3_env) user@lab:~/Documents/rag-model-from-scratch$ ollama show --modelfile deepseek-r1:8b| grep "^FROM"
FROM /home/user/.ollama/models/blobs/sha256-e6a7edc1a4d7d9b2de136a221a57336b76316cfe53a252aeba814496c5ae439d
```

```
import requests
def search_wiki(query, limit=20):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": limit
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return [item["title"] for item in r.json()["query"]["search"]]
```