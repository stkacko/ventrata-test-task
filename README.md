# Ventrata Task 3

This is an automated testing project for a web application. The project uses Python and the Playwright testing framework.

## Project Management

This project is managed using [Rye](https://github.com/astral-sh/rye)

Installation of Rye varies depending on the operating system. For example, on Linux / macOS, you can install Rye using the following command:
```commandline
curl -sSf https://rye.astral.sh/get | bash
```

When Rye is installed, simply clone the project and run the following command to install the project dependencies:
```commandline
rye sync
```

## Running the tests

To run the tests, execute the following command:
```commandline
rye run pytest tests/<test_file>.py
```


