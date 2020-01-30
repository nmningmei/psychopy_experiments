#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 30, 2020, at 15:40
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
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'im_size': '1024', 'premask': '0', 'postmask': '2'}
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
    originPath='C:\\Users\\ning\\Documents\\python works\\psychopy_experiments\\blind sight\\test.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
intro = visual.TextStim(win=win, name='intro',
    text='you will be asked "left" or "right" by pressing "<-" or "->"\n\nyou will be asked visibility:\n    1. unconscious\n    2. glimpse\n    3. conscious\n\npress "space" to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
to_start = keyboard.Keyboard()

# Initialize components for Routine "present_gabor"
present_gaborClock = core.Clock()
grating = visual.GratingStim(
    win=win, name='grating',units='pix', 
    tex='sin', mask='sin',
    ori=1.0, pos=(0, 0), size=1.0, sf=1.0, phase=0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,blendmode='avg',
    texRes=128, interpolate=False, depth=0.0)
im_size = int(expInfo['im_size'])

premask = int(expInfo['premask'])
postmask = int(expInfo['postmask'])

k = 210
mask_directions = [k,k + 90]



# Initialize components for Routine "response"
responseClock = core.Clock()
left_right = keyboard.Keyboard()
message = visual.TextStim(win=win, name='message',
    text='<->',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "visibility"
visibilityClock = core.Clock()
visible = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
# update component parameters for each repeat
to_start.keys = []
to_start.rt = []
# keep track of which components have finished
introductionComponents = [intro, to_start]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro* updates
    if intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro.frameNStart = frameN  # exact frame index
        intro.tStart = t  # local t and not account for scr refresh
        intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro, 'tStartRefresh')  # time at next scr refresh
        intro.setAutoDraw(True)
    
    # *to_start* updates
    waitOnFlip = False
    if to_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        to_start.frameNStart = frameN  # exact frame index
        to_start.tStart = t  # local t and not account for scr refresh
        to_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(to_start, 'tStartRefresh')  # time at next scr refresh
        to_start.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(to_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if to_start.status == STARTED and not waitOnFlip:
        theseKeys = to_start.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro.started', intro.tStartRefresh)
thisExp.addData('intro.stopped', intro.tStopRefresh)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.csv'),
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
    
    # ------Prepare to start Routine "present_gabor"-------
    # update component parameters for each repeat
    grating.setOpacity(opacity)
    grating.setSize((int(expInfo['im_size']), int(expInfo['im_size'])))
    grating.setOri(orientation)
    grating.setMask(mask)
    grating.setSF(spatial_freq)
    grating.contrast = contrast
    #gabor_tex = (
    #visual.filters.makeGrating(res = im_size,
    #    cycles = im_size * spatial_freq) *
    #visual.filters.makeMask(matrixSize = im_size,
    #        shape = 'gauss',range=[0,.01]))
    #grating.tex = gabor_tex
    #grating.tex = np.random.random([im_size,im_size])*2. - 1.
    
    #np.random.shuffle(mask_directions)
    #INITIALISE SOME STIMULI
    grating1 = visual.GratingStim(win, mask="gauss",
                                  color=[1.0, 1.0, 1.0],
                                  opacity=1.0,
                                  size=(im_size, im_size),
                                  units = 'pix',
                                  sf=(0.02,0), ori=mask_directions[0])
    
    grating2 = visual.GratingStim(win, mask="gauss",
                                  color=[1.0, 1.0, 1.0],
                                  opacity=0.5,
                                  size=(im_size, im_size),
                                  units = 'pix',
                                  sf=(.02,0), ori=mask_directions[1])
    
    
    trialClock = core.Clock()
    t = 0
    while t < premask:    # quits after some secs
    
        t = trialClock.getTime()
    
        grating1.setPhase(1*t)  # drift at 1Hz
        grating1.draw()  #redraw it
    
        grating2.setPhase(2*t)    #drift at 2Hz
        grating2.draw()  #redraw it
    
        win.flip()          #update the screen
    
        #handle key presses each frame
        for keys in event.getKeys():
            if keys in ['escape','q']:
                core.quit()
    # keep track of which components have finished
    present_gaborComponents = [grating]
    for thisComponent in present_gaborComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    present_gaborClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "present_gabor"-------
    while continueRoutine:
        # get current time
        t = present_gaborClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=present_gaborClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.setAutoDraw(True)
        if grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                grating.tStop = t  # not accounting for scr refresh
                grating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                grating.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in present_gaborComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "present_gabor"-------
    for thisComponent in present_gaborComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('grating.started', grating.tStartRefresh)
    trials.addData('grating.stopped', grating.tStopRefresh)
    
    trialClock = core.Clock()
    t = 0
    while t < postmask:    # quits after some secs
    
        t = trialClock.getTime()
    
        grating1.setPhase(1*t)  # drift at 1Hz
        grating1.draw()  #redraw it
    
        grating2.setPhase(2*t)    #drift at 2Hz
        grating2.draw()  #redraw it
    
        win.flip()          #update the screen
    
        #handle key presses each frame
        for keys in event.getKeys():
            if keys in ['escape','q']:
                core.quit()
    # the Routine "present_gabor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response"-------
    # update component parameters for each repeat
    left_right.keys = []
    left_right.rt = []
    # keep track of which components have finished
    responseComponents = [left_right, message]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "response"-------
    while continueRoutine:
        # get current time
        t = responseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_right* updates
        waitOnFlip = False
        if left_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_right.frameNStart = frameN  # exact frame index
            left_right.tStart = t  # local t and not account for scr refresh
            left_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_right, 'tStartRefresh')  # time at next scr refresh
            left_right.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(left_right.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(left_right.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if left_right.status == STARTED and not waitOnFlip:
            theseKeys = left_right.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                left_right.keys = theseKeys.name  # just the last key pressed
                left_right.rt = theseKeys.rt
                # was this 'correct'?
                if (left_right.keys == str(corrAns)) or (left_right.keys == corrAns):
                    left_right.corr = 1
                else:
                    left_right.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *message* updates
        if message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            message.frameNStart = frameN  # exact frame index
            message.tStart = t  # local t and not account for scr refresh
            message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(message, 'tStartRefresh')  # time at next scr refresh
            message.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if left_right.keys in ['', [], None]:  # No response was made
        left_right.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           left_right.corr = 1;  # correct non-response
        else:
           left_right.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('left_right.keys',left_right.keys)
    trials.addData('left_right.corr', left_right.corr)
    if left_right.keys != None:  # we had a response
        trials.addData('left_right.rt', left_right.rt)
    trials.addData('left_right.started', left_right.tStartRefresh)
    trials.addData('left_right.stopped', left_right.tStopRefresh)
    trials.addData('message.started', message.tStartRefresh)
    trials.addData('message.stopped', message.tStopRefresh)
    # the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "visibility"-------
    # update component parameters for each repeat
    visible.keys = []
    visible.rt = []
    # keep track of which components have finished
    visibilityComponents = [visible, text]
    for thisComponent in visibilityComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visibilityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "visibility"-------
    while continueRoutine:
        # get current time
        t = visibilityClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visibilityClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visible* updates
        waitOnFlip = False
        if visible.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            visible.frameNStart = frameN  # exact frame index
            visible.tStart = t  # local t and not account for scr refresh
            visible.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visible, 'tStartRefresh')  # time at next scr refresh
            visible.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(visible.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(visible.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if visible.status == STARTED and not waitOnFlip:
            theseKeys = visible.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                visible.keys = theseKeys.name  # just the last key pressed
                visible.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
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
        for thisComponent in visibilityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "visibility"-------
    for thisComponent in visibilityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if visible.keys in ['', [], None]:  # No response was made
        visible.keys = None
    trials.addData('visible.keys',visible.keys)
    if visible.keys != None:  # we had a response
        trials.addData('visible.rt', visible.rt)
    trials.addData('visible.started', visible.tStartRefresh)
    trials.addData('visible.stopped', visible.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # the Routine "visibility" was not non-slip safe, so reset the non-slip timer
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
