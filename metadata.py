import csv
import pickle
import utils
import os
import time


def read_metadata(vocabulary: set):
    '''
        Preprocesses metadata, creates inverted index and term frequency.
        Updates vocabulary.
    '''
    print("Preprocessing metadata.csv...")
    start_time = time.time()

    term_frequency_doc = {}
    inverted_index = {}
    document_frequency = {}

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
            doc_content = utils.remove_punctuation(
                doc_title + ' ' + doc_abstract)

            # Term frequency in this document
            doc_term_frequency = {}

            # Preprocess each token in the document
            for token in doc_content.split(" "):
                # Normalize the token
                n_token = utils.normalize_token(token)

                # Skip stopwords
                if utils.is_stopword(n_token):
                    continue

                # Add token to term frequency
                if n_token not in doc_term_frequency:
                    doc_term_frequency[n_token] = 1
                else:
                    doc_term_frequency[n_token] += 1

                # Add document into inverted index
                if n_token not in inverted_index:
                    inverted_index[n_token] = {doc_id}
                elif doc_id not in inverted_index[n_token]:
                    inverted_index[n_token].add(doc_id)
                    # Increase document frequency of token
                    if n_token not in document_frequency:
                        document_frequency[n_token] = 1
                    else:
                        document_frequency[n_token] += 1

                # Add token to vocabulary
                vocabulary.add(n_token)

            term_frequency_doc[doc_id] = doc_term_frequency

    readFile.close()

    print("Pickle term_frequency_doc, document_frequency, inverted_index")

    # Create out directory
    if not os.path.exists("out"):
        os.makedirs("out")

    # Pickle term_frequency_doc
    with open(utils.get_file_path("out/term_frequency_doc.pickle"), 'wb') as file:
        pickle.dump(term_frequency_doc, file, protocol=pickle.HIGHEST_PROTOCOL)

    # Picke inverted_index
    with open(utils.get_file_path("out/inverted_index.pickle"), 'wb') as file:
        pickle.dump(inverted_index, file, protocol=pickle.HIGHEST_PROTOCOL)

    # Picke document_frequency
    with open(utils.get_file_path("out/document_frequency.pickle"), 'wb') as file:
        pickle.dump(document_frequency, file, protocol=pickle.HIGHEST_PROTOCOL)

    end_time = time.time()

    print('{:.2f} seconds elapsed during metadata preprocessing'.format(
        end_time - start_time))
