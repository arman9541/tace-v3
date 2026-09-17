# TACE PQC (Torricelli Asymptotic Cusp Encryption)

`tace_pqc` is a post-quantum secure cryptographic primitive built on high-dimensional lattice geometry. It replaces vulnerable number-theoretic structures (such as modular square-root sieves and RSA/Rabin composite trapdoors) with a robust, asymmetric lattice-based architecture immune to quantum cryptanalysis, including Shor's Algorithm.

## Core Architecture

* **Quantum Resistance:** Security is anchored in high-dimensional lattice transformations over finite fields, making unauthorized path inversion as hard as solving variants of the Shortest Vector Problem (SVP) and Learning With Errors (LWE).
* **Asymmetric Trapdoor Design:** 
  * *For the Attacker:* An intractable geometric labyrinth with no algebraic shortcuts.
  * *For the Key Creator:* Instantaneous polynomial-time path recovery via structured trapdoor basis delegation and modular Gaussian elimination.
* **NIST-Standardized Parameters:** Leverages NTT-friendly prime moduli ($q = 8380417$) optimized for performance and cryptographic safety.
* **Cryptographic Commitments:** Integrates a domain-separated SHA-256 hash chain to ensure that intermediate state transitions are cryptographically bound to a single public anchor.

---

## Installation

To install the package locally in editable mode for development and testing:

```bash
git clone [https://github.com/your-username/tace_pqc.git](https://github.com/your-username/tace_pqc.git)
cd tace_pqc
pip install -e .
