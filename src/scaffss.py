from argparse import ArgumentParser
import os
import shutil
import pathlib

parser = ArgumentParser()
parser.add_argument("-i", "--input-folder", dest="input_folder", help="The location of the input folder scaffss will use to build the site.")
parser.add_argument("-o", "--output-folder", dest="output_folder", help="The location of the output folder scaffss will use to output the built to.")
args = parser.parse_args()

scaffold_folder = os.path.join(args.input_folder, "scaffold", "")
components_folder = os.path.join(args.input_folder, "components", "")

for root, dirs, files in os.walk(args.output_folder):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        shutil.rmtree(os.path.join(root, name))

counter = 0
for subdir, dirs, files in os.walk(scaffold_folder):
    output_dir = os.path.join(args.output_folder, subdir[len(scaffold_folder):])
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for file in files:
        counter += 1
        input_file = os.path.join(subdir, file)
        print(f'Constructing [{counter}] {input_file.replace(scaffold_folder, "")}')

        output_file = os.path.join(output_dir, file)
        
        if (pathlib.Path(file).suffix in [".css", ".html"]):
            with open(output_file, "w") as output_file_handle:
                with open(input_file, "r") as input_file_handle:
                    for line in input_file_handle:
                        if ("{{{" in line and "}}}" in line):
                            parsed_component = line.replace("{{{", "").replace("}}}", "").strip()
                            component_file = os.path.join(components_folder, parsed_component)

                            with open(component_file, "r") as component_file_handle:
                                for component_line in component_file_handle:
                                    component_line_indented = f'{" " * line.find("{")}{component_line}'
                                    output_file_handle.write(component_line_indented)
                        else:
                            output_file_handle.write(line)
        else:
            shutil.copyfile(input_file, output_file)

print("Construction complete")