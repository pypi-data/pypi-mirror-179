# 📝 git-annex-metadata-edit

Edit [`git-annex` metadata](https://git-annex.branchable.com/metadata/) with your `$EDITOR`.

## 📥 Installation

```bash
# From Gitlab
pip install git+https://gitlab.com/nobodyinperson/git-annex-metadata-edit
```

## ✨ Features

- Frontend to `git annex metadata --set/--remove`
- (recursively) overwrite a field with a value
- add and remove single-line values in one go for multiple files (also recursively)


## ❓ Usage

```bash
# 📟 From the Temrminal
git-annex-metadata-edit FIELDNAME ...FILES...
# or 
git annex-metadata-edit FIELDNAME ...FILES...
# or
git annex metadata-edit FIELDNAME ...FILES...
# or 
python -m git_annex_metadata_edit FIELDNAME ...FILES...

# 🤨 dry-run (check what it would do if you don't trust it)
git-annex-metadata-edit --dry-run FIELDNAME ...FILES...

# ❓ Help
git-annex-metadata-edit -h
```

`git-annex-metadata-edit` first tries your `$VISUAL`, then `$EDITOR`, then a list of common editors.

## 📟 Screencast 📹

[![asciicast](https://asciinema.org/a/541485.svg)](https://asciinema.org/a/541576?autoplay=1)
