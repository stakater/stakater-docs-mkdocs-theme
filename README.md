# stakater-docs-mkdocs-theme

This project serves as a shared MkDocs theme for all the Stakater MkDocs projects. By integrating this repository as a git submodule into your project, you can utilize the common theme and take updates.

## Usage Guide

### Pre-requisites
Python 3 environment

### 1. Import as git submodule
Add the submodule to your target Mkdocs project at `theme_common` path. You can learn more about the git submodules [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### 2. Directory structure in target project
Your target project directory should look like this after adding the submodule:
```
your-project/
    theme_common/
    ...
```
In order to override the `theme_common`, you can mirror this directory in your target project as `theme_override` and customise the files there as you need. Directory structure would look like this after that:
```
your-project/
    theme_common/
    theme_override/
```
In your `theme_override` folder, you can replace `mkdocs.yml` with the following starting template:
```yaml
site_name: <project name>
site_url: https://project-name.stakater.com/
repo_url: <git https url>
docs_dir: content
edit_uri: blob/main/content/

nav:
    - index.md

```

### 3. Add content in target MkDocs project
In this project, default mkdocs documentation folder is set to `content`. If you want to override that setting, you can change following properties in `theme_override/mkdocs.yml`:
- `docs_dir` 
- `edit_uri`

Add your content and then you can link it in `theme_override/mkdocs.yml` by overriding the following setting:
- `nav`

You can visit MkDocs official documentation to find out how to define `nav` in `mkdocs.yml` file.

Target project's directory structure would look like this after adding `content` dir:
```
your-project/
    theme_common/
    theme_override/
    content/
```

### 4. Run scripts in target project
Assuming that target project will already have a python environment,
execute the following commands in the root of your target project:
1. Install Python Dependencies:
```bash
pip3 install -r theme_common/requirements.txt
```
2. Combine Theme Resources:
```bash
python theme_common/scripts/combine_theme_resources.py theme_common/resources theme_override/resources dist/_theme
```
> Above command will output combined theme to `dist/_theme`.
3. Produce mkdocs YAML file:
```bash
python theme_common/scripts/combine_mkdocs_config_yaml.py theme_common/mkdocs.yml theme_override/mkdocs.yml mkdocs.yml
```
These scripts will create a combined theme and a `mkdocs.yml` file.

Your target project will now have an mkdocs theme. If you want to customise `mkdocs.yml` or theme resources, you can do so by modifying files in `theme_override` folder and running the above scripts again.
