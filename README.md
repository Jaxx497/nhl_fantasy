# NHL/FANTASY VISUALIZER

### Usage
Simple to use. If in a public league, simply enter your league_id within `auth.py` before running `main.py` (main). If the league is private, `swid` and `espn_2` cookie information must be pulled from browser and also placed in their respsective variable names.

### About
Simple CLI program written in Python which updates and displays both current NHL information as well as any ESPN fantasy league information as well. Pulls from both the official NHL API as well as multiple ESPN API. 

Version 0.1 is proof of concept. Functionally the program is able to do what it set out to do: the program collects all necessary data and can be printed however the user likes. The next big step is to find a better display for the information, including much information that does not currently display on the CLI, but is held in memory. ~~Considering a Flask front-end implementation of this program.~~

## Next Steps

I've begun working on v0.2 which is written in Rust with the Yew framework and displays information in a webpage rather than the console. I've been met with several hurdles trying to do this but progress is being made. I hope to have a release out by Jan 2023. 
