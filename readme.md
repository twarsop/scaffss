# SCAFFSS

## Super Cool Awesome Framework For Static Sites

The purpose of this project is to create a lightweight framework that can be used to generate static sites.

### Some History

I've recently created a personal website [repo here](https://github.com/twarsop/personal-website), [site here](http://tomwarsop.com/) that is a static site. However, there is a lot of repeated code within the HTML, e.g. the footer on each page, and all this repeated code feels bad.

I've used componentised frameworks before such as Angular. But for creating simple static sites such as my personal webiste this feels like a very heavy handed approach.

Hence, the creation of this project.

## Project Aim

Ideally I would like the output of this project to work in the following way:

```
templates --|
            |--> framework --> output static site pages
data -------|
```

There are a couple of requirements about how the project is approached too:
- Written in python
- Going to use the [jinja2](https://pypi.org/project/Jinja2/) templating library as a base.

## To Do

For others that want to get involved (and as a reference for myself), here is a list of things that currently need doing:
- ~~Create a very simple python script that copies the contents of one folder and outputs it to another folder (this is a fundamental action this project is going to do and is the smallest first building block I can think of). For example files to copy from source to target directories might as well use the current version of [my personal site](https://github.com/twarsop/personal-website).~~
- ~~Create a simple inline templating example using jinja2 - to start to learn how it works.~~
- ~~Update the simple inline templating example to use input files for both the template and the content.~~
- ~~Using the knowledge acquired above, get a templating solution that refactors the footer from my personal site into a single file which is then injected into all of the site pages.~~
- ~~Similarly, refactor the header from the personal site into a single file which is then injected into all of the site pages.~~
- ~~The build method currently has the content injected into the templates hardcoded, this needs to be changed so that it doesn't have to be updated everytime the templates/content changes. Example of hardcoded content:~~
```
output_file.write(Template(template).render(footer=content['footer'], header=content['header']))
```
- ~~Currently scaffss assumes a single flat directory for the `static` folder, this may of course not be true. So `build` needs to be updated to recursively copy the `static` files. (Note: this also means that currently the example personal website isn't actually complete because the previous versions directory has not been included).~~