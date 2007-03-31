#!/usr/bin/env python
# encoding: utf-8

import curses
import widget
import Form

DISABLE_ALL_COLORS    = False


class ThemeManager(object):
    def __init__(self):
        self._max_pairs = curses.COLOR_PAIRS - 1
        self._defined_pairs = {}
        self._names         = {}
        self.initialize_pairs()
        self.initialize_names()
    
    def setTheme(self, caller, request='DEFAULT'):
        if not curses.has_colors() or DISABLE_ALL_COLORS:
            return False

        # Locate the requested colour pair.  Default to default if not found.
        try:
            pair = self._defined_pairs[self._names[request]]
        except:
            pair = self._defined_pairs[self._names['DEFAULT']]

        # now make the actual attribute
        color_attribute = curses.color_pair(pair[0])
        
        # find the screen to operate on:
        if isinstance(caller, widget.Widget):
            pad = caller.parent.curses_pad
        elif isinstance(caller, Form.Form):
            pad = caller.curses_pad
        
        # Set the attribute
        pad.attron(color_attribute)
                
    def setDefault(self, caller):
        return False
        
    def initialize_pairs(self):
        # White on Black is fixed as color_pair 0
        self._defined_pairs['WHITE_BLACK'] = (0, curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        _colors_to_define = ( 
                    ('BLACK_WHITE',      curses.COLOR_BLACK,      curses.COLOR_WHITE),
                    ('BLUE_BLACK',       curses.COLOR_BLUE,       curses.COLOR_BLACK),
                    ('CYAN_BLACK',       curses.COLOR_CYAN,       curses.COLOR_BLACK),
                    ('GREEN_BLACK',      curses.COLOR_GREEN,      curses.COLOR_BLACK),
                    ('MAGENTA_BLACK',    curses.COLOR_MAGENTA,    curses.COLOR_BLACK),
                    ('RED_BLACK',        curses.COLOR_RED,        curses.COLOR_BLACK),
                    ('YELLOW_BLACK',     curses.COLOR_YELLOW,     curses.COLOR_BLACK),
                )
        for cp in _colors_to_define:
            self.initalize_pair(cp[0], cp[1], cp[2])
    
    def initialize_names(self):
        self._names['DEFAULT' ]  = 'WHITE_BLACK'
        self._names['NO_EDIT' ]  = 'BLUE_BLACK'
        self._names['STANDOUT']  = 'CYAN_BLACK'
    
    def initalize_pair(self, name, fg, bg):
        # Initialize a color_pair for the required colour and return the number. Raise an exception if this is not possible.
        if (len(self._defined_pairs.keys())+1) == self._max_pairs:
            raise Exception, "Too many colours"
        
        _this_pair_number = len(self._defined_pairs.keys()) + 1
        
        curses.init_pair(_this_pair_number, fg, bg)
        
        self._defined_pairs[name] = (_this_pair_number, fg, bg)
        
        return _this_pair_number
        
    def get_pair_number(self, name):
        return self._defined_pairs[name][0]