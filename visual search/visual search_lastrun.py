#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 31, 2020, at 15:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'visual search'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ning\\Documents\\python works\\psychopy_experiments\\visual search\\visual search_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
intr_1 = visual.TextStim(win=win, name='intr_1',
    text="Press 'up' if target is the same as original",
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_2 = visual.TextStim(win=win, name='instr_2',
    text="Press 'left' if target rotates to the left compared to the original",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_3 = visual.TextStim(win=win, name='instr_3',
    text="Press 'right' if target rotates to the right compared to the original",
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
proceed = keyboard.Keyboard()

# Initialize components for Routine "experiment"
experimentClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
target = visual.GratingStim(
    win=win, name='target',
    tex='sin', mask='circle',
    ori=1.0, pos=(0.5, 0), size=(0.5, 0.5), sf=[4,5], phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-1.0)
original = visual.GratingStim(
    win=win, name='original',
    tex='sin', mask='circle',
    ori=1.0, pos=(-0.5, 0), size=(0.5, 0.5), sf=[4,5], phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=-2.0)
instruction_1 = visual.TextStim(win=win, name='instruction_1',
    text="Press 'up' if target is the same as original",
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
response = keyboard.Keyboard()
instruction_2 = visual.TextStim(win=win, name='instruction_2',
    text="Press 'left' if target rotates to the left compared to the original\n",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
instruction_3 = visual.TextStim(win=win, name='instruction_3',
    text="Press 'right' if target rotates to the right compared to the original",
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
label_original = visual.TextStim(win=win, name='label_original',
    text='Original',
    font='Arial',
    pos=(-0.5, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
label_target = visual.TextStim(win=win, name='label_target',
    text='Target',
    font='Arial',
    pos=(0.5, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(-0.7, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
# update component parameters for each repeat
proceed.keys = []
proceed.rt = []
# keep track of which components have finished
instructionComponents = [intr_1, instr_2, instr_3, proceed]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intr_1* updates
    if intr_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intr_1.frameNStart = frameN  # exact frame index
        intr_1.tStart = t  # local t and not account for scr refresh
        intr_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intr_1, 'tStartRefresh')  # time at next scr refresh
        intr_1.setAutoDraw(True)
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    
    # *instr_3* updates
    if instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.tStart = t  # local t and not account for scr refresh
        instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
        instr_3.setAutoDraw(True)
    
    # *proceed* updates
    waitOnFlip = False
    if proceed.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        proceed.frameNStart = frameN  # exact frame index
        proceed.tStart = t  # local t and not account for scr refresh
        proceed.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed, 'tStartRefresh')  # time at next scr refresh
        proceed.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed.status == STARTED and not waitOnFlip:
        theseKeys = proceed.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            proceed.keys = theseKeys.name  # just the last key pressed
            proceed.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intr_1.started', intr_1.tStartRefresh)
thisExp.addData('intr_1.stopped', intr_1.tStopRefresh)
thisExp.addData('instr_2.started', instr_2.tStartRefresh)
thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
thisExp.addData('instr_3.started', instr_3.tStartRefresh)
thisExp.addData('instr_3.stopped', instr_3.tStopRefresh)
# check responses
if proceed.keys in ['', [], None]:  # No response was made
    proceed.keys = None
thisExp.addData('proceed.keys',proceed.keys)
if proceed.keys != None:  # we had a response
    thisExp.addData('proceed.rt', proceed.rt)
thisExp.addData('proceed.started', proceed.tStartRefresh)
thisExp.addData('proceed.stopped', proceed.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment matrix.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "experiment"-------
    # update component parameters for each repeat
    target.setOri(gabor)
    original.setOri(conditions)
    response.keys = []
    response.rt = []
    text.setText(trials)
    # keep track of which components have finished
    experimentComponents = [Fixation, target, original, instruction_1, response, instruction_2, instruction_3, label_original, label_target, text]
    for thisComponent in experimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "experiment"-------
    while continueRoutine:
        # get current time
        t = experimentClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *original* updates
        if original.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            original.frameNStart = frameN  # exact frame index
            original.tStart = t  # local t and not account for scr refresh
            original.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(original, 'tStartRefresh')  # time at next scr refresh
            original.setAutoDraw(True)
        if original.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > original.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                original.tStop = t  # not accounting for scr refresh
                original.frameNStop = frameN  # exact frame index
                win.timeOnFlip(original, 'tStopRefresh')  # time at next scr refresh
                original.setAutoDraw(False)
        
        # *instruction_1* updates
        if instruction_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruction_1.frameNStart = frameN  # exact frame index
            instruction_1.tStart = t  # local t and not account for scr refresh
            instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_1, 'tStartRefresh')  # time at next scr refresh
            instruction_1.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['left', 'right', 'up'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                response.keys = theseKeys.name  # just the last key pressed
                response.rt = theseKeys.rt
                # was this 'correct'?
                if (response.keys == str('corrAns')) or (response.keys == 'corrAns'):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *instruction_2* updates
        if instruction_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruction_2.frameNStart = frameN  # exact frame index
            instruction_2.tStart = t  # local t and not account for scr refresh
            instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_2, 'tStartRefresh')  # time at next scr refresh
            instruction_2.setAutoDraw(True)
        
        # *instruction_3* updates
        if instruction_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruction_3.frameNStart = frameN  # exact frame index
            instruction_3.tStart = t  # local t and not account for scr refresh
            instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_3, 'tStartRefresh')  # time at next scr refresh
            instruction_3.setAutoDraw(True)
        
        # *label_original* updates
        if label_original.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_original.frameNStart = frameN  # exact frame index
            label_original.tStart = t  # local t and not account for scr refresh
            label_original.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_original, 'tStartRefresh')  # time at next scr refresh
            label_original.setAutoDraw(True)
        if label_original.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > label_original.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                label_original.tStop = t  # not accounting for scr refresh
                label_original.frameNStop = frameN  # exact frame index
                win.timeOnFlip(label_original, 'tStopRefresh')  # time at next scr refresh
                label_original.setAutoDraw(False)
        
        # *label_target* updates
        if label_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_target.frameNStart = frameN  # exact frame index
            label_target.tStart = t  # local t and not account for scr refresh
            label_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_target, 'tStartRefresh')  # time at next scr refresh
            label_target.setAutoDraw(True)
        if label_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > label_target.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                label_target.tStop = t  # not accounting for scr refresh
                label_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(label_target, 'tStopRefresh')  # time at next scr refresh
                label_target.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experiment"-------
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Fixation.started', Fixation.tStartRefresh)
    trials.addData('Fixation.stopped', Fixation.tStopRefresh)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    trials.addData('original.started', original.tStartRefresh)
    trials.addData('original.stopped', original.tStopRefresh)
    trials.addData('instruction_1.started', instruction_1.tStartRefresh)
    trials.addData('instruction_1.stopped', instruction_1.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str('corrAns').lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    trials.addData('response.started', response.tStartRefresh)
    trials.addData('response.stopped', response.tStopRefresh)
    trials.addData('instruction_2.started', instruction_2.tStartRefresh)
    trials.addData('instruction_2.stopped', instruction_2.tStopRefresh)
    trials.addData('instruction_3.started', instruction_3.tStartRefresh)
    trials.addData('instruction_3.stopped', instruction_3.tStopRefresh)
    trials.addData('label_original.started', label_original.tStartRefresh)
    trials.addData('label_original.stopped', label_original.tStopRefresh)
    trials.addData('label_target.started', label_target.tStartRefresh)
    trials.addData('label_target.stopped', label_target.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
