# H5-NewsTracker
A simple, Lightweight RSS ticker built using TKinter
# Design Structure
MVC: Model-View-Controller, is a well-known and wide practiced design paradigm for designing Graphical User Interfaces (GUI's). Using a MVC approach makes writing complex applications easier as software with this approach is more modular.

Tkinter: The default GUI framework of python. Although not the most beautiful around it does not require (complex) dependencies and is therefore very portable.
# Controller
A Controller serves as the logic hub of the application and as a bridge between a view and model.
# GUI
Frame: Non-interacting Frame widget.
View: interacting, requires a controller.
# Parser
Models store and manipulate data contained by the application. 

# Application flow
1. team5_rss_ticker.py calls rss.py
2. controller loads view
3. controller loads model
4. rss.py enters main loop
5. rss.py updates main loop
6. controller updates view
7. controller updates model

While in the main loop
1. Controller receives update
2. view listens for update from controller
3. view updates from controller

