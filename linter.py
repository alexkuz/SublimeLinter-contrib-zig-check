from SublimeLinter.lint import Linter, STREAM_STDERR
import sublime
import os


class SublimeLinterZigCheck(Linter):
    name = 'zigcheck'
    regex = r'^(?P<filename>\<stdin\>|[^\s\:]+):(?P<line>\d+):(?P<col>\d+):\s+error:\s+(?P<message>.*)$'
    multiline = False
    defaults = {
        'selector': 'source.zig'
    }
    error_stream = STREAM_STDERR

    def split_match(self, match):
        filename = match.group('filename')
        values = super().split_match(match)

        if self.is_stdin_filename(filename):
            return values

        if not os.path.isabs(filename):
            cwd = self.get_working_dir() or os.getcwd()
            filename = os.path.join(cwd, filename)

        filename = os.path.normpath(filename)

        if (filename != self.view.file_name()):
            return None

        return values


    def cmd(self):
        build_cmd = self.settings.get("build-cmd")
        if build_cmd and not self.view.is_dirty():
            return build_cmd
        else:
            return ('zig', 'ast-check', '--color', 'off')

