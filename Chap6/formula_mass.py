# formula_mass.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import re
from am import AM

# Tokenize a molecular formula
def tokenize(formula):
    # Compile regex patterns for matching formula tokens
    p_left  = re.compile(r'\(')             # Literal left parenthesis
    p_right = re.compile(r'\)')             # Literal right parenthesis
    p_num   = re.compile(r'(\d+)')          # One or more digits
    p_atom  = re.compile(r'([A-Z][a-z]?)')  # Upper and optional lowercase letter
    p_ws    = re.compile(r'\s+')            # One or more whitespace chars

    tokens   = []                           # Init token list
    next     = 0                            # Init next char index to 0
    form_len = len(formula)                 # Init number of chars in formula
    
    # Tokenize the formula.
    while next < form_len:                  # While not past end of formula
        if m := p_ws.match(formula, next):  # Discard leading whitespace
            next += m.end()                 # Move to next character position
                                            # Look for atom token
        elif m := p_atom.match(formula, next):
            tokens.append( m.group() )      # Add to token list
            next = m.end()                  # Move to next character position
                                            # Look for integer token
        elif m := p_num.match( formula, next ):
            tokens.append( int(m.group()) ) # Add to token list
            next = m.end()                  # Move to next character position
                                            # Look for left delim token
        elif m := p_left.match( formula, next ):
            tokens.append('(')              # Add to token list
            next = m.end()                  # Move to next character position
                                            # Look for right delim token
        elif m := p_right.match( formula, next ):
            tokens.append(')')              # Add to token list
            next = m.end()                  # Move to next character position
        
        else:                               # No match is a syntax error.
            msg = f'''Invalid character: {formula}
            {' '*(next+20)}^'''             # Identify syntax error location
            raise SyntaxError(msg)
        
    return tokens

# Sum up all masses in a tokenized molecular formula
def sum_masses(tokens):
    masses = []
    for token in tokens:                    # Process tokens into a mass list
        if token == '(':                    # Push left delim bound onto masses 
            masses.append(token)
        
        elif token == ')':                  # On right delim, sum masses to left delim.
            total = 0
            try:                            # Sum masses
                while masses[-1] != '(': total += masses.pop()
            except IndexError:              # Missing delim is a syntax error.
                raise SyntaxError("Missing left delimiter")
            masses[-1] = total              # Replace delim pushed on masses list with total
        
        elif isinstance(token, str):        # Get atom mass and append
            masses.append( AM[token] )
            
        elif isinstance(token, int):        # On number, multiply last mass by int
            masses[-1] = token*masses[-1] # Replace delim with scaled mass
    
    if '(' in masses:                       # Unmatched delim is SyntaxError
        raise SyntaxError("Missing right delimiter")
    
    return sum( masses )                    # Sum total formula mass
    
# Compute formula mass given chemical formula
def formula_mass( formula ):    
    tokens = tokenize(formula)
    total  = sum_masses(tokens)
    return total

# Tests
if __name__ == '__main__':
    
    CalciumCarbonate = "CaCO3"
    print( f'Calcium Carbonate: Formula={CalciumCarbonate}, MW={formula_mass(CalciumCarbonate)}' )
    
    Water = "H2 O"
    print( f'Water: Formula={Water}, MW={formula_mass(Water)}' )
    
    Ethanol = "C2H5OH"
    print( f'Ethanol: Formula={Ethanol}, MW={formula_mass(Ethanol)}' )
    
    Aspartame = "C14H18N2O5"
    print( f'Aspartame: Formula={Aspartame}, MW={formula_mass(Aspartame)}' )

    AlumOx = "Al2O3"
    print( f'Aluminum Oxide: Formula={AlumOx}, MW={formula_mass(AlumOx)}' )

    PenG = "C16H18N2O4S"
    print( f'Penicillin G: Formula={ PenG }, MW={formula_mass(PenG)}' )

    Cholest = "C27H46O"
    print( f'Cholesterol: Formula={ Cholest }, MW={formula_mass(Cholest)}' )

    Isopro = "(CH3)2CH(OH)"
    print( f'Isopropanol: Formula={ Isopro }, MW={formula_mass( Isopro)}' )

    AcetylSal = "CH3COOC6H4COOH"
    print( f'Acetylsalicylic Acid: Formula={ AcetylSal }, MW={formula_mass( AcetylSal)}' )

    ATP = "C10H16N5O13P3"
    print( f'ATP: Formula={ATP}, MW={formula_mass( ATP )}' )
    
    AlumSulfate = "Al2(SO4)3"
    print( f'Aluminum Sulfate: Formula={ AlumSulfate }, MW={formula_mass( AlumSulfate)}' )
        
    # Ammonium Carbonate and Barium Nitrate
    form = "( (NH4)2 CO3)2 ( Ba(NO3)2 )3"
    print( f'Ammonium Carbonate and Barium Nitrate: Formula={form}, MW={formula_mass(form)}' )
    
    form = "C6H2(NO2)3CH3"
    print( f'Formula={form}, MW={formula_mass(form)}' )
    
    form = "(CH3)16(Tc(H2O)3CO(BrFe3(ReCl)3(SO4)2)2)2MnO4"
    print( f'Formula={form}, MW={formula_mass(form)}' )
    
    form = "(Tc(H2O)3CO(BrFe3(ReCl)3(SO4)2)2)2MnO4"
    print( f'Formula={form}, MW={formula_mass(form)}' )

    # Error Checks

    # Broken1 = "CH3COO_C6H4COOH"
    # formula_mass( Broken1 )

    # # Missing left delimiter
    # form = "CH4(Si))"
    # print( form, '=', formula_mass(form))

    # # Missing right delimiter
    # form = "CH4(Si"
    # print( form, '=', formula_mass(form))
