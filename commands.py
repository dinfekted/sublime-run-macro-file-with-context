import sublime
import sublime_plugin
from Context import context

class RunMacroFileWithContext(sublime_plugin.TextCommand):
  def run(self, edit, file):
    macro = sublime.decode_value(sublime.load_resource(file))
    for command in macro:
      args = None
      if 'args' in command:
        args = command['args']

      if 'context' in command and not context.check(self.view, command['context']):
        continue

      self.view.run_command(command['command'], args)