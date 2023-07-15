# Snap SAAS Base

Snap Env (https://snapenv.com) Python base module.

## Tools

To streamline, standardize and ensure standard quality, we recommend using some useful tools.

<details>
<summary>With artificial intelligence</summary>

<details>
<summary>1. Opencommit</summary>

1. [Install opencommit](https://github.com/di-sukharev/opencommit).
    - We use it with NodeJS _v16.19.1_ to install it.
    - _Configuration_:
        - Use gpt-4 for best results:
            ```sh
            opencommit config set OCO_MODEL=gpt-4
            ```
        - Use {GitMoji](https://gitmoji.dev/), we like it:
            ```sh
            opencommit config set OCO_EMOJI=true
            ```
        - Set locale to english:
            ```sh
            oco config set OCO_LANGUAGE=en
            ```
        - Set OpenAI API KEY:
            ```sh
            opencommit config set OCO_OPENAI_API_KEY=<your_api_key>
            ```

</details>

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:

1. ⭐️ _GitHub Codespaces_: click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/orgs/snapenv/snap-saas-base) to clone this repository in a container volume and create a Dev Container with VS Code.
1. _Dev Container_: clone this repository, open it with VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
1. _PyCharm_: clone this repository, open it with PyCharm, and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote) with the `dev` service.
1. _Terminal_: clone this repository, open it with your terminal, and run `docker compose up --detach dev` to start a Dev Container in the background, and then run `docker compose exec dev zsh` to open a shell prompt in the Dev Container.

</details>

<details>
<summary>Developing</summary>

- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
- Run `cz bump` to bump the package's version, update the `CHANGELOG.md`, and create a git tag.

</details>

* opencommit
* 
