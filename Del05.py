import sys

sys.path.append('../x64')
sys.path.insert(0, '..')
import Recorder
deliverable = Recorder.DELIVERABLE()

while True:
    deliverable.Run_Once()
