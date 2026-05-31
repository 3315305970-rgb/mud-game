# Basic commands

from evennia import Command

class CmdLook(Command):
    key = 'look'
    def func(self):
        self.caller.msg('You look around... (dynamic map support)')

# More commands: go, talk, status, etc.
