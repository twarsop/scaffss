import os
from shutil import copyfile
from jinja2 import Template

def copy_folder():
    example_personal_website_dir = "../examples/personal-website/"
    example_personal_website_input_dir = f"{example_personal_website_dir}input/"
    example_personal_website_output_dir = f"{example_personal_website_dir}output/"

    for file in os.listdir(example_personal_website_input_dir):
        copyfile(f"{example_personal_website_input_dir}/{file}", f"{example_personal_website_output_dir}/{file}")

def jinja2_example():
    t = Template("Hello {{ something }}!")
    print(t.render(something="World"))

# copy_folder()
jinja2_example()