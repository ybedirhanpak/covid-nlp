import xml.etree.ElementTree as ET
import utils
import os
import time


def read_query():
    print("Preprocessing metadata.csv...")
    start_time = time.time()

    tree = ET.parse(utils.get_file_path("./data/topics-rnd5.xml"))
    root = tree.getroot()

    normalized_queries = []
    query_ids = []

    for topic in root:
        topic_number = topic.get("number")

        # Concatenate query, question and narrative and remove punctuation
        topic_content = utils.normalize_doc(
            ' '.join([topic[i].text for i in range(3)]))

        # Term frequency in this topic
        topic_tf = {}

        normalized_query = []

        # Preprocess each token in the document
        for token in topic_content.split(" "):
            # Normalize the token
            n_token = utils.normalize_token(token)

            # Skip stopwords
            if utils.is_stopword(n_token):
                continue

            normalized_query.append(n_token)

            # Add token to document dictionary
            if n_token not in topic_tf:
                topic_tf[n_token] = 1
            else:
                topic_tf[n_token] += 1

        normalized_queries.append(' '.join(normalized_query))
        query_ids.append(topic_number)

    print("Pickle normalized_queries...")

    # Create out directory
    if not os.path.exists("out"):
        os.makedirs("out")

    # Pickle normalized_queries
    utils.pickle_object(normalized_queries, "out/normalized_queries.pickle")

    # Pickle query_ids
    utils.pickle_object(query_ids, "out/query_ids.pickle")

    end_time = time.time()

    print('{:.2f} seconds elapsed during query preprocessing'.format(
        end_time - start_time))
