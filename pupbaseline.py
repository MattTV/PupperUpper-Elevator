import puplcd
import pupbuttons

def ChangeBaseline():
    # TODO check number of characters
    puplcd.WriteLCD("^ Accept v Cancel")

    while pupbuttons.IsUpButtonPressed == False and pupbuttons.IsDownButtonPressed == False:
        # get the weight and display it continuously looping