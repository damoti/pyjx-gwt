# Date Time Example
# Copyright (C) 2009 Yit Choong (http://code.google.com/u/yitchoong/)
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

from gwt.Hyperlink import Hyperlink
from html5 import Factory
from gwt.Image import Image
from html5 import DOM
from gwt import Event
from gwt import MouseListener


class HyperlinkImage(Hyperlink):
    def __init__(self, img, **kwargs):
        self.mouseListeners = []
        if not kwargs.has_key('StyleName'):
            kwargs['StyleName'] = 'gwt-HyperlinkImage'
        Hyperlink.__init__(self, **kwargs)
        DOM.appendChild(DOM.getFirstChild(self.getElement()), img.getElement())
        img.unsinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS)

    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)

    def removeMouseListener(self,listener):
        self.mouseListeners.remove(listener)

    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type == 'mousedown' or type == 'mouseup' or type == 'mousemove' or type == 'mouseover' or type == 'mouseout':
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)
            # stop event falling through esp. for drag on image
            DOM.eventPreventDefault(event)

        else:
            Hyperlink.onBrowserEvent(self, event)

Factory.registerClass('gwt.HyperlinkImage', 'HyperlinkImage', HyperlinkImage)

