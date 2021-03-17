import Definitions as D
import GenerateLibrary
import GenerateLipids
import tkinter as tk
import math
import time

Charge_Opts = D.Charge_Opts
classes = D.classes

def buttonpush():

    def write_to_file(spectrum_library):

        if D.Charge_Opts['POS'] == True: Poslibrary = open("Positive_Library.msp", "a")
        if D.Charge_Opts['NEG'] == True: Neglibrary = open("Negative_Library.msp", "a")

        count = 0

        for classes in spectrum_library:                                            
            for lipid in spectrum_library[classes]:
                for adduct in lipid:

                    if adduct['Ion_mode:'] == 'P' and D.Charge_Opts['POS'] == True:
                        for line in adduct:
                            if line == "peaks": Poslibrary.writelines([f"{peak[0]} {peak[1]}\n" for peak in adduct[line]]) # if spectra, whole thing can be written at once
                            else: Poslibrary.write(f"{line} {adduct[line]}\n") # Information is written one line at a time to look for where the spectra is  
                        Poslibrary.write("\n")
                        count += 1

                    if adduct['Ion_mode:'] == 'N' and D.Charge_Opts['NEG'] == True:
                        for line in adduct:
                            if line == "peaks": Neglibrary.writelines([f"{peak[0]} {peak[1]}\n" for peak in adduct[line]]) # if spectra, whole thing can be written at once
                            else: Neglibrary.write(f"{line} {adduct[line]}\n") # Information is written one line at a time to look for where the spectra is      
                        Neglibrary.write("\n")
                        count += 1
        
        try: Poslibrary.close()
        except: pass
        try: Neglibrary.close()
        except: pass

        return count

    t0 = time.time()

    print('Generating...')
    lib = GenerateLibrary.new_library(GenerateLipids.generate_lipids())
    print("Writing...")
    count = write_to_file(lib)

    t1 = time.time()
    
    print(f"Produced {count} spectra in {t1 - t0:.4f} seconds")   


root = tk.Tk()

button = tk.Button(root, text = "Push me", command = buttonpush)
button.pack()
tk.mainloop()