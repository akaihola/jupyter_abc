def render_abc(abc: str, show_source: bool = False) -> str:
    """Create Javascript code for rendering ABC music notation

    :param abc: The ABC source code to render into music notation
    :param show_source: ``True`` to include the original ABC music notation
                        source code in the cell output
    :return: The Javascript code as a single string

    """
    output = ['element.prepend("<div class=\'abc\'></div>");',
              'ABCJS.renderAbc(element.find(".abc").get(0), "{}");'
              .format(abc.replace('\n', r'\n'))]
    if show_source:
        output.insert(1,
                      'element.prepend("<pre>{}</pre>");'
                      .format(abc.replace('\n', '<br />')))
    return ''.join(output)
