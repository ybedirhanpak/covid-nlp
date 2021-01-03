# Read data from preprocessing step
# term_frequency_doc: dict = utils.unpickle_object(
#     'out/term_frequency_doc.pickle')
# term_frequency_query: dict = utils.unpickle_object(
#     'out/term_frequency_query.pickle')
# document_frequency: dict = utils.unpickle_object(
#     'out/document_frequency.pickle')
# vocabulary: set = utils.unpickle_object('out/vocabulary.pickle')
# inverted_index: dict = utils.unpickle_object('out/inverted_index.pickle')


# vocabulary_list = list(vocabulary)
# document_list = term_frequency_doc.keys()

# vocabulary_size = len(vocabulary_list)
# document_size = len(document_list)

# print("V:", vocabulary_size)
# print("D:", document_size)

# print(sorted(vocabulary_list))

# document_tf = np.array([term_frequency_doc[document][word] if word in term_frequency_doc[document] else 0 for document in document_list for word in vocabulary_list])

# print(document_tf.shape)

# document_vectors = np.array([term_frequency_doc[document][word] for word in vocabulary_list for document in document_list])

# print(document_vectors.shape)

# # Document vectors
# document_vectors = {}

# i = 0

# for id, tf_query in term_frequency_query.items():
#     query_vector = np.array(
#         [tf_query[word] if word in tf_query else 0 for word in vocabulary_list])

#     query_document_set = set()
#     for word, tf in tf_query.items():
#         document_set = inverted_index[word]
#         query_document_set.update(document_set)

#     print("Document count", len(query_document_set))

#     for document in query_document_set:
#         tf_doc = term_frequency_doc[document]

#         # Get document vector
#         if document not in document_vectors:
#             document_vectors[document] = np.array(
#                 [tf_doc[word] if word in tf_doc else 0 for word in vocabulary_list])

#         document_vector = document_vectors[document]

#         # Calculate cosine similarity
#         # cosine_similarity = np.dot(
#         #     query_vector, document_vector) / (norm(query_vector) * norm(document_vector))

#         print(id, ' ', document)

#     i += 1
#     if i >= 1:
#         break