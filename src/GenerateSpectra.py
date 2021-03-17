import Definitions as D

Masses = D.Masses
classes = D.classes

def generate_peaks(key, mass, lipid, adduct): # Was meant to be simple...
    
    peaks = [] # Fragmentation spectra stored here as [[mz, intensity], [...], ... ] 
   
    def MA(intensity): # A == Adduct
        peaks.append([round((mass + Masses[adduct][0])
        /Masses[adduct][2], 6), intensity])

    def MA_sub_H2O(intensity):
        peaks.append([round((mass + Masses[adduct][0] - Masses['H2O'])
        /Masses[adduct][2], 6), intensity])

    def MA_sub_2H2O(intensity):
        peaks.append([round((mass + Masses[adduct][0] - 2*Masses['H2O'])
        /Masses[adduct][2], 6), intensity])

    def MA_sub_FA(intensity):
        peaks.extend([[round(mass + Masses[adduct][0] - tail[0], 6), intensity] 
         for tail in lipid])

    def MA_sub_FAk(intensity):
        peaks.extend([[round(mass + Masses[adduct][0] + Masses['H2O'] - tail[0], 6), intensity] 
         for tail in lipid])  


    def MH(intensity): # H == Hydrogen. Sometimes the adduct is lost during fragmentation, replaced w/ H+.
        if Masses[adduct][1] == 'P':
            peaks.append([round(mass + Masses['H'], 6), intensity])
        if Masses[adduct][1] == 'N': 
            peaks.append([round(mass - Masses['H'], 6), intensity])  
    
    def MH_sub_H2O(intensity):
        if Masses[adduct][1] == 'P':
            peaks.append([round(mass + Masses['H'] - Masses['H2O'], 6), intensity])
        if Masses[adduct][1] == 'N':
            peaks.append([round(mass - Masses['H'] - Masses['H2O'], 6), intensity])
    
    def MH_sub_2H2O(intensity):
        if Masses[adduct][1] == 'P':
            peaks.append([round(mass + Masses['H'] - 2*Masses['H2O'], 6), intensity])
        if Masses[adduct][1] == 'N':
            peaks.append([round(mass - Masses['H'] - 2*Masses['H2O'], 6), intensity])
    
    def MH_sub_FA(intensity):
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass + Masses['H'] - tail[0], 6), intensity] 
             for tail in lipid])
        if Masses[adduct][1] == 'N':
            peaks.extend([[round(mass - Masses['H'] - tail[0], 6), intensity] 
             for tail in lipid])
    
    def MH_sub_FAk(intensity):
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass + Masses['H'] + Masses['H2O'] - tail[0], 6), intensity] 
             for tail in lipid])
        if Masses[adduct][1] == 'N':
            peaks.extend([[round(mass - Masses['H'] + Masses['H2O'] - tail[0], 6), intensity] 
             for tail in lipid])


    
    def FA_sub_H(intensity): 
        peaks.extend([[round(tail[0] - Masses['H'], 6), intensity]
         for tail in lipid if 'E' not in tail[1]])
    
    def FAk_H(intensity):
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(tail[0] - Masses['H2O'] + Masses['H'], 6), intensity]
             for tail in lipid if 'E' not in tail[1]])
        if Masses[adduct][1] == 'N':
            peaks.extend([[round(tail[0] - Masses['H2O'] - Masses['H'], 6), intensity]
             for tail in lipid if 'E' not in tail[1]])
    
    def FAk_A(intensity):
        peaks.extend([[round(tail[0] - Masses['H2O'] + Masses[adduct][0], 6), intensity]
         for tail in lipid if 'E' not in tail[1]])
    
    def HG_FA_NL(HG): # Fragments common to some GPLs. Loss of headgroup and tail.
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - HG - tail[0] + Masses['H2O'] + Masses[adduct][0], 6), 8]
            for tail in lipid])
        if Masses[adduct][1] == 'N':
            peaks.extend([[round(mass - HG - tail[0] - Masses['H'], 6), 15] # Not sure if these should be + Masses[adduct][0] rather than - Masses['H']. If the prior, could be done for both polarities?
            for tail in lipid])
            peaks.extend([[round(mass - HG - tail[0] + Masses['H2O'] - Masses['H'], 6), 5]
            for tail in lipid])


    def PA_gpl_Character(Place_Holder):
        HG_FA_NL(97.976895)
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - 97.976895 + Masses['H'], 6), 100]])
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10]])

    def PC_gpl_Character(Place_Holder):
        #HG_FA_NL(183.066044) # ?
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(183.066044 + Masses['H'], 6), 100]])
            if adduct == "[M+Na]+":
                peaks.extend([[round(mass - 59.073499  + Masses[adduct][0], 6), 25], #(Loss of N(CH3)3) Only happens for Alkaline salts?
                              [round(mass - 183.066044 + Masses[adduct][0], 6),  4],
                              [round(mass - 183.066044 + Masses['H'],       6),  4]]) # Should this be for all positive adducts?
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,  5],
                         [96.969618,   5],
                         [152.995833, 10]])

    def PE_gpl_Character(Place_Holder):
        HG_FA_NL(141.019094)
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - 141.019094 + Masses['H'], 6), 100]])
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10],
                          [140.011817,  3],
                          [196.038032,  5]])

    def PG_gpl_Character(Place_Holder):
        
        if Masses[adduct][1] == 'P':
            HG_FA_NL(172.013674) # Neutral loss is headgroup mass
            peaks.extend([[round(mass - 172.013674 + Masses['H'], 6), 100]])
        if Masses[adduct][1] == 'N':
            HG_FA_NL(74.036779) # Neutral loss is different to headgroup mass
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10],
                          [209.022048,  5],
                          [227.032612,  5],
                          [245.043177,  5]])

    def PI_gpl_Character(Place_Holder):
        if Masses[adduct][1] == 'P':
            pass
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10],
                          [223.001312,  5],
                          [241.011877, 25],
                          [259.022442,  5],
                          [297.038092,  5],
                          [315.048656,  5]])

    def PIP_gpl_Character(Place_Holder):
        if Masses[adduct][1] == 'P':
            pass
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10],
                          [223.001312,  5],
                          [241.011877, 25],
                          [259.022442,  5],
                          [297.038092,  5],
                          [315.048656,  5],
                          [302.957642,  5],
                          [320.978207,  5],
                          [395.014986,  5],
                          [159.985465,  5],
                          [168.9907475, 5],
                          [mass - 80.973606, 5],
                          [mass - 80.973606 - Masses['H2O'], 5],
                          [mass - Masses['H'] - Masses['H2O'], 5]])
    
    def PIP2_gpl_Character(Place_Holder):
        if Masses[adduct][1] == 'P': pass
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10],
                          [223.001312,  5],
                          [241.011877, 25],
                          [259.022442,  5],
                          [297.038092,  5],
                          [315.048656,  5],
                          [mass - 80.973606, 5],
                          [mass - 80.973606 - Masses['H2O'], 5],
                          [mass - Masses['H'] - Masses['H2O'], 5]])
    
    def PS_gpl_Character(Place_Holder):
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - 185.008923 + Masses['H'], 6), 100]])
        if Masses[adduct][1] == 'N':
            peaks.extend([[78.959053,   5],
                          [96.969618,   5],
                          [152.995833, 10]])
    
    def MG_gpl_Character():
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - 180.063388 + Masses['H2O'] + Masses['H']), 50]])
        if Masses[adduct][1] == 'N':
            pass
    
    def DG_gpl_Character():
        if Masses[adduct][1] == 'P':
            peaks.extend([[round(mass - 342.116212 + Masses['H2O'] + Masses['H']), 50]])
        if Masses[adduct][1] == 'N':
            pass

    f = {
        'MA':           MA,
        'MA_sub_H2O':   MA_sub_H2O,
        'MA_sub_2H2O':  MA_sub_2H2O,
        'MA_sub_FA':    MA_sub_FA,
        'MA_sub_FAk':   MA_sub_FAk,

        'MH':           MH,
        'MH_sub_H2O':   MH_sub_H2O,
        'MH_sub_2H2O':  MH_sub_2H2O,
        'MH_sub_FA':    MH_sub_FA,
        'MH_sub_FAk':   MH_sub_FAk,
        
        'FFA':          FA_sub_H,
        'FFAk':         FAk_H,
        'FFAkA':        FAk_A,

        'gPA':           PA_gpl_Character,
        'gPC':           PC_gpl_Character,
        'gPE':           PE_gpl_Character,
        'gPG':           PG_gpl_Character,
        'gPI':           PI_gpl_Character,
        'gPIP':          PIP_gpl_Character,
        'gPIP2':         PIP2_gpl_Character,
        'gPS':           PS_gpl_Character,
        'gMG':           MG_gpl_Character,
        'gDG':           DG_gpl_Character
    }

    spectra = classes[key][2][adduct]
    for func, intens in zip(spectra[0], spectra[1]):
        f[func](intens)

    keep = [] # Remove duplicates
    seen = set([])
    for peak in peaks:
        if peak[0] not in seen:
            keep.append(peak)
            seen.add(peak[0])
    keep.sort() # Sort fragments based on mass
    peaks = keep

    return peaks