from SublimeLinter.lint import Linter, STREAM_STDERR


class SublimeLinterZigCheck(Linter):
    name = 'zig ast-check'
    cmd = ('zig', 'ast-check', '--color', 'off')
    regex = r'^<stdin>:(?P<line>\d+):(?P<col>\d+):\s+error:\s+(?P<message>.*)$'
    multiline = False
    defaults = {
        'selector': 'source.zig'
    }
    error_stream = STREAM_STDERR
