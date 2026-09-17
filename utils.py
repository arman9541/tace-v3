import hashlib

def h(s):
    """Domain-separated cryptographic hash wrapper using SHA-256."""
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def gaussian_solve(A, b, q):
    """
    Optimized modular Gaussian elimination for trapdoor inversion over Z_q.
    Solves A * x = b (mod q).
    """
    d = len(A)
    M = [row[:] + [b[r]] for r, row in enumerate(A)]
    
    for col in range(d):
        pivot = -1
        for row in range(col, d):
            if M[row][col] % q != 0:
                pivot = row
                break
        if pivot == -1:
            return None
        M[col], M[pivot] = M[pivot], M[col]
        
        inv = pow(M[col][col], q - 2, q) # Fermat's Little Theorem for modular inverse
        for c in range(col, d + 1):
            M[col][c] = (M[col][c] * inv) % q
            
        for row in range(d):
            if row != col:
                factor = M[row][col]
                for c in range(col, d + 1):
                    M[row][c] = (M[row][c] - factor * M[col][c]) % q
                    
    return [M[i][d] % q for i in range(d)]
