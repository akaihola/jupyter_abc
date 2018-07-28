def render_abc(abc: str, show_source: bool = False) -> str:
    """Create Javascript code for rendering ABC music notation

    :param abc: The ABC source code to render into music notation
    :param show_source: ``True`` to include the original ABC music notation
                        source code in the cell output
    :return: The Javascript code as a single string

    """
    abc_js = abc.replace('\n', r'\n')
    output = [
        'require(["abcjs"], function(ABCJS) {',
        '    element.prepend("<div class=\'abc\'></div>");',
        '    var output = element.find(".abc").get(0);',
        '    console.log(element, output, ABCJS, "{}");'.format(abc_js),
        '    ABCJS.renderAbc(output, "{}");'.format(abc_js),
        '});']
    if show_source:
        output.insert(3,
                      'element.prepend("<pre>{}</pre>");'
                      .format(abc.replace('\n', '<br />')))
    return ''.join(output)
