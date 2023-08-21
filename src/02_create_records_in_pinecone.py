import pandas as pd
import pinecone
from .load_config import load

df = pd.read_csv("data/documents_processed.csv")

pinecone_token = load("config.yaml")["tokens"]["pinecone"]
pinecone_env = load("config.yaml")["parameters"]["pinecone_env"]
pinecone.init(api_key=pinecone_token, environment=pinecone_env)
# create a Pinecone index
try:
    pinecone.create_index("startech", dimension=1536, metric="cosine")
except:
    print("index already exists")

print(pinecone.list_indexes())
index = pinecone.Index("startech")

def create_a_list_from_list_as_string(x):
    ll = x.replace("[", "").replace("]", "").split(",")
    return [float(element) for element in ll] 

df["embeddings_as_list"]= df["embeddings"].apply(create_a_list_from_list_as_string)
# upsert records into the index
records = []
for row in df.iterrows():
    records.append((str(row[1]["index"]), row[1]["embeddings_as_list"]))


index.upsert(records)
