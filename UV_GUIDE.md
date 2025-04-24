# Guide to setting up a development environment with uv

This guide explains how to set up a development environment for this project using `uv`.

## Prerequisites

- Install `uv`. Follow the instructions on the official `uv` documentation for your operating system.

## Setup

1.  **Navigate to the project directory:**

    ```bash
    cd gpt-researcher
    ```

2.  **Create a virtual environment using `uv`:**

    ```bash
    uv venv
    ```
    This will create a `.venv` directory in your project.

3.  **Activate the virtual environment:**

    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```

4.  **Install dependencies using `uv`:**

    ```bash
    uv pip install -r requirements.txt
    ```
    This will install all the project dependencies listed in the `requirements.txt` file within your activated virtual environment.

## Running the project

Once the dependencies are installed, you can run the project as described in the main `README.md` file. For example, to start the server:

```bash
python -m uvicorn main:app --reload
```

## Using Poetry (Alternative)

The project also uses Poetry for dependency management (indicated by `pyproject.toml`). If you prefer using Poetry, you can install it and then run:

```bash
poetry install
```

This will create a virtual environment and install dependencies based on the `pyproject.toml` file. Refer to the Poetry documentation for more details.