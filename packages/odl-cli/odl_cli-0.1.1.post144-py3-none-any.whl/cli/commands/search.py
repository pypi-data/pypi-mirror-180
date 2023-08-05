"""
一个命令的实现例子

Examples:
    $python cli.py rm  -y  openmmlab/flying3d

"""

from commands.cmdbase import CmdBase
from commons.stdio import print_stdout


class Search(CmdBase):

    def __init__(self):
        self.__config = None

    def init_parser(self, subparsers):
        """
        Initialize the parser for the command
        document : https://docs.python.org/zh-cn/3/library/argparse.html#

        Args:
            subparsers:

        Returns:

        """
        search_parser = subparsers.add_parser(
            'search',
            help='search dataset in a desired manner',
        )  # example 样例文件位于resources/下，普通的文本文件，每个命令写一个

        return search_parser

    def cmd_entry(self, cmdargs, config, *args, **kwargs):
        """
        Entry point for the command

        Args:
            self:
            cmdargs:
            config:

        Returns:

        """
        print_stdout("""CIFAR-10-Auto
CIFAR-10
CIFAR-100
Fashion-MNIST
STL-10""")
