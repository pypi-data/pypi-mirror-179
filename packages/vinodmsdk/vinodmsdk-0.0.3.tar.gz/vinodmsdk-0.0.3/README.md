# vinodmsdk - Python SDK client for [Lord of the Rings one API](https://the-one-api.dev/documentation)

## Description
The python client for the-one-api provides access to the following endpoints
- book
- chapter
- character
- movie
- quote

## Requirements
- Python 3.8 or higher
- requests

## Installation

``` python
pip install requests
pip install vinodmsdk
```

## Usage
To get books
``` python
import lotr

# Put in your api_key here
api_key="Your-api-key"
lotr = lotr.Client(api_key=api_key)
books=lotr.get_books()
```

To get chapters in a book
``` python
import lotr

# Put in your api_key here
api_key="Your-api-key"
lotr = lotr.Client(api_key=api_key)
books=lotr.get_books()
for book in books:
    chapters = lotr.get_book_chapters(book["_id"])
```

For pagination with sorting
``` python
import lotr

# Put in your api_key here
api_key="Your-api-key"
lotr = lotr.Client(api_key=api_key)
chapter_paginator = lotr.get_paginator("book_chapters", id="5cf5805fb53e011a64671582", sort="chapterName:asc", page_size=5)
for chapters in chapter_paginator:
    print(f"{chapters}\n")
```

Filtering
``` python
import lotr

# Put in your api_key here
api_key="Your-api-key"
lotr = lotr.Client(api_key=api_key)
characters=lotr.get_characters(params="name=Gandalf")
print(f"{characters}\n")
```

## SDK Documentation

# Supported functions

| Function | (Parameter=default) | Description |
| ----------- | ----------- | ----------- |
| get_books | (params=None) | List of all "The Lord of the Rings" books. |
| get_book | (id) | Get one specific book. `id` is the id of the book e.g. 5cf5805fb53e011a64671582 |
| get_movies | (params=None) | List of all movies. |
| get_movie | (id) | Get one specific movie. `id` is the id of the movie e.g. 5cd95395de30eff6ebccde5d |
| get_characters | (params=None) | List of characters including metadata like name, gender, realm, race and more. |
| get_character | (id) | Get one specific character. `id` is the id of the character e.g. 5cd99d4bde30eff6ebccfe9e |
| get_chapters | (params=None) | List of all book chapters. |
| get_chapter | (id) | Get one specific book chapter. `id` is the id of the book chapter e.g. 6091b6d6d58360f988133b8b |
| get_book_chapters | (id, params=None) | Get all chapters of one specific book. id is the id of the book e.g. 5cf5805fb53e011a64671582 |
| get_quotes | (params=None) | List of quotes from all movies. |
| get_quote | (id) | Get one specific movie quote. `id` is the id of the quote e.g. 5cd96e05de30eff6ebcce7ff |
| get_movie_quotes | (id, params=None) | List of quotes from one movie. `id` is the id of the movie e.g. 5cd95395de30eff6ebccde5d|
| get_character_quotes | (id, params=None) | List of quotes of one character. `id` is the id of the character e.g. 5cd99d4bde30eff6ebccfe9e|
| get_paginator | (resource, page_size=1000, sort=None, id=None) | `resource` is one of `books`, `chapters`, `book_chapters`, `characters`, `movies`, `quotes`, `movie_quotes`, `character_quotes`. `id` should only be specified when `resource` is one of `book_chapters`, `movie_quotes`, `character_quotes`. `sort` specifies the sort order e.g. `sort=character:desc` or `sort=name:asc`|

# Pagination
Pagination is supported for the functions that return more than one record.
Use the `get_paginator` to get a paginator iterator and then iterate through it. See the pagination example above.

## Open Issues and Missing Code:
- Tests tests tests...
- Request Timeout and Retry
- offset parameter in the API does not appear to work with pagination - investigate this and later add the offset to the SDK
- More robust filters and filters validation
- add filtering with pagination too

