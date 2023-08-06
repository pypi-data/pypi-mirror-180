# repoutil

repoutil is a simple command line utility to write gitignores, licenses and workflow files to a project.

## Usage

```
Usage: repo [OPTIONS] COMMAND [ARGS]...

  repo is a simple command line utility to write gitignores, licenses and
  workflows to a repo.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  g  Generates a gitignore file for the given language.
  l  Generates a license file for the given license.
  w  Generates a workflow file for the given language.
```

Examples:
```
repo g python # generate a gitignore file for python
repo l mit # generate a mit license file
```


<br>


## Versioning

repoutil releases follow semantic versioning, every release is in the *x.y.z* form, where:

- x is the MAJOR version and is incremented when a backwards incompatible change to stella is made.
- y is the MINOR version and is incremented when a backwards compatible change to stella is made, like changing dependencies or adding a new function, method, or features.
- z is the PATCH version and is incremented after making minor changes that don't affect stella's public API or dependencies, like fixing a bug.

<br>

## Licensing

License © 2021-Present Shravan Asati

This repository is licensed under the MIT license. See [LICENSE](LICENSE.txt) for details.