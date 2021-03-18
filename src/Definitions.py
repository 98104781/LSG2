Charge_Opts = {

    'POS':  False,  
    'NEG':  True}

Masses = {
    "[M-H]-":     
    [-1.007276, 'N', 1],

    "[M-2H]2-":   
    [-2.014552, 'N', 2],

    "[M-3H]3-":   
    [-3.021828, 'N', 3],

    "[M+Cl]-":    
    [34.969401, 'N', 1],

    "[M+H]+":     
    [1.007276,  'P', 1],

    "[M+H-H2O]+": 
    [-17.003289,'P', 1],

    "[M+Na]+":    
    [22.989221, 'P', 1],

    "[M+NH4]+":   
    [18.033826, 'P', 1],

    "H":           
    1.007276,

    "H2O":         
    18.010565}

Chain_parameters = [16, 20, 0, 4]

classes = { # Structural and spectra information defined here.
    
    'MAG':                                          # Class
     [False,                                        # [Generate/Don't generate,
     [1, 'Glycerol', None],                         # [# of tails, Body type ('Glycerol' for glycerolipids or 'SB' for sphingolipids), Headgroup mass (None if no headgroup)]]
     {"[M+H]+":     [['MA', 'MA_sub_H2O', 'FFAk'],  # { Adduct:   [[Types of fragments to generate],
                     [100, 50, 50]],                #              [Intensities of fragment]] }                        
      "[M+H-H2O]+": [['MA', 'FFAk'], 
                     [100, 50]],
      "[M+Na]+":    [['MA', 'MA_sub_H2O','FFAk', 'FFAkA'],
                     [100, 50, 50, 10]],
      "[M+NH4]+":   [['MA', 'MH', 'MH_sub_H2O', 'FFAk'],
                     [100, 100, 50, 50]]}], 
                                                    
    'DAG':                                          ##### Metabolites 2016, 6(3), 25; https://doi.org/10.3390/metabo6030025
     [False,                                        ##### J Am Soc Mass Spectrom. 2010 April ; 21(4): 657–669. https://doi.org/10.1016/j.jasms.2010.01.007
     [2, 'Glycerol', None],           
     {"[M+H]+":     [['MA', 'MH_sub_H2O', 'FFAk', 'MH_sub_FA'],
                     [25, 100, 1, 25]],
      "[M+H-H2O]+": [['MA', 'FFAk', 'MH_sub_FA'],
                     [25, 1, 25]],
      "[M+Na]+":    [['MA', 'MA_sub_H2O', 'FFAk', 'MH_sub_FA', 'FFAkA', 'MA_sub_FA'],
                     [25, 50, 1, 25, 5, 10]],
      "[M+NH4]+":   [['MA', 'MH', 'MH_sub_H2O', 'FFAk', 'MH_sub_FA'],
                     [25, 10, 100, 1, 25]]}],

    'TAG':                 
     [False, 
     [3, 'Glycerol', None],           
     {"[M+Na]+":   [['MA', 'MH_sub_FA', 'MA_sub_FA', 'FFAk', 'FFAkA'], 
                    [25, 100, 10, 10, 5]],
     "[M+NH4]+":   [['MA', 'MH_sub_FA', 'FFAk'], 
                    [25, 100, 10]]}],

    'PA':                  
     [False, 
     [2, 'Glycerol', 97.976895],           
     {"[M-H]-":    [['MA', 'gPA', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                    [25, 0, 100, 15, 5]],
      "[M+H]+":    [['MA', 'gPA', 'FFAk'],
                    [25, 0, 4]],
      "[M+Na]+":   [['MA', 'gPA', 'FFAkA'], 
                    [25, 0, 4]]}],

    'Lyso PA':      
     [False, 
     [1, 'Glycerol', 97.976895],           
     {"[M-H]-":    [['MA', 'gPA', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                    [25, 0, 100, 15, 5]],
      "[M+H]+":    [['MA', 'gPA', 'FFAk'],
                    [25, 0, 4]],
      "[M+Na]+":   [['MA', 'gPA', 'FFAkA'],  # Should Lyso GPLs have [M+H-H2O]+ ?
                    [25, 0, 4]]}],

    'PC':                  
     [False, 
     [2, 'Glycerol', 183.066044], # headgroup mass has -H to maintain neutral charge              
     {"[M+H]+":    [['MA', 'gPC', 'MH_sub_FA', 'MH_sub_FAk', 'FFAk'],
                    [25, 0, 4, 8, 4]],
      "[M+Na]+":   [['MA', 'gPC', 'MA_sub_FA', 'MA_sub_FAk', 'FFAkA'],
                    [25, 0, 4, 8, 4]]}],

    'Lyso PC':             
     [False, 
     [1, 'Glycerol', 183.066044], # headgroup mass has -H to maintain neutral charge              
     {"[M+H]+":    [['MA', 'gPC', 'MH_sub_FA', 'MH_sub_FAk', 'FFAk'],
                    [25, 0, 4, 8, 4]],
      "[M+Na]+":   [['MA', 'gPC', 'MA_sub_FA', 'MA_sub_FAk', 'FFAkA'],
                    [25, 0, 4, 8, 4]]}],

    'PE':                  
     [False, 
     [2, 'Glycerol', 141.019094],           
     {"[M-H]-":    [['MA', 'gPE', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                   [25, 0, 100, 15, 5]],
      "[M+H]+":    [['MA', 'gPE', 'FFAk'],
                   [25, 0, 4]],
      "[M+Na]+":   [['MA', 'gPE', 'FFAkA'],
                   [25, 0, 4]]}],

    'Lyso PE':             
     [False, 
     [1, 'Glycerol', 141.019094],           
     {"[M-H]-":    [['MA', 'gPE', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                   [25, 0, 100, 15, 5]],
      "[M+H]+":    [['MA', 'gPE', 'FFAk'],
                   [25, 0, 4]],
      "[M+Na]+":   [['MA', 'gPE', 'FFAkA'],
                   [25, 0, 4]]}],

    'PG':                  
     [False, 
     [2, 'Glycerol', 172.013674],           
     {"[M-H]-":   [['MA', 'gPG', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                   [25, 0, 100, 15, 5]],
      "[M+H]+":   [['MA', 'gPG', 'FFAk'],
                   [25, 0, 4]],
      "[M+Na]+":  [['MA', 'gPG', 'FFAkA'],
                   [25, 0, 4]]}],

    'Lyso PG':             
     [False, 
     [1, 'Glycerol', 172.013674],           
     {"[M-H]-":   [['MA', 'gPG', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                   [25, 0, 100, 15, 5]],
      "[M+H]+":   [['MA', 'gPG', 'FFAk'],
                   [25, 0, 4]],
      "[M+Na]+":  [['MA', 'gPG', 'FFAkA'],
                   [25, 0, 4]]}],                                           # Perhaps I should add PGly ?
                                                    
    'PI':                                                                   # https://doi.org/10.1016/S1044-0305(00)00172-0
     [True, 
     [2, 'Glycerol', 260.029718],           
     {"[M-H]-":   [['MA', 'gPI', 'FFA', 'MH_sub_FA', 'MH_sub_FAk'],
                   [25, 0, 100, 15, 5]]}],

    'Lyso PI':             
     [False, 
     [1, 'Glycerol', 260.029718],           
     {"[M-H]-":   [[],
                   []]}],

    'PIP':                 
     [True, 
     [2, 'Glycerol', 339.996048],          
     {"[M-H]-":[['MA' , 'MH_sub_H2O', 'M2H', 'gPIP', 'FFA', 'MH_sub_FA_H2O', 'MH_sub_FA', 'MH_sub_FAk'],
                [25, 10, 5, 0, 100, 15, 15, 5]],
      "[M-2H]2-":[[],
                  []]}],

    'PIP2':                
     [False, 
     [2, 'Glycerol', 419.962378],
     {"[M-H]-":[],
      "[M-2H]2-":[],
       "[M-3H]3-":[]}],

    'PS':                  
     [False, 
     [2, 'Glycerol', 185.008923],           
     {"[M-H]-":[],
      "[M+H]+":[],
       "[M+Na]+":[]}],

    'Lyso PS':             
     [False, 
     [1, 'Glycerol', 185.008923],           
     {"[M-H]-":[],
      "[M+H]+":[],
       "[M+Na]+":[]}],

    'MGDG':                
     [False, 
     [2, 'Glycerol', 180.063388], # headgroup mass is just of the galactose ring        
     {"[M+Na]+":[],
      "[M+NH4]+":[]}],

    'DGDG':                
     [False, 
     [2, 'Glycerol', 342.116212], # headgroup mass is just of the galactose rings       
     {"[M+Na]+":[],
      "[M+NH4]+":[]}],

    'Sphingosine': # LipidBlast seemed to have only "[M+Na]+" spectra. Seen "[M+NH4]+" and "[M-H]-" in some articles.         
     [False, 
     [0, 'SB', None],        
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'N-acylsphingosine': # Lipidblast also only has 1 fragment for these, and there aren't many characteristic studies.   
     [False, 
     [1, 'SB', None],  
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],             
    
    'Ceramide PA':         
     [False, 
     [1, 'SB', 97.976895],                 
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide PC':         
     [False, 
     [1, 'SB', 183.066044], # headgroup mass has -H to maintain neutral charge                 
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide PE':         
     [False, 
     [1, 'SB', 141.019094],                 
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide PG':         
     [False, 
     [1, 'SB', 172.013674],                 
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide PI':         
     [False, 
     [1, 'SB', 260.029718],                 
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}], # Perhaps PIP and PIP2 should be included.
    
    'Ceramide PS':         
     [False, 
     [1, 'SB', 185.008923],                
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide MG':         
     [False, 
     [1, 'SB', 180.063388], # headgroup mass is just of the galactose ring               
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}],
    
    'Ceramide DG':         
     [False, 
     [1, 'SB', 342.116212], # headgroup mass is just of the galactose rings            
     {"[M-H]-":[],
      "[M+Cl]-":[],
       "[M+H]+":[],
        "[M+Na]+":[]}]}