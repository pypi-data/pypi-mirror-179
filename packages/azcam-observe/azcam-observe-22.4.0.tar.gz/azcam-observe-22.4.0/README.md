# azcam-observe

*azcam-observe* is an *azcam* extension for running observing scripts. It can be used
with a Qt-based GUI or with a command line interface.

The *observe* command is usually executed from an console window. 

The Qt GUI uses the *PySide2* package.

## Code Documentation

See https://mplesser.github.io/docs/azcam_observe/.

## Installation

`pip install azcam-observe`

Or download from github: https://github.com/mplesser/azcam-observe.git.

## Usage

`observe.start()` to start the GUI.  A new window will open.

![GUI example after loading script file.](observe_gui.jpg)
*GUI example after loading script file.*

After starting the GUI, Press "Select Script" to find a script to load on disk. 
Then press "Load Script" to populate the table.  The excute, press Run.
You may Pause a script after the current command by pressing the Pause/Resume button. 
Then press the same button to resume the script.  The "Abort Script" button will 
abort the script as soon as possible.

If you have troubles, close the console window and start again.

## GUI Real-time Updates

   You may change a cell in the table to update values while a script is running.  Click in the cell, make the change and press "Enter" (or click elsewhere).
   
## Non-GUI Use

It is still possible to run *observe* without the GUI, although this mode is depricated.
   
## Examples

```python
observe.observe('/azcam/systems/90prime/ObservingScripts/bass.txt',1)
observe.move_telescope_during_readout=1
```

## Parameters

   Parameters may be changed from the command line as:
   
```python
observe.move_telescope_during_readout=1
observe.verbose=1
```

## Script Commands

Always use double quotes (") when needed
Comment lines start with # or !
Status integers are start of a script line are ignored or incremented

```
Observe scripts commands:
obs        ExposureTime ImageType Title NumberExposures Filter RA DEC Epoch
stepfocus  RelativeNumberSteps
steptel    RA_ArcSecs Dec_ArcSecs
movetel    RA Dec Epoch
movefilter FilterName
delay      NumberSecs
test       ExposureTime imagetype Title NumberExposures Filter RA DEC Epoch
print      "hi there"
prompt     "press any key to continue..."
quit       quit script

Example of a script:
obs 10.5 object "M31 field F" 1 u 00:36:00 40:30:00 2000.0 
obs 2.3 dark "a test dark" 2 u
stepfocus 50
delay 3.5
stepfocus -50
steptel 12.34 12.34
movetel 112940.40 +310030.0 2000.0
```
