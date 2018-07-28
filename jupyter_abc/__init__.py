from string import Template
from typing import List, Dict

from IPython import InteractiveShell
from IPython.core.display import display, HTML
from pkg_resources import resource_listdir

from jupyter_abc.magics import JupyterAbcMagics


def find_abcjs() -> str:
    """Find the abcjs JavaScript file bundled with jupyter_abc

    The first file matching ``abcjs*.js`` in the ``static`` directory of the
    package is used. This way we can just replace the library with a newer
    version without updating the file name in Python code.

    :return: The HTTP path for the ``abcjs`` library inside the Jupyter server

    """
    static_files = resource_listdir('jupyter_abc', 'static')
    abcjs_filename = next(name for name in static_files
                          if name.startswith('abcjs') and name.endswith('.js'))
    return ('require.toUrl("nbextensions/jupyter-abc/{}")'
            .format(abcjs_filename))


def get_requirejs_configuration() -> str:
    """Generate configuration to use for ``require.config()``

    This is required for loading the ``abcjs`` Javascript library. The library
    is loaded using the ``requirejs`` library included in Jupyter Notebook.
    ``abcjs`` is bundled and minified using Webpack and can't be loaded
    directly with ``requirejs`` without specifying the path and the name of the
    exported global object.

    :return: The configuration object for ``require.config()`` as JavaScript
             code

    """
    return Template("""
        {paths: {abcjs: ${abcjs_url}},
         shim: {abcjs: {exports: 'ABCJS'}}}
    """).substitute(abcjs_url=find_abcjs())


INIT_JAVASCRIPT_TEMPLATE = Template(
    '<script type="text/javascript">'
    '    require.config(${requirejs_config});'
    '</script>')


def _jupyter_nbextension_paths() -> List[Dict[str, str]]:
    return [{'section': 'notebook',
             'src': 'static',
             'dest': 'jupyter-abc',
             'require': 'jupyter-abc/index'}]


def load_ipython_extension(ipython: InteractiveShell) -> None:
    """Initialize magics commands and initialize the ``abcjs`` library

    ``abcjs`` is initialized by loading the Javascript library and assigning it
    to the window global ``ABCJS``.

    :param ipython: The active IPython instance

    """
    ipython.register_magics(JupyterAbcMagics)
    init_script = INIT_JAVASCRIPT_TEMPLATE.substitute(
        requirejs_config=get_requirejs_configuration())
    display(HTML(init_script))
