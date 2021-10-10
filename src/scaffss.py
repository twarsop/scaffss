import os
from shutil import copyfile
from distutils.dir_util import copy_tree
from jinja2 import Template

def copy_folder():
    example_personal_website_dir = "../examples/personal-website/"
    example_personal_website_input_dir = f"{example_personal_website_dir}input/"
    example_personal_website_output_dir = f"{example_personal_website_dir}output/"

    for file in os.listdir(example_personal_website_input_dir):
        copyfile(f"{example_personal_website_input_dir}/{file}", f"{example_personal_website_output_dir}/{file}")

def read_file(file_name):
    file_contents = None
    with open(file_name) as file:
        file_contents = file.read().strip()
    return file_contents

def jinja2_example():
    jinja2_example_from_file_dir = "../examples/jinja2-example-from-file/"
    jinja2_example_from_file_input_dir = f"{jinja2_example_from_file_dir}input/"
    jinja2_example_from_file_output_dir = f"{jinja2_example_from_file_dir}output/"

    template = read_file(f"{jinja2_example_from_file_input_dir}template.txt")
    content = read_file(f"{jinja2_example_from_file_input_dir}content.txt")

    with open(f"{jinja2_example_from_file_output_dir}output.txt", "w") as output_file:
        output_file.write(Template(template).render(something=content));

def build():
    example_personal_website_dir = "../examples/personal-website/"
    content_dir = f"{example_personal_website_dir}input/content/"
    static_dir = f"{example_personal_website_dir}input/static/"
    templates_dir = f"{example_personal_website_dir}input/templates/"
    output_dir = f"{example_personal_website_dir}output/"

    content = dict()
    for file in os.listdir(content_dir):
        content[file.split('.')[0]] = read_file(f'{content_dir}/{file}')

    copy_tree(static_dir, output_dir)

    for file in os.listdir(templates_dir):
        template = read_file(f'{templates_dir}/{file}')
        with open(f'{output_dir}{file}', 'w') as output_file:
            output_file.write(Template(template).render(**content))

# copy_folder()
# jinja2_example()
build()