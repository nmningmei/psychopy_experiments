#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on June 08, 2017, at 20:19
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'visual search'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'D:\\NING - spindle\\psychopy_experiments\\visual search.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
intr_1 = visual.TextStim(win=win, name='intr_1',
    text="Press 'up' if target is the same as original",
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
instr_2 = visual.TextStim(win=win, name='instr_2',
    text="Press 'left' if target rotates to the left compared to the original",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
instr_3 = visual.TextStim(win=win, name='instr_3',
    text="Press 'right' if target rotates to the right compared to the original",
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "experiment"
experimentClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
target = visual.GratingStim(
    win=win, name='target',
    tex='sin', mask='circle',
    ori=1.0, pos=(0.5, 0), size=(0.5, 0.5), sf=[4,5], phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
original = visual.GratingStim(
    win=win, name='original',
    tex='sin', mask='circle',
    ori=1.0, pos=(-0.5, 0), size=(0.5, 0.5), sf=[4,5], phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
instruction_1 = visual.TextStim(win=win, name='instruction_1',
    text="Press 'up' if target is the same as original",
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
instruction_2 = visual.TextStim(win=win, name='instruction_2',
    text="Press 'left' if target rotates to the left compared to the original\n",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
instruction_3 = visual.TextStim(win=win, name='instruction_3',
    text="Press 'right' if target rotates to the right compared to the original",
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
label_original = visual.TextStim(win=win, name='label_original',
    text='Original',
    font='Arial',
    pos=(-0.5, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
label_target = visual.TextStim(win=win, name='label_target',
    text='Target',
    font='Arial',
    pos=(0.5, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text = visual.TextStim(win=win, name='text',
    text='default text',
    font=u'Arial',
    pos=(-0.7, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
proceed = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [intr_1, instr_2, instr_3, proceed]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intr_1* updates
    if t >= 0.0 and intr_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        intr_1.tStart = t
        intr_1.frameNStart = frameN  # exact frame index
        intr_1.setAutoDraw(True)
    
    # *instr_2* updates
    if t >= 0.0 and instr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_2.tStart = t
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.setAutoDraw(True)
    
    # *instr_3* updates
    if t >= 0.0 and instr_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_3.tStart = t
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.setAutoDraw(True)
    
    # *proceed* updates
    if t >= 1 and proceed.status == NOT_STARTED:
        # keep track of start time/frame for later
        proceed.tStart = t
        proceed.frameNStart = frameN  # exact frame index
        proceed.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(proceed.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if proceed.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            proceed.keys = theseKeys[-1]  # just the last key pressed
            proceed.rt = proceed.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if proceed.keys in ['', [], None]:  # No response was made
    proceed.keys=None
thisExp.addData('proceed.keys',proceed.keys)
if proceed.keys != None:  # we had a response
    thisExp.addData('proceed.rt', proceed.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'experiment matrix.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "experiment"-------
    t = 0
    experimentClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    target.setOri(gabor)
    original.setOri(conditions)
    response = event.BuilderKeyResponse()
    text.setText(trials)
    # keep track of which components have finished
    experimentComponents = [Fixation, target, original, instruction_1, response, instruction_2, instruction_3, label_original, label_target, text]
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "experiment"-------
    while continueRoutine:
        # get current time
        t = experimentClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.0 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # *target* updates
        if t >= 0.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)
        
        # *original* updates
        if t >= 0.0 and original.status == NOT_STARTED:
            # keep track of start time/frame for later
            original.tStart = t
            original.frameNStart = frameN  # exact frame index
            original.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if original.status == STARTED and t >= frameRemains:
            original.setAutoDraw(False)
        
        # *instruction_1* updates
        if t >= 1 and instruction_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_1.tStart = t
            instruction_1.frameNStart = frameN  # exact frame index
            instruction_1.setAutoDraw(True)
        
        # *response* updates
        if t >= 1 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'up'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # was this 'correct'?
                if (response.keys == str('corrAns')) or (response.keys == 'corrAns'):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *instruction_2* updates
        if t >= 1 and instruction_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_2.tStart = t
            instruction_2.frameNStart = frameN  # exact frame index
            instruction_2.setAutoDraw(True)
        
        # *instruction_3* updates
        if t >= 1 and instruction_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_3.tStart = t
            instruction_3.frameNStart = frameN  # exact frame index
            instruction_3.setAutoDraw(True)
        
        # *label_original* updates
        if t >= 0.0 and label_original.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_original.tStart = t
            label_original.frameNStart = frameN  # exact frame index
            label_original.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if label_original.status == STARTED and t >= frameRemains:
            label_original.setAutoDraw(False)
        
        # *label_target* updates
        if t >= 0.0 and label_target.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_target.tStart = t
            label_target.frameNStart = frameN  # exact frame index
            label_target.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if label_target.status == STARTED and t >= frameRemains:
            label_target.setAutoDraw(False)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experiment"-------
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
        # was no response the correct answer?!
        if str('corrAns').lower() == 'none':
           response.corr = 1  # correct non-response
        else:
           response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
