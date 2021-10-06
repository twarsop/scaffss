import os
from shutil import copyfile

example_personal_website_dir = "../examples/personal-website/"
example_personal_website_input_dir = f"{example_personal_website_dir}input/"
example_personal_website_output_dir = f"{example_personal_website_dir}output/"

for file in os.listdir(example_personal_website_input_dir):
    copyfile(f"{example_personal_website_input_dir}/{file}", f"{example_personal_website_output_dir}/{file}")