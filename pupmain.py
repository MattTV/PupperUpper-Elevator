import puplcd
import pupbeams
import pupscale
import pupmotors
import pupserver
import pupbuttons
import pupbaseline
import pupdatabase
from enum import Enum

def main():

    # Init Each Piece
    puplcd.InitLCD()
    pupbeams.InitBeams()
    pupmotors.InitMotors()
    pupbuttons.InitButtons()

    # Infinitely Looping Tests
    # pupbuttons.TestButtons()
    # pupbeams.TestBeams()
    # puplcd.TestLCD()
    # pupmotors.TestMotors()





    Locations = Enum('Locations', [ 'TOP', 'BOTTOM' ] )
    location = Locations.BOTTOM
    
    while True:

        # if pupbuttons.IsUpButtonPressed() and pupbuttons.IsDownButtonPressed():

        #     pupbaseline.ChangeBaseline()

        match(location):
            
            case Locations.BOTTOM:
                
                if pupbuttons.IsUpButtonPressed() or pupbeams.IsBottomBeamBroken():

                    # Wait until the beams are clear
                    while pupbeams.IsBottomBeamBroken() or pupbeams.IsTopBeamBroken():
                        pass
                    
                    # Weighing and displaying process
                    MeasureRecordCheckDisplay()

                    # Raise the lift
                    pupmotors.RaiseLift()

                    # Set state to TOP
                    location = Locations.TOP
    
            case Locations.TOP:
                
                if pupbuttons.IsDownButtonPressed() or pupbeams.IsTopBeamBroken():
                    
                    # Wait until the beams are clear
                    while pupbeams.IsTopBeamBroken() or pupbeams.IsBottomBeamBroken():
                        pass
                        
                    # Weighing and displaying process
                    MeasureRecordCheckDisplay()

                    # Raise the lift
                    pupmotors.LowerLift()

                    # Set state to BOTTOM
                    location = Locations.BOTTOM

def MeasureRecordCheckDisplay():
    # Measure Weight
    weight = pupscale.MeasureWeight()

    # Add weight to DB
    pupdatabase.AddWeight(weight)

    # Post weight to server
    pupserver.PostWeight(weight)
    
    # Check if the weight is too high
    if weight >= pupdatabase.GetLatestBaseline() * 1.05:
        puplcd.WriteLCD("!!! WARNING !!!!\nOVERWEIGHT {weight}", 0, 0)

    elif weight <= pupdatabase.GetLatestBaseline() * 0.95:
        puplcd.WriteLCD("!!! WARNING !!!!\nUNDERWEIGHT {weight}", 0, 0)
    
    else:
        # Display weight on screen
        puplcd.WriteLCD("Current Weight:\n{weight} Pounds", 0, 0)

if __name__ == "__main__":
    main()
    