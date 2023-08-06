# OpenTriviaDB

An asynchronous wrapper for the [Open Trivia DB](https://opentdb.com/) API.

This is an unofficial wrapper, and is not affiliated with [PIXELTAIL GAMES LLC.](https://www.pixeltailgames.com/)

## Installation

To install the latest stable version of OpenTriviaDB, use the following command:

```sh
pip install opentriviadb
```

You can also install the latest development version using the following command:

```sh
pip install git+https://github.com/parafoxia/opentriviadb
```

You may need to prefix these commands with a call to the Python interpreter depending on your OS and Python configuration.

## Usage

Before you can pull questions from the API, you first need to create a client:

```py
from opentriviadb import Client

client = Client()

# You can also use the client via a context manager.
async with Client() as client:
    ...
```

To prevent duplicate questions being pulled, request a session token:

```py
await client.request_token()
```

You can now run a round of trivia!
Questions are yielded one at a time when needed, though you can use the `list()` built-in function if you need them all available at once.
See the [`Question`](./questions) docs for more information.

```py
async for q in client.round():
    # Yields `Question` objects.
    ...
```

Once you're done, you need to tear the client down:

```py
await client.teardown()
```

If you use the client via the context manager, the teardown method is called automatically.

## Contributing

Contributions are very much welcome!
To get started:

* Familiarise yourself with the [code of conduct](https://github.com/parafoxia/opentriviadb/blob/main/CODE_OF_CONDUCT.md)
* Have a look at the [contributing guide](https://github.com/parafoxia/opentriviadb/blob/main/CONTRIBUTING.md)

## License

The OpenTriviaDB module for Python is licensed under the [BSD 3-Clause License](https://github.com/parafoxia/opentriviadb/blob/main/LICENSE).
