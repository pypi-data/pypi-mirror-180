from distutils import log
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):

    def __init__(self, *args):
        _build_ext.__init__(self, *args)

    def has_chinillaclvm_extensions(self):
        return (
            self.distribution.chinillaclvm_extensions
            and len(self.distribution.chinillaclvm_extensions) > 0
        )

    def check_extensions_list(self, extensions):
        if extensions:
            _build_ext.check_extensions_list(self, extensions)

    def run(self):
        """Run build_chinillaclvm sub command """
        if self.has_chinillaclvm_extensions():
            log.info("running build_chinillaclvm")
            build_chinillaclvm = self.get_finalized_command("build_chinillaclvm")
            build_chinillaclvm.inplace = self.inplace
            build_chinillaclvm.run()

        _build_ext.run(self)
