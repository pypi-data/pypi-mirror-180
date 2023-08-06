# PyFeyn2

Forked from <https://pyfeyn.hepforge.org/>

PyFeyn is a Python-language based system for drawing Feynman diagrams. It was inspired by the C++ FeynDiagram system, and aims to provide the same functionality and quality of output as that, with the added benefits of a modern interpreted language, an improved interface and output direct to both EPS and PDF. Behind the scenes, PyFeyn uses the excellent PyX system - you can use PyX constructs in PyFeyn diagrams if you want, too.

## Dependencies

*   libmagickwand-dev (to display pdfs in a jupyter-notebook, might require a policy change of the imagemagick config for PDFs, see Troubleshooting)
*   latexmk
*   (feynmp-auto/feynmf)

## Installation

```sh
poerty install --with docs --with dev
poetry shell
```

## Documentation

*   <https://pyfeyn2.readthedocs.io/en/stable/>
*   <https://apn-pucky.github.io/pyfeyn2/index.html>

## Troubleshooting

*   [ImageMagick security policy 'PDF' blocking conversion]( https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion )

## Development


### package/python structure:

*   <https://mathspp.com/blog/how-to-create-a-python-package-in-2022>
*   <https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/>
