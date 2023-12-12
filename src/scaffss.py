# from typing import List, Dict
# import os
# from shutil import copyfile
# from distutils.dir_util import copy_tree
# from jinja2 import Template
# import json
from argparse import ArgumentParser
import os
import shutil
import pathlib

# class PageFile():
#     def __init__(self, root_dir: str, location: str, name: str):
#         self.location = os.path.join(root_dir, location, name)
#         self.name = name

#     @classmethod
#     def from_json(cls, root_dir, data):
#         return cls(root_dir, data['location'], data['name'])

# class InjectMany():
#     def __init__(self, tag: str, page_file: PageFile, inject_literal_sets: List[Dict[str, str]]):
#         self.tag = tag
#         self.page_file = page_file
#         self.inject_literal_sets = inject_literal_sets

#     @classmethod
#     def from_json(cls, root_dir, data):
#         return cls(data['tag'], PageFile.from_json(root_dir, data['page_file']), data['inject_literal_sets'])

# class Page():
#     def __init__(self, page_file: PageFile, inject_files: List[Dict[str, str]], inject_literals: List[Dict[str, str]], inject_many: List[InjectMany]):
#         self.page_file = page_file
#         self.inject_files = inject_files
#         self.inject_literals = inject_literals
#         self.inject_many = inject_many

#     @classmethod
#     def from_json(cls, data):
#         inject_many = []
#         for im in data['inject_many']:
#             inject_many.append(InjectMany.from_json(data['root_dir'], im))
#         return cls(PageFile.from_json(data['root_dir'], data["page_file"]), data["inject_files"], data["inject_literals"], inject_many)

# class Scaffss():
#     def __init__(self, root_dir: str, output_folder: str, static_folder: str, pages: List[Page]):
#         self.root_dir = root_dir
#         self.output_folder = os.path.join(root_dir, output_folder)
#         self.static_folder = os.path.join(root_dir, static_folder)
#         self.pages = pages

#     @classmethod
#     def from_json(cls, root_dir, data):
#         for d in data['pages']:
#             d['root_dir'] = root_dir
#         return cls(root_dir, data["output_folder"], data["static_folder"], list(map(Page.from_json, data["pages"])))

# def read_file(file_name):
#     file_contents = None
#     with open(file_name) as file:
#         file_contents = file.read().strip()
#     return file_contents

# def build(scaffss_file_location):
#     data_str = None
#     with open(scaffss_file_location) as json_file:
#         data_str = json_file.read()

#     scaffss = Scaffss.from_json(os.path.dirname(scaffss_file_location), json.loads(data_str))

#     copy_tree(scaffss.static_folder, scaffss.output_folder)    

#     for page in scaffss.pages:
#         page_contents = read_file(page.page_file.location)
        
#         page_inject_contents = dict()

#         for inject_file in page.inject_files:
#             for key, value in inject_file.items():
#                 page_inject_contents[key] = read_file(os.path.join(scaffss.root_dir, value))

#         for inject_literal in page.inject_literals:
#             for key, value in inject_literal.items():
#                 page_inject_contents[key] = value

#         for im in page.inject_many:
#             im_page = read_file(im.page_file.location)

#             im_contents = ''
#             for ils in im.inject_literal_sets:
#                 im_contents += Template(im_page).render(**ils)

#             page_inject_contents[im.tag] = im_contents

#         with open(os.path.join(scaffss.output_folder, page.page_file.name), 'w') as output_file:
#             previously_rendered_template = None
#             rendered_template = Template(page_contents).render(**page_inject_contents)
            
#             while previously_rendered_template != rendered_template:
#                 previously_rendered_template = rendered_template
#                 rendered_template = Template(rendered_template).render(**page_inject_contents)

#             output_file.write(rendered_template)

# parser = ArgumentParser()
# parser.add_argument("-sf", "--scaffss-file", dest="scaffss_file", help="The location of the scaffss file to process")
# args = parser.parse_args()

# build(args.scaffss_file)

parser = ArgumentParser()
parser.add_argument("-i", "--input-folder", dest="input_folder", help="The location of the input folder scaffss will use to build the site.")
parser.add_argument("-o", "--output-folder", dest="output_folder", help="The location of the output folder scaffss will use to output the built to.")
args = parser.parse_args()

scaffold_folder = os.path.join(args.input_folder, "scaffold", "")
components_folder = os.path.join(args.input_folder, "components", "")

print(f"input_folder: {args.input_folder}")
print(f"scaffold_folder: {scaffold_folder}")
print(f"components_folder: {components_folder}")
print(f"output_folder: {args.output_folder}")

for root, dirs, files in os.walk(args.output_folder):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        shutil.rmtree(os.path.join(root, name))

for subdir, dirs, files in os.walk(scaffold_folder):
    output_dir = os.path.join(args.output_folder, subdir[len(scaffold_folder):])
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    print("====================================================")
    print(output_dir)

    for file in files:
        print("-----------------------------------------------------------")
        print(file)

        input_file = os.path.join(subdir, file)
        print(input_file)

        output_file = os.path.join(output_dir, file)
        print(output_file)

        if (pathlib.Path(file).suffix in [".css", ".html"]):
            with open(output_file, "w") as output_file_handle:
                with open(input_file, "r") as input_file_handle:
                    for line in input_file_handle:
                        if ("{{{" in line and "}}}" in line):
                            # parse the component to load
                            parsed_component = line.replace("{{{", "").replace("}}}", "").strip()

                            component_file = os.path.join(components_folder, parsed_component)

                            print(component_file)

                            with open(component_file, "r") as component_file_handle:
                                for component_line in component_file_handle:
                                    print(component_line)
                                    component_line_indented = f'{" " * line.find("{")}{component_line}'
                                    output_file_handle.write(component_line_indented)
                        else:
                            output_file_handle.write(line)
        else:
            shutil.copyfile(input_file, output_file)