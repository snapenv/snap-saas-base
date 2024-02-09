[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/orgs/snapenv/snap-saas-base)

# Snap SAAS Base

Snap Env (https://snapenv.com) Python base module.

## Using

_Python package_: To add and install this package as a dependency of your project, run `poetry add snap-saas-base`.

## Contributing

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Set up Git to use SSH</summary>

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. Configure SSH to automatically load your SSH keys:
    ```sh
    cat << EOF >> ~/.ssh/config
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
    EOF
    ```

</details>

<details>
<summary>2. Install Docker</summary>

1. [Install Docker Desktop](https://www.docker.com/get-started).
    - Enable _Use Docker Compose V2_ in Docker Desktop's preferences window.
    - _Linux only_:
        - Export your user's user id and group id so that [files created in the Dev Container are owned by your user](https://github.com/moby/moby/issues/3206):
            ```sh
            cat << EOF >> ~/.bashrc
            export UID=$(id --user)
            export GID=$(id --group)
            EOF
            ```

</details>

<details>
<summary>3. Install VS Code or PyCharm</summary>

1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
2. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>

<details>
<summary>4. Install OpenCommit</summary>

1. [Install OpenCommit](https://github.com/di-sukharev/opencommit). Open a new shell window and execute the following commands:
    ```sh
    npm install -g opencommit
    oco config set OCO_OPENAI_API_KEY=sk-N...
    oco config set OCO_MODEL=gpt-4
    oco config set OCO_EMOJI=true
    ```

</details>

<details>
<summary>5. Install gpt4docstrings (dont install until tool upgrade to use new openai API client)</summary>

1. [Install gpt4docstrings](https://github.com/MichaelisTrofficus/gpt4docstrings). In the directory of the project and with poetry activated, execute the following commands:
    ```sh
    poetry add --group dev gpt4docstrings
    ```
2. _Optional:_ Test the command:
    ```sh
    OPENAI_API_KEY=sk-N... gpt4docstrings -w src/api.py
    ```
    - Check _src/snap_saas_base/api.py_ to see the generated docstring.

</details>

<details>
<summary>6. Install aider</summary>

1. [Install aider](https://github.com/paul-gauthier/aider). In the directory of the project and with poetry activated, execute the following commands:
    ```sh
    poetry add --group dev aider-chat
    ```
2. _Optional:_ Test the command:
    ```sh
    OPENAI_API_KEY=sk-N... aider --no-auto-commits 
    ```
    - After aider is loaded, use `/help` to see avaiable commands and check [aider project(https://github.com/paul-gauthier/aider) to understand this tool.
</details>

<details>
<summary>7. Install cz-conventional-gitmoji</summary>

1. [Install cz-conventional-gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji). In the directory of the project and with poetry activated, execute the following commands:
    ```sh
    poetry add --group dev cz-conventional-gitmoji
    ```
2. _Optional:_ Test the command:
    ```sh
    cz commit
    ```

</details>

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:

1. ⭐️ _GitHub Codespaces_: click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/snapenv/snap-saas-base) to clone this repository in a container volume and create a Dev Container with VS Code.
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
- Run `cz --name cz_gitmoji commit` so commit files using conventional commits with emojis.
- Run `cz --name cz_gitmoji bump --changelog` to bump the package's version, update the `CHANGELOG.md`, and create a git tag.
- Run `git push --tags` to push the new tag to github.

</details>
