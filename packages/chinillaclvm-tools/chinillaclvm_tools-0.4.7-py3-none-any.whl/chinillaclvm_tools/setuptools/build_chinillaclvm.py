from distutils.cmd import Command
from distutils import log

from setuptools.dist import Distribution

from chinillaclvm_tools.chinillaclvmc import compile_chinillaclvm


Distribution.chinillaclvm_extensions = ()


class build_chinillaclvm(Command):
    """ Command for building chinillaclvm """

    description = "build chinillaclvm extensions"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        file_list = self.distribution.chinillaclvm_extensions
        for _ in file_list:
            log.info("build_chinillaclvm on %s" % _)
            target = "%s.hex" % _
            compile_chinillaclvm(_, target)
