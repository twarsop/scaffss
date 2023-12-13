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