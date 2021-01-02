import xml.etree.ElementTree as ET
import utils
import os
import pickle
import time


def read_query(vocabulary: set):
    print("Preprocessing metadata.csv...")
    start_time = time.time()

    tree = ET.parse(utils.get_file_path("./data/topics-rnd5.xml"))
    root = tree.getroot()

    term_frequency_query = {}

    for topic in root:
        topic_number = topic.get("number")

        # Concatenate query, question and narrative and remove punctuation
        topic_content = utils.remove_punctuation(
            ' '.join([topic[i].text for i in range(3)]))

        # Term frequency in this topic
        topic_tf = {}

        # Preprocess each token in the document
        for token in topic_content.split(" "):
            # Normalize the token
            n_token = utils.normalize_token(token)

            # Skip stopwords
            if utils.is_stopword(n_token):
                continue

            # Add token to document dictionary
            if n_token not in topic_tf:
                topic_tf[n_token] = 1
            else:
                topic_tf[n_token] += 1

            # Add token to vocabulary
            vocabulary.add(n_token)

        term_frequency_query[topic_number] = topic_tf

    print("Pickle term_frequency_query")

    # Create out directory
    if not os.path.exists("out"):
        os.makedirs("out")

    # Pickle term_frequency_query
    with open(utils.get_file_path("out/term_frequency_query.pickle"), 'wb') as file:
        pickle.dump(term_frequency_query, file,
                    protocol=pickle.HIGHEST_PROTOCOL)

    end_time = time.time()

    print('{:.2f} seconds elapsed during query preprocessing'.format(
        end_time - start_time))
