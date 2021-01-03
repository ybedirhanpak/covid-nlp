import metadata
import query
import time

start_time = time.time()

metadata.read_metadata()
query.read_query()

end_time = time.time()

print('{:.2f} seconds elapsed during total preprocessing'.format(
    end_time - start_time))
