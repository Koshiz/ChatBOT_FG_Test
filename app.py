from sentence_transformers import SentenceTransformer
import pinecone
import random
import itertools


sentences = "FolioGrow is smart cannabis cultivation software that helps you make the right decisions to increase your yields and profits"

# pinecone.init(api_key="91e41499-ee04-4431-8ddc-d878f12a62a0", environment="us-west4-gcp-free")

# pinecone.create_index("chatbot", dimension=384, metric="cosine")

# index = pinecone.Index("chatbot")

# pinecone.list_indexes()

model = SentenceTransformer('./all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

#inserting embeddings to a list
embeddings =  embeddings.tolist()

print(embeddings)


#Batching upserts
# def chunks(iterable, batch_size=100):
#     """A helper function to break an iterable into chunks of size batch_size."""
#     it = iter(iterable)
#     chunk = tuple(itertools.islice(it, batch_size))
#     while chunk:
#         yield chunk
#         chunk = tuple(itertools.islice(it, batch_size))

# vector_dim = 384
# vector_count = 10000

# # Example generator that generates many (id, vector) pairs
# example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

# Upsert data with 100 vectors per upsert request
# for ids_vectors_chunk in chunks(example_data_generator, batch_size=100):
#     index.upsert(vectors=ids_vectors_chunk)  

# query_sentence = "Foliogrow"
# query_embedding = model.encode([query_sentence])

# K = 10  # Number of nearest neighbors to retrieve

# # Iterate over each vector in the index
# for vector in ids_vectors_chunk:
#     # Perform a nearest neighbor search for the current vector
#     results = index.query(queries=[vector], top_k=K)
    
#     # Retrieve the nearest neighbor IDs and distances
#     neighbor_ids = results.ids[0]
#     neighbor_distances = results.distances[0]
    
#     # Process the nearest neighbor results as needed
#     # ...

# nearest_sentences = index.retrieve(ids=neighbor_ids)

# for sentence, distance in zip(nearest_sentences, neighbor_distances):
#     print(f"Sentence: {sentence}, Distance: {distance}")

# pinecone.deinit()




# print(embeddings)
# print(len(embeddings[0]))
