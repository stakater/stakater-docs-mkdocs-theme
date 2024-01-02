# stakater-docs-mkdocs-theme
Stakater documentation MkDocs theme common resources

## How to use

Import this git submodule into your target docs project by running the follow command:
```bash
git submodule add https://github.com/stakater/stakater-docs-mkdocs-theme.git th
eme_common
```
OR by adding a specific branch:
```bash
git submodule add -b whichGitBranch https://github.com/stakater/stakater-docs-mkdocs-theme.git th
eme_common
```

> Note: If you project already have this as a git submodule, you can take an update by running this command:
```bash
git submodule update --init --recursive --remote
```

Then, run the scripts in `scripts` folder in your target project root as below:

```bash
python theme_common/scripts/combine_theme_resources.py theme_common/resources theme_override/resources dist/_theme
```

```bash
python theme_common/scripts/combine_mkdocs_config_yaml.py theme_common/mkdocs.yml theme_override/mkdocs.yml mkdocs.yml
```

where as `theme_override` folder represents the overriden theme resources in your target project.

These scripts will generate theme resources and will also create a final `mkdocs.yml` file in the tharget project's root directory.

Your target project directory should look like this:

```
your-project/
    theme_common/
    theme_override/
    ...
```

In above directory structure, `theme_common` is the git submodule pointing to this project.
`theme_override` will have the same directory structure as `theme_common` to override the common resources.
