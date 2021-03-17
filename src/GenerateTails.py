import Definitions as D
from itertools import compress

def generate_tails(n, classes_to_generate):

    def any_Sp_lipids():                                                        # look for whether SB lipids are needed
        if 'SB' in [D.classes[lipid][1][1] for lipid in classes_to_generate]: return True 
        else: return False

    def calculate_mass_and_name(c, d):
        definitions = { 'Ac':[31.98982926, 0, 0, ''],                            # Acyl chains, Mass of body, how many carbons does the body count as, how much desaturation does the body include
                        'Pl':[15.994915, 0, 1,  'E'],                            # Plasmenyl chains
                        'Sp':[91.063329, 3, 0,'Sp_']}                            # Sphingoid bases
        i = definitions[type]
        return [i[0] + (c-i[1])*14.01565007 - (d-i[2])*2.01565007, f"{i[3]}{c}:{d}"]

    def generate(type):
        Tail_Opts =   {'Odd':  True}                                            # Needs to be pulled out and put in definitions
        list_location = {'Ac':0, 'Pl':0, 'Sp':1}                                # Sphingoid bases need to be added to a separate list, as they're not fatty acids
        tails[list_location[type]].extend([calculate_mass_and_name(c, d)        # Extend the appropriate list
            for c in range(n[0], n[1] + 1) 
                if (Tail_Opts['Odd'] == False and (c % 2 == 0))
                or (Tail_Opts['Odd'] == True)
                    for d in range(n[2], n[3] + 1) if d <= ((c-1)/2)])          # Limits desaturation based on C number

    tail_types =  {'Ac':   True,
                   'Pl':   False,                                               # Needs to be pulled out and put in definitions later on
                   'Sp':   any_Sp_lipids()}
    types_to_generate = list(compress([t for t in tail_types], 
     [int(tail_types[t]) for t in tail_types]))                                 # What types of lipids to generate? currently Acyl (Ac), Plasmenyl (Pl) or Sphingoid (Sp)
    tails = [[],[]]                                                             # Tails template. Location 0 for acyl, Location 1 for Sphingoid.

    for type in types_to_generate:                                              # For all the types of lipids needed, generate them and add them to the appropriate list
        generate(type)

    return tails