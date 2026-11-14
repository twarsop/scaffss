# SCAFFSS

## Super Cool Awesome Framework For Static Sites

The purpose of this project is to create a lightweight framework that can be used to generate static sites.

## Background

I've recently created a personal website [repo here](https://github.com/twarsop/personal-website), [site here](http://tomwarsop.com/) that is a static site. However, there is a lot of repeated code, e.g. the footer on each page, and all this repeated code feels bad. So I wanted to create reusable components to reduce code duplication.

I've used componentised frameworks before such as Angular. But for creating simple static sites such as my personal webiste this feels like a very heavy handed approach.

Hence, the creation of this project.

## Usage

The `scaffss.py` is fairly small at the moment and easy to use. It requires two parameters when executed: an input folder location and an output folder location. These are identified with the `-i` and `-o` flags (or `--input-folder` and `--output-folder` in long hand). So example usage of executing the script is:

```
scaffss.py -i some/folder/location/input -o another/folder/location/output
```

To keep the current script small some conventions are used. It is expected that the input folder will contain two futher folders:
- `scaffold/`: contains all of the pages for the site
- `components/`: contains all of the components that will be injected into the scaffold pages

To inject a component into a scaffold page include the component's filename surrounded by 3 pairs of braces, e.g. `{{{ component_file.html }}}`.

## Variables

Values that are used in more than one place can be kept in an optional `config.json` file in the input folder (next to `scaffold/` and `components/`). It must contain a single JSON object:

```
config.json

{
    "version": "1.2.0",
    "updated": "2026/11/14"
}
```

To inject a value include its name surrounded by 2 pairs of braces, e.g. `{{ version }}`. Unlike components, variables can appear anywhere in a line, any number of times, in both scaffold pages and components (only `.html` and `.css` files are processed). If a page uses a variable that isn't in `config.json` the build stops with an error naming the file and the variable.

## Example

Scaffold file (`input-folder/scaffold/`):

```
index.html

<!DOCTYPE html>
<html lang="en">
    <body>
        <div>Hello World</div>
        {{{ component.html }}}
    </body>
</html>
```

Component file (`input-folder/components/`):

```
component.html

<div>This is a component</div>
```

Result of executing scaffss on the scaffold and components (`output-folder`):

```
index.html

<!DOCTYPE html>
<html lang="en">
    <body>
        <div>Hello World</div>
        <div>This is a component</div>
    </body>
</html>
```

For a real life and more involved example of this framework is used see the repo for my personal site [here](https://github.com/twarsop/personal-website).