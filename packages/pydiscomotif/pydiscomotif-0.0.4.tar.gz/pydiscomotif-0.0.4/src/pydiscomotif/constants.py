### Index bins constants ###
INDEX_DISTANCE_BIN_SIZE:float = 0.5 # Angstrooms
INDEX_MAX_DISTANCE_VALUE: float = 20.0
INDEX_ANGLE_BIN_SIZE: float = 10.0 # Degrees
INDEX_MAX_ANGLE_VALUE: float = 180.0 # Not used

### Amino acid constants ###
NON_POLAR_RESIDUES = {'G', 'A', 'V', 'L', 'I'}
POLAR_RESIDUES     = {'S', 'T', 'P', 'N', 'Q'}
SULFUR_RESIDUES    = {'M', 'C'}
POSITIVE_RESIDUES  = {'K', 'R', 'H'}
NEGATIVE_RESIDUES  = {'D', 'E'}
AROMATIC_RESIDUES  = {'F', 'Y', 'Z'}

AMINO_ACID_ALPHABET = set.union(NON_POLAR_RESIDUES, POLAR_RESIDUES, SULFUR_RESIDUES, POSITIVE_RESIDUES, NEGATIVE_RESIDUES, AROMATIC_RESIDUES)

# This mapping is used in search mode when residue_type_policy == 'relaxed'.
AMINO_ACID_RELAXED_GROUPS_MAP = {
    'G':NON_POLAR_RESIDUES,
    'A':NON_POLAR_RESIDUES,
    'V':NON_POLAR_RESIDUES,
    'L':NON_POLAR_RESIDUES,
    'I':NON_POLAR_RESIDUES,

    'S':POLAR_RESIDUES,
    'T':POLAR_RESIDUES,
    'P':POLAR_RESIDUES,
    'N':POLAR_RESIDUES,
    'Q':POLAR_RESIDUES,
    
    'M':SULFUR_RESIDUES,
    'C':SULFUR_RESIDUES,

    'K':POSITIVE_RESIDUES,
    'R':POSITIVE_RESIDUES,
    'H':POSITIVE_RESIDUES,

    'D':NEGATIVE_RESIDUES,
    'E':NEGATIVE_RESIDUES,

    'F':AROMATIC_RESIDUES,
    'Y':AROMATIC_RESIDUES,
    'W':AROMATIC_RESIDUES
}