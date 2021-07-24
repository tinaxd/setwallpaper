import ctypes

_User32 = ctypes.windll.User32

def set_wallpaper(filename: str) -> None:
    result = _User32.SystemParametersInfoW(
        0x0014,
        0,
        filename,
        0x0001
    )
