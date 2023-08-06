# Repo Ranger

Repo Ranger is a command-line tool for managing a set of Git repositories. It
uses a configuration file to define the root folder for the repositories and
the list of repositories to manage.

## Installation

To install Repo Ranger, clone this repository and run `pip install .` from
the root directory.

## Usage

```bash
repo_ranger [OPTIONS] COMMAND [ARGS]...
```

### Commands

* `init`: Initialize the repository structure based on the configuration file.
* `list`: List the configured repositories and their metadata.
* `clone`: Clone the configured repositories.
* `pull`: Pull the latest changes from the remote repositories.
* `help`: Show this message and exit.

### Options

* `-c, --config FILE`: Path to the configuration file.

## Examples

Initialize the repository structure:

```bash
repo_ranger init -c /path/to/config.yml
```

Pull the latest changes from all repositories:

```bash
repo_ranger pull -c /path/to/config.yml
```

Pull the latest changes from repositories with the "web" tag:

```bash
repo_ranger pull --include web -c /path/to/config.yml
```

List the configured repositories:

```bash
repo_ranger list -c /path/to/config.yml
```

Clone the configured repositories:

```bash
repo_ranger clone -c /path/to/config.yml
```

Display help information for `repo_ranger`:

```bash
repo_ranger help
```

## Configuration

The configuration file is a YAML file that defines the root folder for the
repositories and the list of repositories to manage. An example configuration
file is shown below:

```yaml
proot_folder: /path/to/repositories

repositories:
  - name: project-frontend
    url: https://github.com/user/project-frontend.git
    path: project/frontend
    summary: This repository contains the frontend code for the project.
    tags: [web, frontend]
  - name: project-backend
    url: https://github.com/user/project-backend.git
    path: project/backend
    summary: This repository contains the backend code for the project.
    tags: [api, backend]
  - name: project-docs
    url: https://github.com/user/project-docs.git
    path: project/docs
    summary: This repository contains the documentation for the project.
    tags: [docs]
```

## Contributing

We welcome contributions to Repo Ranger. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and add tests for them
4. Run the tests to ensure they pass
5. Submit a pull request

Before submitting your changes, please make sure that your code follows the
[PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide and that it
passes the linting and testing checks. You can run the linting and testing
checks by using the following commands:

```bash
make lint
make test
```

## Credits

- Repo Ranger uses the [PyYAML](https://github.com/yaml/pyyaml) library to
parse the configuration file.
- RepoRanger was created with the help of [Assistant](https://assistant.openai.com/),
a large language model trained by OpenAI.

## License

Repo Ranger is released under the MIT license. See
[LICENSE](https://chat.openai.com/LICENSE) for more details.

