""" Control Widgets.  Presently comprises a Vertical Slider Demo and derivatives.

    HorizontalDemoSlider and HorizontalDemoSlider2 added by Bill Winder
    AreaDemoSlider and AreaDemoSlider2 added by Bill Winder

    Copyright (C) 2008, 2009, 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
    Copyright (C) 2010 - Cedric Gestes <gestes@aldebaran-robotics.com>
    Copyright (C) 2009, 2010 - Bill Winder <wgwinder@gmail.com>


    To do: All controls with draggable=True do not fire the OnFocus methon on single click.
    the control does not activate the OnFocus method. Clicking the handle does fire OnFocus, however.

"""

print "WARNING: Controls.py is deprecated and split into AreaSlider, Control, etc."

from gwt.Control import Control
from gwt.DoubleControl import DoubleControl as DControl
from gwt.VerticalSlider import VerticalSlider as VerticalDemoSlider
from gwt.InputControl import InputControl
from gwt.HorizontalSlider import HorizontalSlider as HorizontalDemoSlider
from gwt.AreaSlider import AreaSlider as AreaDemoSlider

class VerticalDemoSlider2(VerticalDemoSlider):

    def __init__(self, min_value, max_value, start_value=None, **kwargs):

        VerticalDemoSlider.__init__(self, min_value, max_value, start_value,
                                    **kwargs)
        self.setDragable(True)


class HorizontalDemoSlider2(HorizontalDemoSlider):
    def __init__(self, min_value, max_value, start_value=None, **kwargs):

        HorizontalDemoSlider.__init__(self, min_value, max_value, start_value,
                                    **kwargs)
        self.setDragable(True)

class AreaDemoSlider2(AreaDemoSlider):
    def __init__(self, min_value, max_value, start_value=None, **kwargs):

        AreaDemoSlider.__init__(self, min_value, max_value, start_value,
                                    **kwargs)
        self.setDragable(True)
