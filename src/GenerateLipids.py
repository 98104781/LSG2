import Definitions as D
import GenerateTails
from itertools import compress
from itertools import combinations_with_replacement as cwr
from itertools import product

classes = D.classes

def generate_lipids():
    
    def generate(key):

        lipid_body = D.classes[key][1][1]
        number_of_tails = D.classes[key][1][0]

        if lipid_body == 'Glycerol': 
            lst = [list(comb) 
             for comb in cwr(tails[0], number_of_tails)]

        elif lipid_body == 'SB':
            lst = [list(filter(None, comb))
             for comb in product(tails[1], [tail * number_of_tails
              for tail in tails[0]])]                                                   # Hacky, only works for 0 and 1.

        return lst

    classes_to_generate = list(compress([lipid for lipid in D.classes],
     [int(D.classes[lipid][0]) for lipid in D.classes]))
    tails = GenerateTails.generate_tails(D.Chain_parameters, classes_to_generate)   # Tails created here

    species = {key:generate(key)
     for key in classes_to_generate}

    return species