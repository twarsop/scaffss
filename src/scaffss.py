from typing import List, Dict
import os
from shutil import copyfile
from distutils.dir_util import copy_tree
from jinja2 import Template
import json

class PageFile():
    def __init__(self, location: str, name: str):
        self.location = location
        self.name = name

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def fullpath(self):
        return os.path.join(self.location, self.name)

class Page():
    def __init__(self, page_file: PageFile, inject_files: List[Dict[str, str]], inject_literals: List[Dict[str, str]]):
        self.page_file = page_file
        self.inject_files = inject_files
        self.inject_literals = inject_literals

    @classmethod
    def from_json(cls, data):
        return cls(PageFile.from_json(data["page_file"]), data["inject_files"], data["inject_literals"])

class Scaffss():
    def __init__(self, output_folder: str, pages: List[Page]):
        self.output_folder = output_folder
        self.pages = pages

    @classmethod
    def from_json(cls, data):
        return cls(data["output_folder"], list(map(Page.from_json, data["pages"])))

def read_file(file_name):
    file_contents = None
    with open(file_name) as file:
        file_contents = file.read().strip()
    return file_contents

def build(scaffss_file_location):
    data_str = None
    with open(scaffss_file_location) as json_file:
        data_str = json_file.read()

    scaffss = Scaffss.from_json(json.loads(data_str))
    
    example_personal_website_dir = "../examples/personal-website/"
    static_dir = f"{example_personal_website_dir}input/static/"

    copy_tree(static_dir, scaffss.output_folder)    

    for page in scaffss.pages:
        page_contents = read_file(page.page_file.fullpath())
        
        page_inject_contents = dict()

        for inject_file in page.inject_files:
            for key, value in inject_file.items():
                page_inject_contents[key] = read_file(value)

        for inject_literal in page.inject_literals:
            for key, value in inject_literal.items():
                page_inject_contents[key] = value

        with open(os.path.join(scaffss.output_folder, page.page_file.name), 'w') as output_file:
            output_file.write(Template(page_contents).render(**page_inject_contents))

build('../examples/personal-website/input/scaffss.json')