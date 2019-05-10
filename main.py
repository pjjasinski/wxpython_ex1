#!/usr/bin/env python
import wx  # imports GUI lib

from gui_from_fbp import gui_frame  # imports gui created with wxformbuilder


class MainProgram(gui_frame):  # main inherits from gui_frame->wx.Frame
    def __init__(self, parent):  # constructor
        gui_frame.__init__(self, parent)  # calling base class wx.Frame constructor
        self.bind_events()  # bind gui events

    def bind_events(self):
        # this is events binding
        # button click will be bind to on_button_click method
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.m_button)

    def on_button_click(self, event):
        # this method is bind to button click
        self.m_staticText.SetLabel('button clicked')


# this section is where program starts
if __name__ == '__main__':
    app = wx.App(False)  # app class creation
    frame = MainProgram(None)  # my app
    frame.Show(True)  # show on the screen method
    app.MainLoop()  # call main loop

