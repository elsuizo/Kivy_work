#= -------------------------------------------------------------------------
# @file game1.py
#
# @date 11/17/15 23:12:50
# @author Martin Noblia
# @email martin.noblia@openmailbox.org
#
# @brief
#
# @detail
#
#  Licence:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License

#---------------------------------------------------------------------------=#

from kivy.app import App
from kivy.uix.widget import Widget

class Game(Widget):
    pass

class GameApp(App):
    def build(self):
        return Game()

if __name__ == "__main__":
    GameApp().run()
