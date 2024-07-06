import json
from typing import List, Dict, Any


class GraphJsonParser:
    def parse(self, file_path: str):
        """
        Parse the JSON file and return the data
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as file:
            for line in file:
                yield json.loads(line)
