# Flask-Bootstrapless
Flask Bootstrap Template that auto-builds Bootstrap styles from LESS source

*Flask-Bootstrapless* is a convenient template to quickly create a
[Flask](http://flask.pocoo.org/) web application built from the
[Bootstrap 3](https://getbootstrap.com/) LESS source. The advantage to
building Bootstrap from source is that you can simply edit the LESS
variables file to globally change colors, styles, and other CSS throughout
the Bootstrap Framework.

*Flask-Bootstrapless* uses
[Flask-Assets](https://flask-assets.readthedocs.io/en/latest/), which means
that all static resources (LESS, JS, etc.) are pre-compiled, minified, and
cached for efficient handling of web requests. Assets are only
recompiled whenever a change is detected in the sourcecode.

## Installation

### Node.js

This template relies on `Node.js` to compile LESS to CSS. As such, you must
have [Node.js installed](https://nodejs.org/en/download/package-manager/)
on your system. With a working installation of Node.js, you can use `npm`
(Node's package manager) to install the first dependencies:

```shell
npm install -g less uglify-js less-plugin-autoprefix
```

These files are also listed in `npm-requirements.txt` and need not be installed
globally, but the above command provides the easiest form of installation.

### Python3

This Flask template is built to use Python3. As such, you must logically have
[Python3 installed](https://www.python.org/downloads/) on your system to run
this code. With a working installation of Python3, you can use `pip`
(Python's package manager) to install the remaining dependencies:

```shell
sudo pip3 install -r requirements.txt
```

All required Python packages are listed in `requirements.txt`, and the above
command provides the easiest form of installation.

## Usage

This template provides a boilerplate Bootstrap 3 implementation on Flask which
builds from LESS source. The important directories are as follows:

- `templates/` -- this directory contains sample Jinja2 Flask HTML templates
with a simple Bootstrap template. `layout.html` is the base layout and
`index.html` inherits from *layout*, providing a simple template for web
application pages.

- `static/styles/` -- this directory contains two files which are the basis of
styling for this application:
    - `variables.less` -- the truly magical component of this template; editing
    the LESS variables in this file will globally change all CSS styles in the
    Bootstrap implementation.
    - `custom-styles.less` -- this is a convenient place to store any custom CSS
    which you would like globally available throughout the application. Here, you
    have access to any LESS variables that have been declared in *variables* and
    Bootstrap LESS mixins. Vendor prefixes will automatically be applied during
    the pre-compilation process.

Have fun!
