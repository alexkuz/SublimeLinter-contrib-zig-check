SublimeLinter-contrib-zig-check
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-zig-check.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-zig-check)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [zig ast-check](https://ziglang.org/) command. It will be used with files that have the “zig” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `zig` is installed on your system.

In order for `zig` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-contrib-zig-check settings:

| Setting  | Description   |
|:---------|:--------------|
| build&#8209;cmd | If set, this command will be executed on file save (to be precise, when file is not in "dirty" state) instead of default `zig ast-check`. This allows you to validate whole project with more detailed results. |

Example for `SublimeLinter.sublime-settings`:
```json
{
  "linters": {
    "zigcheck": {
      "build-cmd": "zig build-lib -fno-emit-bin ./src/main.zig"
    }
    ...
  }
}
```

Project-specific settings (`<my-project>.sublime-project`):
```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "SublimeLinter.linters.zigcheck.build-cmd": "zig build-lib -fno-emit-bin ./src/main.zig"
  }
}
```
