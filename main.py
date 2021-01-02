import utils
import ReadMetaData
import ReadQuery

query_dict = ReadQuery.Read_Query_Dict()
doc_dict = ReadMetaData.Read_MetaData()
inverted_index = utils.create_invertedindex_list(doc_dict)
total_word_list = utils.create_total_word_list(query_dict, doc_dict)


print(query_dict, "QUERY")
print(doc_dict, "DOC DICT")
print(inverted_index, "INVERTED INDEX")
print(total_word_list, "TOTAL WORD LIST")
