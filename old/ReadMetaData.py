import csv
import utils

total_doc = {}
inverted_index = {}


def Read_MetaData():
    with open('./data/metadata.csv', 'r') as readFile:
        csv_reader = csv.reader(readFile, delimiter=',')

        for row in csv_reader:
            temp_title = f'{row[3]}'
            temp_abstract = f'{row[8]}'
            temp_docid = f'{row[0]}'

            sub_total_dic = temp_title + ' ' + temp_abstract

            sub_total_dic = utils.punct_removal(sub_total_dic)
            sub_total_dic = utils.stopword_removal(sub_total_dic.split(" "))
            sub_total_dic = utils.empty_removal(sub_total_dic)
            sub_total_dic = utils.repetition_removal(sub_total_dic)

            total_doc[temp_docid] = sub_total_dic

    readFile.close()

    return (total_doc)
