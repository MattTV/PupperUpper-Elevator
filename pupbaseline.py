import puplcd
import pupscale
import pupbuttons
import pupdatabase

def ChangeBaseline():
    # TODO check number of characters
    puplcd.WriteLCD("↑ = ✓      ↓ = X", 0, 1)

    stop = False

    while not stop:
        
        weight = pupscale.MeasureWeight()
        puplcd.WriteLCD(f'{weight} Pounds', 0, 0)
        
        if pupbuttons.IsUpButtonPressed():
            stop = True
            pupdatabase.AddBaseline(weight)
            
        elif pupbuttons.IsDownButtonPressed():
            stop = True