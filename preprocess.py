import metadata
import query
import pickle
import utils
import time

start_time = time.time()

vocabulary = set()

metadata.read_metadata(vocabulary)
query.read_query(vocabulary)

print("Pickle vocabulary")

# Pickle vocabulary
with open(utils.get_file_path("out/vocabulary.pickle"), 'wb') as file:
    pickle.dump(vocabulary, file, protocol=pickle.HIGHEST_PROTOCOL)

end_time = time.time()

print('{:.2f} seconds elapsed during total preprocessing'.format(
    end_time - start_time))
