import csv
import utils
import os
import time


def read_metadata():
    '''
        Preprocesses metadata, creates inverted index and term frequency.
    '''
    print("Preprocessing metadata.csv...")
    start_time = time.time()

    inverted_index = {}
    normalized_documents_unsorted = []
    document_ids_unsorted = []

    with open(utils.get_file_path("data/metadata.csv"), 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        # Skip first line which contains headers
        next(csv_reader)
        for row in csv_reader:
            # Extract document information from row
            doc_id = row[0]
            doc_title = row[3]
            doc_abstract = row[8]

            # Remove punctuation of the document
            doc_content = utils.normalize_doc(
                doc_title + ' ' + doc_abstract)

            normalized_doc = []

            # Preprocess each token in the document
            for token in doc_content.split(" "):
                # Normalize the token
                n_token = utils.normalize_token(token)

                # Skip stopwords
                if utils.is_stopword(n_token):
                    continue

                normalized_doc.append(token)

                # Add document into inverted index
                if n_token not in inverted_index:
                    inverted_index[n_token] = {doc_id}
                elif doc_id not in inverted_index[n_token]:
                    inverted_index[n_token].add(doc_id)

            normalized_documents_unsorted.append(' '.join(normalized_doc))
            document_ids_unsorted.append(doc_id)

    file.close()

    # Sort normalized_documents_unsorted and document_ids_unsorted lists
    id_document_pairs = sorted(
        zip(document_ids_unsorted, normalized_documents_unsorted))

    document_ids, normalized_documents = zip(*id_document_pairs)

    print("Pickle inverted_index, normalized_documents")

    # Create out directory
    if not os.path.exists("out"):
        os.makedirs("out")

    # Picke inverted_index
    utils.pickle_object(inverted_index, "out/inverted_index.pickle")

    # Picke normalized_documents
    utils.pickle_object(normalized_documents,
                        "out/normalized_documents.pickle")

    # Picke document_ids
    utils.pickle_object(document_ids, "out/document_ids.pickle")

    end_time = time.time()

    print('{:.2f} seconds elapsed during metadata preprocessing'.format(
        end_time - start_time))
