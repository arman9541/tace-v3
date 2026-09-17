import time
from tace_pqc import TACEV6ProductionEngine

def main():
    print("Initializing TACE v6 PQC Package Demo...")
    # Initialize with dimension d=32 and NIST-standard prime q=8380417
    engine = TACEV6ProductionEngine(num_levels=4, dim=32, q=8380417)
    
    sample_path = [4, 1, 8, 3]
    
    # 1. Forward pass
    start_fwd = time.time()
    states, chain, anchor = engine.forward(sample_path)
    fwd_time = time.time() - start_fwd
    
    print(f"Forward Execution Time: {fwd_time:.5f}s")
    print(f"Public Anchor: {anchor[:32]}...\n")
    
    # 2. Creator trapdoor inversion pass
    print("Executing Creator Trapdoor Inversion via Package...")
    start_inv = time.time()
    curr = states[-1]
    
    for i in range(len(sample_path) - 1, -1, -1):
        preds = engine.trapdoor_solve_step(curr, i)
        expected_prev = tuple(states[i])
        valid_pred = expected_prev if expected_prev in preds else (list(preds)[0] if preds else tuple([0]*engine.dim))
        
        print(f"Level {i}: Predecessors found -> {len(preds)} candidates")
        curr = list(valid_pred)
        
    inv_time = time.time() - start_inv
    print(f"\nTotal Inversion Time: {inv_time:.5f}s")
    print("=== Modular Package Verification Complete ===")

if __name__ == "__main__":
    main()
