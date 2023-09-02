import pupbeams
import pupscale
import pupmotors
import pupbuttons
from enum import Enum

def main():

    pupbeams.InitBeams()
    pupbeams.TestBeams()

    States = Enum('States', [ 'TOP', 'BOTTOM', 'LIFTING', 'LOWERING' ])
    state = States.BOTTOM
    
    while True:

        match (state):

            case States.TOP:

                if pupbuttons.IsDownButtonPressed():
                    state = States.LOWERING
                    pupmotors.LowerLift()
                    pupscale.MeasureWeight()
                    state = States.BOTTOM

                elif pupbeams.IsTopBeamBroken():
                    while pupbeams.IsTopBeamBroken():
                        pass
                    state = States.LOWERING
                    pupmotors.LowerLift()
                    pupscale.MeasureWeight()
                    state = States.BOTTOM

            case States.BOTTOM:
                
                if pupbuttons.IsUpButtonPressed():
                    state = States.LIFTING
                    pupmotors.RaiseLift()
                    pupscale.MeasureWeight()
                    state = States.TOP

                elif pupbeams.IsBottomBeamBroken():
                    while pupbeams.IsBottomBeamBroken():
                        pass
                    state = States.LIFTING
                    pupmotors.RaiseLift()
                    pupscale.MeasureWeight()
                    state = States.TOP
                
            case _:
                pass


if __name__ == "__main__":
    main()