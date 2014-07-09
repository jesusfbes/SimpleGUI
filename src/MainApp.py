#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

from MainAppController import MainAppController

def main():

    controller = MainAppController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')

    controller.init_view(root)


    print 'Bye Bye'



if __name__ == "__main__":
    main()