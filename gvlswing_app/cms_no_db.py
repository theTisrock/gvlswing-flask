# This module implements a class (or classes) that handle simple content management from json files instead of
# from a database. The methods contained here attempt to read in json data from a file. Their returned json may be
# useful for applying data to a template.

# This idea is in testing and is originally developed for the main page content

import json
import os


class CMSSimple(object):

    @staticmethod
    def get_json_content(json_file_name):

        base_directory = os.path.abspath(os.path.dirname(__file__))
        full_file_name = os.path.join(base_directory, json_file_name)

        print(full_file_name)

        file = open(full_file_name, mode='r')
        json_raw = file.read()  # read in all contents
        converted = json.loads(json_raw)
        file.close()  # always remember to close

        return converted

# end cms-no-db
