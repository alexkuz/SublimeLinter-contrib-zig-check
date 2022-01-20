from SublimeLinter.lint import Linter, STREAM_STDERR


class SublimeLinterZigCheck(Linter):
    name = 'zigcheck'
    regex = r'^(?P<filename>\<stdin\>|[^\s\:]+):(?P<line>\d+):(?P<col>\d+):\s+error:\s+(?P<message>.*)$'
    multiline = False
    defaults = {
        'selector': 'source.zig'
    }
    error_stream = STREAM_STDERR

    def cmd(self):
        build_cmd = self.settings.get("build-cmd")
        if build_cmd and not self.view.is_dirty():
            return build_cmd
        else:
            return ('zig', 'ast-check', '--color', 'off')

