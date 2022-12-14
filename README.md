# NHL/FANTASY VISUALIZER

### Usage
Simple to use. If in a public league, simply enter your league_id within `auth.py` before running `fantasy.py` (main). If the league is private, `swid` and `espn_2` cookie information must be pulled from browser. 

### About
Simple CLI program written in Python which updates and displays both current NHL information as well as any ESPN fantasy league information as well. Pulls from both the official NHL API as well as multiple ESPN API. 

Version 0.1 is proof of concept. Functionally the program is able to do what it set out to do. The next big step is to find a better display for the information, including much information that does not currently display on the CLI, but is held in memory. Considering a Flask front-end implementation of this program.  

Planning to add RECENT_GOALS, a function to display the 3 most recent goals with assist & timestamp info.

