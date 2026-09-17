# tace-v3
Reference implementation and security verification harness for the TACE v3 cryptographic path-commitment architecture.
# Torricelli Asymptotic Cusp Encryption (TACE) v3

**A Non-Archimedean Path-Commitment Primitive and Its Algebraic Funnel Analysis**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cryptographic Primitive](https://img.shields.io/badge/Primitive-Path%20Commitment-orange.svg)]()
[![Quantum Resistance](https://img.shields.io/badge/Quantum%20Resistant-QFT%20Evasion-green.svg)]()

## Overview

Traditional public-key cryptosystems relying on flat Euclidean cyclic groups are vulnerable to quantum algorithms exploiting the Quantum Fourier Transform (QFT). **TACE v3** introduces an alternative topological foundation built upon **non-Archimedean $p$-adic ultrametric trees**. 

Geometrically inspired by **Gabriel's Horn** (Torricelli's Paradox)—where an infinite surface area encapsulates a finite volume—TACE maps an exponentially large combinatorial path space ($p^N$) into a compact, collision-resistant cryptographic anchor ($C_k$).

## Core Architecture

1. **The Private Path Space ($\mathbb{Z}_p$):** A hierarchical traversal path $k = (a_0, a_1, \dots, a_{N-1})$ down an $N$-level ultrametric tree.
2. **The Cusp Transition Function:** A non-linear polynomial lifting recurrence governing state evolution across expanding prime-power moduli:
   $$x_{i+1} = (x_i \cdot p + a_i)^2 + i \pmod{p^{i+1}}$$
3. **The Algebraic Funnel Hypothesis:** Empirical backward-branching analysis demonstrates that predecessor trajectories form a tightly bounded sieve rather than unconstrained expansion, proving the necessity of cryptographic binding.
4. **The Path-Commitment Hash Chain:** A domain-separated cryptographic accumulator ($C_k = c_N$) binding every step of the trajectory to ensure complete collision resistance and non-malleability.
5. **Quantum Security (QFT Evasion):** The total absence of a global translation-invariant cyclic group structure in ultrametric spaces prevents Shor-style period decimation.

---

## Quick Start: Running the Verification Suite

The included Python simulation harness tests the algebraic funnel behavior, mid-path tampering detection, and anchor forgery resistance.

### Requirements
* Python 3.8+ (Uses only standard library modules: `hashlib`).

### Execution
Clone the repository and run the verification suite:

```bash
python3 tace_v3.py
