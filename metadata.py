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
    normalized_documents = []
    document_ids = []

    with open(utils.get_file_path("data/metadata.csv"), 'r') as readFile:
        csv_reader = csv.reader(readFile, delimiter=',')

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

            normalized_documents.append(' '.join(normalized_doc))
            document_ids.append(doc_id)

    readFile.close()

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
