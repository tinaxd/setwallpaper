import platform

set_wallpaper = None

_OS = platform.system()
if _OS == 'Windows':
    from .win import set_wallpaper as _set_wallpaper
    set_wallpaper = _set_wallpaper
else:
    raise Exception(f'not yet implemented for {_OS}')
