import sys

sys.path.append('../x64')
sys.path.insert(0, '..')
import Deliverable
deliverable = Deliverable.DELIVERABLE()

while True:
    deliverable.Run_Once()
