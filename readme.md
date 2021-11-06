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

For others that want to get involved (and as a reference for myself), here is a list of things that could be done in the future:
- Unit testing, specifcally around parsing the `scaffss.json` file
- Probably could remove Jinja2, we aren't really using any of it's more powerful functions (just the replace `{{ x }}` with a string), which we could probably do ourselves.
- Remove the personal website example - my personal website should actually be re-written to use this framework.
- Make `scaffss` a system wide command. So, for example, in any folder we can type the word `scaffss` and it will look for a `scaffss.json` file to parse and then build according to the instructions found it that file.
- Add a file watcher so hot reloads can be done during development - we can leave scaffss running on a folder and as changes are made it rebuilds.
```