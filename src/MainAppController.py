
from MainAppView import MainAppView


class MainAppController(object):  


    def nothing(self):
        pass


    def init_view(self,root):
        """Initializes GUI view

            In addition it bindes the Buttons with the callback methods.

           
        """
        self.view = MainAppView(master=root)   
    
        # Bind buttons with callback methods
        self.view.one["command"] = self.nothing
        self.view.two["command"] = self.nothing
        self.view.three["command"] = self.nothing
        self.view.four["command"] = self.nothing

        # Start the gui 
        self.view.start_gui()
        


