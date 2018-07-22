from IPython.core.display import Javascript
from IPython.core.magic import cell_magic, Magics, magics_class

from jupyter_abc.render import render_abc


@magics_class
class JupyterAbcMagics(Magics):
    """Jupyter notebook magic commands for rendering music notation"""
    @cell_magic
    def abc(self, line: str, cell: str) -> Javascript:
        """The ``%%abc`` magic command for rendering ABC music notation

        If the first line of a cell starts with ``%%abc``, subsequent lines are
        interpreted as ABC notation and rendered as music using the ``abcjs``
        JavaScript library.

        :param line: The first line of the cell
        :param cell: The rest of the text in the cell
        :return: The Javascript code for rendering the music

        """
        arguments = line.split()
        show_source = '--source' in arguments or '-s' in arguments
        return Javascript(render_abc(cell, show_source=show_source))
