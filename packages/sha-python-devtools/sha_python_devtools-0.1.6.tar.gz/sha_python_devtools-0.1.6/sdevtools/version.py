from importlib_metadata import PackageNotFoundError, version
# 用于从github动作中自动设置版本号
# 以及在本地测试时不中断
try:
    __version__ = version(__package__)  # type: ignore
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

VERSION = __version__
