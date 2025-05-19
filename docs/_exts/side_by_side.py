from docutils import nodes
from docutils.parsers.rst import Directive, directives

class SideBySideDirective(Directive):
    has_content = True

    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        container = nodes.container(classes=['sphinx-side-by-side'])

        if 'class' in self.options:
            container['classes'].extend(self.options['class'])

        self.state.nested_parse(self.content, self.content_offset, container)
        return [container]

def setup(app):
    app.add_directive('side-by-side', SideBySideDirective)
    return {
        "parallel_read_safe": True,
    }

