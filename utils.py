def validSequence(seq):
    valid_nuc = "ACTG"
    for nuc in seq:
        if not nuc in valid_nuc:
            return False
    return True
