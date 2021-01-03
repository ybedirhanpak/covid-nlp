import utils
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

start_time = time.time()

print("Unpickle files...")

normalized_documents: list = utils.unpickle_object(
    'out/normalized_documents.pickle')
normalized_queries: list = utils.unpickle_object(
    'out/normalized_queries.pickle')

document_ids: list = utils.unpickle_object(
    'out/document_ids.pickle')
query_ids: list = utils.unpickle_object(
    'out/query_ids.pickle')

vectorizer = TfidfVectorizer()

docs_tf_idf = vectorizer.fit_transform(normalized_documents)
queries_tf_idf = vectorizer.transform(normalized_queries)

print("Docs", docs_tf_idf.shape)
print("Queries", queries_tf_idf.shape)

print("Calculating cosine similarities...")

cosine_similarities = cosine_similarity(queries_tf_idf, docs_tf_idf)

print("Cosine similarity matrix is calculated.\nPrinting out to out/cosine_similarities.txt...")

with open(utils.get_file_path("out/cosine_similarities.txt"), 'w') as f:
    for q_index, doc_row in enumerate(cosine_similarities):
        for d_index, d_score in enumerate(doc_row):
            print(
                f'{query_ids[q_index]} {document_ids[d_index]} {d_score}', file=f)

end_time = time.time()

print("Finished.")

print('{:.2f} seconds elapsed during vectorization and cosine similarity calculations'.format(
    end_time - start_time))