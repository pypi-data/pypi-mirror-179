# UnsplashX

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

UnsplashX is 

* an extremely simple **Unsplash** e**X**ploerer for Python.
* written in Python Standard Library

UnsplashX supports to

* get Unsplash Source's URL of a photo without the Official Unsplash API.




## Installation

```bash
pip install unsplashx
```



## Quickstart

```python
import unsplashx

unsplashx.source()
```



## License

UnsplashX has a BSD-3-Clause license, as found in the [LICENSE](https://github.com/imyizhang/unsplashx/blob/main/LICENSE) file.



## Documentation

### unsplashx.status

#### `unsplashx.status`

Unsplash API Status URL.



### unsplashx.changelog

#### `unsplashx.changelog`

Unsplash API Changelog URL.



### unsplashx.id

#### `unsplashx.id(link, verbose=False)`

Get the identifier given Unsplash share link URL.

> **Get the ID of a photo**
> ```
> https://unsplash.com/photos/{id}
> ```

> **Get the username of a user**
> ```
> https://unsplash.com/@{id}
> ```

> **Get the ID of a collection**
> ```
> https://unsplash.com/collections/{id}/{name}
> ```

**Parameters:**

* **link** (str): Unsplash share link URL of a photo, a user, or a collection. 
* **verbose** (bool, optional): Whether to enable verbose output. Defaults to `False`.

**Returns:**

(str): The identifier, that can be the ID of a photo, the username of a user, or the ID of a collection.



### unsplashx.source

#### `unsplashx.source(photo=None, user=None, collection=None, liked=None, featured=None, resolution=None, update=None, query=None, verbose=False)`

Get Unsplash Source download link URL of a photo given the parameters.

> **Get a random photo**
> ```
> https://source.unsplash.com/random
> ```
> Optionally, limit to a featured selection
> ```
> https://source.unsplash.com/featured
> ```
> Optionally, specify a size
> ```
> https://source.unsplash.com/{resolution}
> ```
> Optionally, limit to only updaing daily or weekly
> ```
> https://source.unsplash.com/{update}
> ```
> Optionally, limit to matching search terms
> ```
> https://source.unsplash.com/random?{query}
> ```
> Optionally, narrow the selection further
> ```
> https://source.unsplash.com/featured/{resolution}/{update}?{query}
> ```

> **Get a photo**
> ```
> https://source.unsplash.com/{id}
> ```
> Optionally, specify a size
> ```
> https://source.unsplash.com/{id}/{resolution}
> ```

> **Get a random photo from a user's photos**
> ```
> https://source.unsplash.com/user/{id}
> ```
> Optionally, narrow the selection further
> ```
> https://source.unsplash.com/user/{id}/featured/{resolution}/{update}
> ```

> **Get a random photo from a user's liked photos**
> ```
> https://source.unsplash.com/user/{id}/likes
> ```
> Optionally, specify a size
> ```
> https://source.unsplash.com/user/{id}/likes/{resolution}
> ```

> **Get a random photo from a collection's photos**
> ```
> https://source.unsplash.com/collection/{id}
> ```
> Optionally, narrow the selection further
> ```
> https://source.unsplash.com/collection/{id}/{resolution}/{update}
> ```

**Note:**

Unsplash Source is being deprecated. Existing uses will continue to work, however for new projects use the full Unsplash API.

**Parameters:**

* **photo** (str, optional): Unsplash share link URL or the ID of a photo.
* **user** (str, optional): Unsplash share link URL or the username of a user.
* **liked** (bool, optional): Whether to limit to a user's liked photos. Defaults to `False`.
* **collection** (str, optional): Unsplash share link URL or the ID of a collection.
* **featured** (bool, optional): Whether to limit to a featured selection. Defaults to `False`.
* **resolution** (str, optional): The size of a photo to be set. Formats to `{width}x{height}`. Defaults to `None`. 
* **update** (str, optional): Whether to limit to only updating daily or weekly. Defaults to `False`.
* **query** (str, optional): Comma-separated search terms. Defaults to `None`.
* **verbose** (bool, optional): Whether to enable verbose output. Defaults to `False`.

**Returns:**

(str): Unsplash Source download link URL of a photo.

**Reference:**

[1] https://changelog.unsplash.com/deprecations/2021/11/25/source-deprecation.html



## Contributing



## Changelog

**UnsplashX 0.1.0**

Made Unsplash Source's URL constructor functional.





[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/imyizhang/unsplashx



[pypi_badge]: https://badgen.net/pypi/v/unsplashx?icon=pypi&color=black&label
[pypi_link]: https://www.pypi.org/project/unsplashx