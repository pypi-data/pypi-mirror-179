from typing import List, Optional

from PySide6 import QtCore

from ..Constants.packaging_constants import PyinstallerArgs, pyinstaller_args_list
from .subprocess_tool import SubProcessTool


class Packaging(QtCore.QObject):
    """
    执行打包的类 \n
    """

    # 自定义信号
    args_settled = QtCore.Signal(list)

    def __init__(self, parent: Optional[QtCore.QObject] = None) -> None:
        """
        :param parent: 父控件对象
        """

        super(Packaging, self).__init__(parent)

        self.args_dict: dict = dict.fromkeys(pyinstaller_args_list, "")
        self._args: List[str] = []
        self.subprocess: SubProcessTool = SubProcessTool(self, program="pyinstaller")

    @QtCore.Slot(tuple)
    def set_pyinstaller_args(self, arg: tuple[str, str]) -> None:
        """
        解析传递来的PyInstaller运行参数，并添加至命令参数字典 \n
        :param arg: 运行参数
        """

        arg_key, arg_value = arg
        if arg_key in pyinstaller_args_list:
            self.args_dict[arg_key] = arg_value
            self._add_pyinstaller_args()

    def _add_pyinstaller_args(self) -> None:
        """
        将命令参数字典中的参数按顺序添加到命令参数列表中 \n
        """

        self._args = []  # 避免重复添加
        self._args.extend([self.args_dict[PyinstallerArgs.script_path]])
        if self.args_dict[PyinstallerArgs.icon_path]:
            self._args.extend(["--icon", self.args_dict[PyinstallerArgs.icon_path]])
        if self.args_dict[PyinstallerArgs.FD]:
            if self.args_dict[PyinstallerArgs.FD] == "One Dir":
                self._args.extend(["--onedir"])
            elif self.args_dict[PyinstallerArgs.FD] == "One File":
                self._args.extend(["--onefile"])
        if self.args_dict[PyinstallerArgs.console]:
            if self.args_dict[PyinstallerArgs.console] == "console":
                self._args.extend(["--console"])
            elif self.args_dict[PyinstallerArgs.console] == "windowed":
                self._args.extend(["--windowed"])
        if self.args_dict[PyinstallerArgs.out_name]:
            self._args.extend(["--name", self.args_dict[PyinstallerArgs.out_name]])

        self.args_settled.emit(self._args)

    def run_packaging_process(self) -> None:
        """
        使用给定的参数启动打包子进程 \n
        """

        self.subprocess.set_arguments(self._args)
        self.subprocess.start_process()
