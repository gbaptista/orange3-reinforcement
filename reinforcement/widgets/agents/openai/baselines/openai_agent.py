from tempfile import NamedTemporaryFile
from os import remove

from ...agent import Agent

# Tensorflow Issue
#
# Problem: tensorflow/python/framework/load_library.py > load_op_library
# On file: tensorflow/contrib/image/python/ops/single_image_random_dot_stereograms.py
# You should comment:
# _sirds_ops = loader.load_op_library(
#     resource_loader.get_path_to_datafile(
#         "_single_image_random_dot_stereograms.so"))

class OpenAIAgent(Agent):
    def previous_results_load_path(self):
        if 'pkl_data' in self.memory:
            temporary_file = NamedTemporaryFile(suffix='.pkl', delete=False)
            temporary_file.write(self.memory['pkl_data'])
            temporary_file_name = temporary_file.name
            temporary_file.close()

            return temporary_file_name
        else:
            return None

    def save_results(self):
        print('save_results!')
        temporary_file = NamedTemporaryFile(suffix='.pkl', delete=True)
        temporary_file_name = temporary_file.name
        temporary_file.close()

        self.act.save(temporary_file_name)

        with open(temporary_file_name, 'rb') as pkl:
            pkl_data = pkl.read()

        self.memory['pkl_data'] = pkl_data

        remove(temporary_file_name)
