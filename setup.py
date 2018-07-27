from setuptools import setup

setup(
    data_files=[('share/jupyter/nbextensions/jupyter-abc',
                 ['jupyter_abc/static/abcjs_basic_5.1.2-min.js'])]
    # The rest of the setuptools configuration comes from `setup.cfg`. The
    # `data_files` argument is here since it's not yet supported in
    # `setup.cfg`.
)
