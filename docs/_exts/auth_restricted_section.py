from docutils import nodes
from docutils.parsers.rst import Directive

class AuthRestrictedStartDirective(Directive):
    has_content = False

    def run(self):
        container = nodes.container(classes=['sphinx-auth-restricted-start'])
        return [container]

class AuthRestrictedEndDirective(Directive):
    has_content = False

    def run(self):
        container = nodes.container(classes=['sphinx-auth-restricted-end'])
        return [container]

def setup(app):
    app.add_directive('auth-restricted-start', AuthRestrictedStartDirective)
    app.add_directive('auth-restricted-end', AuthRestrictedEndDirective)
    return {
        "parallel_read_safe": True,
    }
