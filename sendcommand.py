import os
import sublime, sublime_plugin



class SendCommandCommand(sublime_plugin.TextCommand):

    def run(self,edit,cmd):
        os.system(cmd)
