import string


def punct_removal(stringval):
    total_string = ""
    for var in stringval:
        if var not in string.punctuation:
            total_string = total_string + var.lower()
        else:
            if var != '-':
                total_string = total_string + " "

    return total_string


def stopword_removal(splitted_doc):
    with open("./data/stopwords.txt") as f:
        stopword_array = f.read().splitlines()

    for splitted in list(splitted_doc):
        if splitted in stopword_array:
            splitted_doc.remove(splitted)

    f.close()
    return splitted_doc



def empty_removal(splitted_doc):
    for word in list(splitted_doc):
        if word == '':
            splitted_doc.remove(word)

    return splitted_doc


def repetition_removal(list):
    new_word_dic = {}

    for word in list:
        if word not in new_word_dic:
            new_word_dic[word] = 1
        else:
            new_word_dic[word] += 1

    return new_word_dic


def create_invertedindex_list(total_doc):
    inverted_index = {}

    for doc_id in total_doc:
        for token in total_doc[doc_id]:
            if token not in inverted_index:
                inverted_index[token] = [doc_id]
            else:
                inverted_index[token].append(doc_id)

    return (inverted_index)


# Create total word dictionary consist of all words just by one
def create_total_word_list(query_dict, doc_dict):
    total_word_list = []

    for word in query_dict:
        if word not in total_word_list:
            total_word_list.append(word)

    for doc in doc_dict.values():
        for word in doc:
            if word not in total_word_list:
                total_word_list.append(word)

    return total_word_list