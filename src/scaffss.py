import os
from shutil import copyfile
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
    example_personal_website_input_static_dir = f"{example_personal_website_dir}input/static/"
    example_personal_website_input_templates_dir = f"{example_personal_website_dir}input/templates/"
    example_personal_website_output_dir = f"{example_personal_website_dir}output/"

    for file in os.listdir(example_personal_website_input_static_dir):
        copyfile(f"{example_personal_website_input_static_dir}{file}", f"{example_personal_website_output_dir}{file}")

    for file in os.listdir(example_personal_website_input_templates_dir):
        template = read_file(f'{example_personal_website_input_templates_dir}/{file}')
        with open(f'{example_personal_website_output_dir}{file}', 'w') as output_file:
            output_file.write(Template(template).render())

# copy_folder()
# jinja2_example()
build()