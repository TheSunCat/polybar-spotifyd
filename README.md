# polybar-spotifyd
I had trouble getting Spotifyd songs on polybar so I made this.

## Usage
Click the text to pause/unpause.

Middle click for previous track.

Right click for next track.

I swear this is intuitive to me, but if it doesn't feel free to change it in the module definition.

## Setup
Install `spotifyd` from the AUR and set it up. You will also need `playerctl` and python.

Place `spotifyd.py` `inside ~/.config/polybar/`

Add the following module to your polybar config:
```toml
[module/spotifyd]
type = custom/script

exec = ~/.config/polybar/spotifyd.py
interval = 1

click-left = ~/.config/polybar/spotifyd.py toggleplay
click-middle = ~/.config/polybar/spotifyd.py previous
click-right = ~/.config/polybar/spotifyd
```

Finally, place the module somewhere in the polybar.
I used the following (very sophisticated) placement:
```toml
modules-center = spotifyd
```
Re-launch polybar (and witness next-generation text rendering).

I use `spotify-tui` to control Spotify, but you may use any client which supports spotifyd.

## Known issues
The interactions take a while. I don't think it's on my side, it seems either playerctl or spotifyd are just *really* slow sometimes.
