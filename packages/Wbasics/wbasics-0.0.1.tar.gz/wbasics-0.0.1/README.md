
# Wbasics

Wbasics just makes coding in python easier. Wbasics shortens things that would take too long to code for each time its needed.
## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)



## Installation

Install Wbasics with pip


  pip install Wbasics

    
## Usage/Examples

opening an app:
```python
import Wbasics as w

w.openapp("chrome")
```

using the wait command:
```python
import Wbasics as w

w.wait(20)
```

Text To Speech:
```python
import Wbasics as w

w.SpeakText("text")
```

Create a file:
```python
import Wbasics as w

w.createfile(filename)
```

Write to  a file:
```python
import Wbasics as w

w.writefile(filename,text)
```
Read a file:
```python
import Wbasics as w

w.readfile(filename)
```
Secure a script so that only a few users can use it:
```python
import Wbasics as w

alloweduserslist = ("me", "friend")

w.securescript(allowedusers)
```
Control a LG TV:
```python
import Wbasics as w

w.LGtvconnect(ip)
w.LGtvlaunch(App)
w.Lgtvvolume(updownmuteunmute, amount)
w.Lgtvpauseplay(pauseplay)
w.LGtvscreenswitch(onoff)
w.getchannellist()
w.changechannel(channelId)
```
Switch a webcam on/off:
```python
import Wbasics as w

w.webcamswitch(camnumb, windowname)
```
