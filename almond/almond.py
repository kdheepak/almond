# -*- coding: utf-8 -*-

import os

import pypandoc


class Almond(object):
    INPUT_FORMAT = 'md'
    OUTPUT_FORMAT = 'html'
    CONTENT = 'content'
    OUTPUT = 'output'
    ENCODING = 'utf-8'

    def __init__(self):
        try:
            os.makedirs(self.OUTPUT)
        except OSError:
            if not os.path.isdir(self.OUTPUT):
                raise

    def find_files(self):
        for root, dirs, files in os.walk(self.CONTENT):
            for file in files:
                if file.endswith(self.INPUT_FORMAT):
                    yield os.path.join(root, file)

    def convert(self, path_to_file):
        self.convert_to_html(path_to_file)

    def convert_to_html(self, path_to_file):
        html = pypandoc.convert_file(path_to_file, 'html')
        with open(path_to_file.replace(self.CONTENT, self.OUTPUT)
                .replace(self.INPUT_FORMAT, self.OUTPUT_FORMAT), 'w') as f:
            f.write(html.encode(self.ENCODING))
