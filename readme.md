# RunMacroFileWithContext

Allows to use context in sublime macro files.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Usage

Whenever you want to use context in macro file change use
"run_macro_file_with_context" command instead of regular "run_macro_file".

Example command:

```
{
  "command": "run_macro_file_with_context",
  "args": {
    "file": "Packages/User/macro/mymacro.sublime-macro",
  }
},
```


### Dependencies

* [Context](https://github.com/shagabutdinov/sublime-context)