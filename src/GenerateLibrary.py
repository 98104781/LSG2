import Definitions as D
import GenerateSpectra as S

Masses = D.Masses
classes = D.classes

def new_library(lipids):

    def new_spectra(key, lipid, adducts):

        def new_list():                                                             # .mgf format
            lst = {
            "Name:":f"{key} {'_'.join(str(nam) for nam in name)} {adduct}",
            "Spectrum_type:":"MS2",
            "Ion_mode:":Masses[adduct][1],
            "PrecursorMZ:":f"{mass + Masses[adduct][0]:.6f}",
            "Precursor_type:":adduct,
            "Num Peaks:":len(peaks),
            "peaks":peaks} 
            return lst       

        Mass = {                                                                    # If statements results into tuples, whereas dictionary gives floats.
         'Glycerol': 92.047344 + sum((tail[0] - Masses['H2O']) 
           for tail in lipid),                                                      # Sums tails for glycerolipids
         'SB': Masses['H2O'] + sum(tail[0] - Masses['H2O'] 
           for tail in lipid)}                                                      # Sums tails for sphingolipids
        mass = Mass[classes[key][1][1]]                                             # classes[key][1][1] is backbone
        if classes[key][1][2]: mass += (classes[key][1][2] - Masses['H2O'])         # Adds headgroup mass

        name = [tail[1] for tail in lipid]                                          # Put together the name from tail composition and class
        if len(name) < 2: name.append('0:0')                                        # Adds 0:0 to the name for Lyso GPLs / Sphingosines
        if key in ('MAG', 'DAG'): name.append('0:0')                                # Adds another 0:0 to the name for MAGs and DAGs to complement TAGs
        
        lst = []
        for adduct in adducts:
            if (D.Masses[adduct][1] == 'P' and D.Charge_Opts['POS']) or (D.Masses[adduct][1] == 'N' and D.Charge_Opts['NEG']):
                peaks = S.generate_peaks(key, mass, lipid, adduct)
                lst.append(new_list())
            else: pass
        return lst

    library = {}                                                                    # This is where the fragments will be stored
    for key in list(lipids):
        library[key] = []
        for lipid in lipids[key]:
            library[key].append(new_spectra(key, lipid, classes[key][2]))

    return(library)