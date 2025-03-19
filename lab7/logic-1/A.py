def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40  
    else:
        return 40 <= cigars <= 60
cigars = 30
is_weekend = False