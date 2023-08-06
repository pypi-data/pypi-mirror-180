import dataclasses
import os
import os.path
import types
import webbrowser
from typing import List, Optional

import click
import pkg_resources

import tmt
import tmt.options
import tmt.steps
import tmt.steps.report

HTML_TEMPLATE_PATH = pkg_resources.resource_filename(
    'tmt', 'steps/report/html/template.html.j2')

jinja2: Optional[types.ModuleType] = None


def import_jinja2() -> None:
    """
    Import jinja2 module only when needed

    Until we have a separate package for each plugin.
    """
    global jinja2
    try:
        import jinja2
    except ImportError:
        raise tmt.utils.ReportError(
            "Missing 'jinja2', fixable by 'pip install tmt[report-html]'")


@dataclasses.dataclass
class ReportHtmlData(tmt.steps.report.ReportStepData):
    open: bool = False


@tmt.steps.provides_method('html')
class ReportHtml(tmt.steps.report.ReportPlugin):
    """
    Format test results into an html report

    Example config:

        report:
            how: html
            open: true
    """

    _data_class = ReportHtmlData

    @classmethod
    def options(cls, how: Optional[str] = None) -> List[tmt.options.ClickOptionDecoratorType]:
        """ Prepare command line options for the html report """
        return [
            click.option(
                '-o', '--open', is_flag=True,
                help='Open results in your preferred web browser.'),
            click.option(
                '--absolute-paths',
                is_flag=True,
                help='Make paths absolute rather than relative to working directory.')
            ] + super().options(how)

    def prune(self) -> None:
        """ Do not prune generated html report """
        pass

    def go(self) -> None:
        """ Process results """
        super().go()

        import_jinja2()
        assert jinja2

        # Prepare the template
        environment = jinja2.Environment()
        environment.filters["basename"] = lambda x: os.path.basename(x)

        if self.opt('absolute-paths'):
            environment.filters["linkable_path"] = os.path.abspath
        else:
            # Links used in html should be relative to a workdir
            environment.filters["linkable_path"] = lambda x: os.path.relpath(x, self.workdir)

        environment.trim_blocks = True
        environment.lstrip_blocks = True
        with open(HTML_TEMPLATE_PATH) as file:
            template = environment.from_string(file.read())

        # Write the report
        filename = 'index.html'
        self.write(
            filename,
            data=template.render(
                results=self.step.plan.execute.results(),
                base_dir=self.step.plan.execute.workdir,
                plan=self.step.plan))

        # Nothing more to do in dry mode
        if self.opt('dry'):
            return

        # Show output file path
        assert self.workdir is not None
        target = os.path.join(self.workdir, filename)
        self.info("output", target, color='yellow')
        if not self.get('open'):
            return

        # Open target in webbrowser
        try:
            if webbrowser.open(f"file://{target}", new=0):
                self.info(
                    'open', 'Successfully opened in the web browser.',
                    color='green')
                return
            self.fail("Failed to open the web browser.")
        except Exception as error:
            self.fail(f"Failed to open the web browser: {error}")

        raise tmt.utils.ReportError("Unable to open the web browser.")
