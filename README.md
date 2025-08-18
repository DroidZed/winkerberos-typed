# Winkerberos typed

This package aims to make the SSO library [`winkerberos`](https://github.com/mongodb/winkerberos) more pythonic and user friendly.

It only includes a stub file (AI generated from the help(winkerberos) command) which improves the devloper experience.

PS: This package won't do anything on its own. You need the [original](https://github.com/mongodb/winkerberos/) for the full experience.

## Table of Contents

<ul>
  <li>
    <a href="#comparison">Comparison</a>
    <ul>
      <li><a href="#before-types">Before Types</a></li>
      <li><a href="#after-types">After Types</a></li>
    </ul>
  </li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#build">Build</a></li>
  <li><a href="#license">License</a></li>
</ul>

## Comparison

### Before types:

<img src="https://raw.githubusercontent.com/DroidZed/winkerberos-typed/refs/heads/main/images/before.png"  alt="before types" title="before"/>

### After types:

<img src="https://raw.githubusercontent.com/DroidZed/winkerberos-typed/refs/heads/main/images/after.png"  alt="after types" title="after"/>

## Installation:

Simply:

```sh
pip install winkerberos-typed

```

_or_

```sh
uv add winkerberos-typed

```

_or_

```sh
poetry add winkerberos-typed

```

## Build

1. Install `uv` by following [this link](https://docs.astral.sh/uv/getting-started/installation/).

2. Clone the project:

    ```sh
    git clone https://github.com/DroidZed/winkerberos-typed && cd winkerberos-typed
    ```

4. Build with `uv`:

    ```sh
    uv build
    ```

## License:

This project is licensed under the MIT license.
