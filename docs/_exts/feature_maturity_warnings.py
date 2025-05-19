from docutils.parsers.rst.directives.admonitions import Warning
from docutils.statemachine import StringList


class FeatureMaturityWarningDirective(Warning):
    has_content = False
    optional_arguments = 1
    message = ""

    def run(self):
        component = self.arguments[0] if len(self.arguments) > 0 else "This"
        self.content = StringList([self.message.format(component=component)])
        nodes = super().run()
        return nodes


class UnsupportedWarningDirective(FeatureMaturityWarningDirective):
    message = """
    {component} is an :ref:`unsupported<feature-maturity-level-definitions>`
    feature and is not supported for any level of use with any Isovalent
    Enterprise product. Consult with the :ref:`isovalent-support`
    team if you would still like to use it.
    """


class BetaWarningDirective(FeatureMaturityWarningDirective):
    message = """
    {component} is a :ref:`beta<feature-maturity-level-definitions>` feature
    and is only suitable for non-production environments. Support
    requests for this feature are limited to SEV-3. To participate in
    the beta program, contact :ref:`isovalent-support`.
    """


class LimitedWarningDirective(FeatureMaturityWarningDirective):
    message = """
    {component} is a :ref:`limited<feature-maturity-level-definitions>`
    feature and is only suitable for production environments in
    specific scenarios. Consult :ref:`isovalent-support` before using it.
    """


def setup(app):
    app.add_directive('unsupported-warning', UnsupportedWarningDirective)
    app.add_directive('beta-warning', BetaWarningDirective)
    app.add_directive('limited-warning', LimitedWarningDirective)

    return {
        "parallel_read_safe": True,
    }
