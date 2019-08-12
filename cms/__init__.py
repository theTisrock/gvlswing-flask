# This module implements a class (or classes) that handle simple content management from json files instead of
# from a database. The methods contained here attempt to read in json data from a file. Their returned json may be
# useful for applying data to a template.

# This idea is in testing and is originally developed for the main page content

import json
import os

base_directory = "/home/thetisrock/Documents/projects/clients/gvlswing-flask/managed_content/"


class CMS(object):

    @staticmethod
    def read(json_file_name):
        full_file_name = os.path.join(base_directory, json_file_name)

        file = open(full_file_name, mode='r')
        json_raw = file.read()  # read in all contents
        converted = json.loads(json_raw)
        file.close()  # always remember to close

        return converted

    @staticmethod
    def write(json_file_name, content_dict):
        json_raw = json.dumps(content_dict)  # json to raw text
        full_file_name = os.path.join(base_directory, json_file_name)

        file = open(full_file_name, mode='w')
        file.write(json_raw)

        file.close()  # always remember to close

# end cms-no-db
