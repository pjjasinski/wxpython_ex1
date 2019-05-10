# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class gui_frame
###########################################################################

class gui_frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Example 1", pos=wx.DefaultPosition,
                          size=wx.Size(377, 112), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_button = wx.Button(self, wx.ID_ANY, u"Click me", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_button, 0, wx.ALL, 5)

        self.m_staticText = wx.StaticText(self, wx.ID_ANY, u"staticText", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText.Wrap(-1)
        bSizer16.Add(self.m_staticText, 0, wx.ALL, 5)

        self.SetSizer(bSizer16)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


