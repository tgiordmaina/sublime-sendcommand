# sublime-sendcommand
Run a system command with sublime

# Install
Copy sendcommand.py to your Packages directory

# Key Binding
```
[
    {"keys" : ["ctrl+alt+r"],"command" : "send_command", "args" : {"cmd" : "nautilus"}},
     {"keys" : ["ctrl+alt+t"],"command" : "after_save_action", "args" : {"cmd" : "cmd.exe /c exit"}}
]
```