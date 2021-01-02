import xml.etree.ElementTree as ET
import utils

tree = ET.parse('./data/topics-rnd5.xml')
root = tree.getroot()

query_list = []
question_list = []
narrative_list = []
word_dict = []


def Read_Query_Dict():
    for child in root:
        sub_topic_list = []
        query_list.append(child[0].text)
        question_list.append(child[1].text)
        narrative_list.append(child[2].text)

        sub_topic_list.append(child[0].text + ' ' + child[1].text + ' ' + child[2].text)

        sub_topic_list = utils.punct_removal(' '.join(map(str, sub_topic_list)))
        sub_topic_list = utils.stopword_removal(sub_topic_list.split(" "))
        sub_topic_list = utils.empty_removal(sub_topic_list)
        sub_topic_dict = utils.repetition_removal(sub_topic_list)

        word_dict.append(sub_topic_dict)

    return word_dict