# Library Genesis EBook Downloader (LGED)

##### Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Examples](#examples)
    - [Accessing lged documentation](#lged-doc)
    - [Download ebooks by searching keyword](#lged-download)
- [Author](#author)

<br>

<a name="features"/>

# Features
| Status | Feature                                 |
| :----- | :-------------------------------------- |
| ✅     | download ebook by searching keyword     |
| ✅     | nice progress bar                       |
| ✅     | resume failed downloads                 |
| ✅     | skip already downloaded videos          |
| ✅     | all platforms                           |

<a name="prerequisites"/>

# Prerequisites
- [Python 3](https://www.python.org/downloads/)

<a name="installation"/>

# Installation
```cli
$ pip --no-cache-dir install lged
```
If you have multiple versions of python installed in your system, use **pip3** instead.
<!-- TODO: can someone confirm this is how the install would look with pip3? -->
```cli
$ pip3 --no-cache-dir install lged
```

### Running from local installation
```
lged --help
```

<a name="examples"/>

# Examples

<a name="lged-doc"/>

### Accessing lged documentation
```cli
$ lged --help
```

<a name="lged-download"/>

### Download ebooks by searching keyword

```cli

$ lged --keyword "Data Science"
```

<a name="author"/>

# Author
Feilong Cui
