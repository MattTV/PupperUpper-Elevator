# import puplcd
import pupbeams
# import pupscale
# import pupmotors
import pupbuttons
# import pupbaseline
# import pupdatabase
# from enum import Enum

def main():

    # Tested Ok!
    # pupbuttons.InitButtons()
    # pupbuttons.TestButtons()

    # Tested Ok!
    # pupbeams.InitBeams()
    # pupbeams.TestBeams()

    # Locations = Enum('Locations', [ 'TOP', 'BOTTOM' ] )
    # location = Locations.BOTTOM
    
    # while True:

    #     if pupbuttons.IsUpButtonPressed() and pupbuttons.IsDownButtonPressed():

    #         pupbaseline.ChangeBaseline()

    #     match(location):
            
    #         case Locations.BOTTOM:
                
    #             if pupbuttons.IsUpButtonPressed() or pupbeams.IsBottomBeamBroken():

    #                 # Wait until the beam is clear
    #                 while pupbeams.IsBottomBeamBroken():
                        
    #                     # Weighing and displaying process
    #                     MeasureRecordCheckDisplay()

    #                     # Raise the lift
    #                     pupmotors.RaiseLift()

    #                     # Set state to TOP
    #                     location = Locations.TOP
    
    #         case Locations.TOP:
                
    #             if pupbuttons.IsDownButtonPressed() or pupbeams.IsTopBeamBroken():
    #                 while pupbeams.IsTopBeamBroken():
                        
    #                     # Weighing and displaying process
    #                     MeasureRecordCheckDisplay()

    #                     # Raise the lift
    #                     pupmotors.LowerLift()

    #                     # Set state to BOTTOM
    #                     location = Locations.BOTTOM

def MeasureRecordCheckDisplay():
    # Measure Weight
    weight = pupscale.MeasureWeight()

    # Add weight to DB
    pupdatabase.AddWeight(weight)
    
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
    