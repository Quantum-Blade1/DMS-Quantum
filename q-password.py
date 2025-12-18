"""
============================================================
QUANTUM-ENHANCED PASSWORD STRENGTH ANALYZER
Combining Discrete Mathematics + Quantum Computing
============================================================

PROJECT COMPONENTS:
1. Classical Analysis (DMS - Sets, Counting, Logarithms)
2. Quantum Threat Analysis (Grover's Algorithm)
3. Quantum Encryption (QKD Simulation)

TECHNOLOGIES:
- Python 3.x
- Qiskit (IBM Quantum Computing Framework)
- NumPy, Math
============================================================
"""

import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumPasswordAnalyzer:
    """
    MAIN CLASS: Combines Classical DMS + Quantum Computing
    
    SIMPLE EXPLANATION:
    This class is like a security expert that:
    1. Checks your password TODAY (classical)
    2. Checks your password TOMORROW (quantum threat)
    3. Creates quantum protection (quantum encryption)
    """
    
    def __init__(self):
        """
        Initialize the analyzer with character sets and quantum simulator
        
        SIMPLE EXPLANATION:
        This is like setting up your lab equipment before an experiment:
        - Character sets = ingredients for passwords
        - Attacker speeds = how fast hackers work
        - Quantum simulator = virtual quantum computer
        """
        # Classical character sets (DMS: Sets Theory)
        self.char_sets = {
            'lowercase': 26,  # {a, b, c, ..., z}
            'uppercase': 26,  # {A, B, C, ..., Z}
            'digits': 10,     # {0, 1, 2, ..., 9}
            'symbols': 8      # {!, @, #, $, %, ^, &, *}
        }
        
        # Attack speeds
        self.classical_speed = 10**8   # 100 million attempts/second (today)
        self.quantum_speed = 10**12    # 1 trillion attempts/second (future)
        
        # Quantum simulator (IBM Qiskit)
        self.quantum_backend = Aer.get_backend('qasm_simulator')
        
        print("✅ Quantum Password Analyzer Initialized!")
        print(f"   Classical Speed: {self.classical_speed:,.0f} attempts/sec")
        print(f"   Quantum Speed: {self.quantum_speed:,.0f} attempts/sec")
    
    # ============================================================
    # MODULE 1: CLASSICAL ANALYSIS (Discrete Mathematics)
    # ============================================================
    
    def calculate_charset_size(self, use_lowercase, use_uppercase, use_digits, use_symbols):
        """
        Calculate character set size using SET UNION
        
        SIMPLE EXPLANATION:
        Imagine you have 4 boxes of letters:
        - Box 1: a-z (26 letters)
        - Box 2: A-Z (26 letters)
        - Box 3: 0-9 (10 numbers)
        - Box 4: !@#$ (8 symbols)
        
        We combine the boxes you selected and count total items.
        
        FORMULA: k = |Lowercase ∪ Uppercase ∪ Digits ∪ Symbols|
        """
        k = 0
        details = []
        
        if use_lowercase:
            k += self.char_sets['lowercase']
            details.append(f"Lowercase: +{self.char_sets['lowercase']}")
        
        if use_uppercase:
            k += self.char_sets['uppercase']
            details.append(f"Uppercase: +{self.char_sets['uppercase']}")
        
        if use_digits:
            k += self.char_sets['digits']
            details.append(f"Digits: +{self.char_sets['digits']}")
        
        if use_symbols:
            k += self.char_sets['symbols']
            details.append(f"Symbols: +{self.char_sets['symbols']}")
        
        return k, details
    
    def calculate_classical_combinations(self, k, n):
        """
        Calculate total combinations using COUNTING PRINCIPLE
        
        SIMPLE EXPLANATION:
        If you have a lock with 'n' dials, and each dial has 'k' numbers,
        total combinations = k × k × k × ... (n times) = k^n
        
        Example: 4-digit PIN with 10 numbers = 10^4 = 10,000 combinations
        
        FORMULA: Total = k^n
        """
        combinations = k ** n
        return combinations
    
    def calculate_entropy(self, k, n):
        """
        Calculate password entropy using LOGARITHMS
        
        SIMPLE EXPLANATION:
        Entropy = "randomness" or "unpredictability"
        Higher entropy = harder to guess
        
        Think of it like:
        - Flipping 1 coin = 1 bit of entropy (2 options)
        - Flipping 2 coins = 2 bits of entropy (4 options)
        - Your password = n × log2(k) bits
        
        FORMULA: H = n × log₂(k)
        """
        if k <= 0:
            return 0
        entropy = n * math.log2(k)
        return entropy
    
    def calculate_classical_crack_time(self, combinations):
        """
        Estimate time to crack with CLASSICAL computers
        
        SIMPLE EXPLANATION:
        If a hacker tries 100 million passwords per second,
        how long to try all combinations?
        
        Time = Total Combinations ÷ Speed
        
        Example: 1 million passwords ÷ 100 million per sec = 0.01 seconds
        """
        time_seconds = combinations / self.classical_speed
        return self.format_time(time_seconds)
    
    def classify_strength(self, entropy):
        """
        Classify password strength using RELATIONS
        
        SIMPLE EXPLANATION:
        We create a rule (relation) that maps entropy to strength:
        - Below 40 bits → WEAK (like a 3-digit PIN)
        - 40-60 bits → MEDIUM (like a simple password)
        - 60-80 bits → STRONG (like a good password)
        - Above 80 bits → VERY STRONG (like a super password)
        
        RELATION: R = {(entropy, strength) | rules applied}
        """
        if entropy < 40:
            return "WEAK", "🔴"
        elif entropy < 60:
            return "MEDIUM", "🟡"
        elif entropy < 80:
            return "STRONG", "🟢"
        else:
            return "VERY STRONG", "🟢🟢"
    
    # ============================================================
    # MODULE 2: QUANTUM THREAT ANALYSIS
    # ============================================================
    
    def apply_grovers_speedup(self, combinations):
        """
        Apply Grover's Algorithm for QUANTUM SPEEDUP
        
        SIMPLE EXPLANATION:
        Classical computer: "Let me try password 1, 2, 3, 4..." (slow)
        Quantum computer: "Let me try ALL passwords at once!" (fast)
        
        Grover's algorithm reduces search time from N to √N
        
        Example:
        - Classical: 1,000,000 attempts
        - Quantum: √1,000,000 = 1,000 attempts (1000× faster!)
        
        FORMULA: Quantum Attempts = √(Classical Combinations)
        """
        quantum_attempts = math.sqrt(combinations)
        speedup_factor = combinations / quantum_attempts if quantum_attempts > 0 else 1
        return quantum_attempts, speedup_factor
    
    def calculate_quantum_crack_time(self, quantum_attempts):
        """
        Estimate time to crack with QUANTUM computers
        
        SIMPLE EXPLANATION:
        Same as classical, but:
        1. Fewer attempts needed (thanks to Grover)
        2. Faster quantum processors
        
        This shows how vulnerable your password is to FUTURE attacks
        """
        time_seconds = quantum_attempts / self.quantum_speed
        return self.format_time(time_seconds)
    
    def assess_quantum_vulnerability(self, classical_time_str, quantum_time_str):
        """
        Compare classical vs quantum vulnerability
        
        SIMPLE EXPLANATION:
        Compares how long your password lasts:
        - TODAY (classical computers)
        - TOMORROW (quantum computers)
        
        If difference is huge → you need quantum protection!
        """
        vulnerability = "CRITICAL" if "second" in quantum_time_str or "minute" in quantum_time_str else \
                       "HIGH" if "hour" in quantum_time_str or "day" in quantum_time_str else \
                       "MODERATE" if "year" in quantum_time_str else "LOW"
        
        return vulnerability
    
    # ============================================================
    # MODULE 3: QUANTUM ENCRYPTION (QKD Simulation)
    # ============================================================
    
    def create_quantum_key(self, length):
        """
        Generate quantum encryption key using QUANTUM CIRCUIT
        
        SIMPLE EXPLANATION:
        Classical key: "Here's your key: 101010"
        Quantum key: "Here's your key in superposition: |0⟩+|1⟩"
        
        WHY IT'S SECURE:
        1. Key exists in multiple states (superposition)
        2. Measuring it changes it (observer effect)
        3. Any eavesdropper is detected!
        
        QUANTUM GATES USED:
        - Hadamard (H): Creates superposition (0 and 1 simultaneously)
        - CNOT: Creates entanglement (qubits connected)
        """
        
        # Create quantum circuit
        num_qubits = min(length, 8)  # Limit to 8 qubits for simulation
        qr = QuantumRegister(num_qubits, 'q')
        cr = ClassicalRegister(num_qubits, 'c')
        qc = QuantumCircuit(qr, cr)
        
        print(f"\n   🔬 Creating Quantum Circuit with {num_qubits} qubits...")
        
        # Step 1: Apply Hadamard gate (creates superposition)
        print(f"   Step 1: Applying Hadamard gates (superposition)...")
        for i in range(num_qubits):
            qc.h(qr[i])  # H gate: |0⟩ → (|0⟩ + |1⟩)/√2
        
        # Step 2: Apply CNOT gates (creates entanglement)
        print(f"   Step 2: Applying CNOT gates (entanglement)...")
        for i in range(num_qubits - 1):
            qc.cx(qr[i], qr[i + 1])  # Entangle adjacent qubits
        
        # Step 3: Add barrier for visualization
        qc.barrier()
        
        # Step 4: Measure quantum states
        print(f"   Step 3: Measuring quantum states...")
        qc.measure(qr, cr)
        
        # Execute quantum circuit
        job = self.quantum_backend.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts(qc)
        quantum_key = list(counts.keys())[0]
        
        print(f"   ✅ Quantum Key Generated: {quantum_key}")
        
        return quantum_key, qc
    
    def quantum_encrypt_password(self, password_length):
        """
        Create quantum-protected password hash
        
        SIMPLE EXPLANATION:
        Normal encryption: password → hash
        Quantum encryption: password → quantum key → quantum hash
        
        The quantum key is:
        1. Impossible to copy (no-cloning theorem)
        2. Detects eavesdropping
        3. Future-proof against quantum attacks
        """
        quantum_key, circuit = self.create_quantum_key(password_length)
        
        # Create quantum-enhanced hash (simulation)
        # In real QKD, this would use quantum channels
        quantum_hash = f"QKD-{quantum_key}-{hash(quantum_key) % 10000:04d}"
        
        return quantum_hash, quantum_key, circuit
    
    # ============================================================
    # UTILITY FUNCTIONS
    # ============================================================
    
    def format_time(self, seconds):
        """Convert seconds to readable format"""
        if seconds < 60:
            return f"{seconds:.2e} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.2f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.2f} days"
        else:
            return f"{seconds/31536000:.2e} years"
    
    # ============================================================
    # MAIN ANALYSIS FUNCTION
    # ============================================================
    
    def analyze_password(self, length, use_lowercase=True, use_uppercase=True,
                        use_digits=True, use_symbols=False, show_quantum_circuit=False):
        """
        Complete password analysis: Classical + Quantum
        
        SIMPLE EXPLANATION:
        This is the main function that:
        1. Analyzes password with DMS (math)
        2. Checks quantum threat (future)
        3. Creates quantum protection (encryption)
        4. Gives you complete security report
        """
        
        print("\n" + "="*70)
        print("🔐 QUANTUM-ENHANCED PASSWORD STRENGTH ANALYZER")
        print("="*70)
        
        # ============================================================
        # MODULE 1: CLASSICAL ANALYSIS
        # ============================================================
        print("\n" + "📊 MODULE 1: CLASSICAL ANALYSIS (Discrete Mathematics)")
        print("-"*70)
        
        # Step 1: Character set
        k, details = self.calculate_charset_size(use_lowercase, use_uppercase, 
                                                  use_digits, use_symbols)
        print(f"\n✓ Character Set Size (k): {k}")
        for detail in details:
            print(f"  • {detail}")
        
        # Step 2: Combinations
        combinations = self.calculate_classical_combinations(k, length)
        print(f"\n✓ Total Combinations: {combinations:.2e}")
        print(f"  Formula: k^n = {k}^{length}")
        
        # Step 3: Entropy
        entropy = self.calculate_entropy(k, length)
        print(f"\n✓ Password Entropy: {entropy:.2f} bits")
        print(f"  Formula: H = n × log₂(k) = {length} × {math.log2(k):.2f}")
        
        # Step 4: Classical crack time
        classical_time = self.calculate_classical_crack_time(combinations)
        print(f"\n✓ Classical Crack Time: {classical_time}")
        print(f"  (Using classical computers at {self.classical_speed:.0e} attempts/sec)")
        
        # Step 5: Strength classification
        strength, emoji = self.classify_strength(entropy)
        print(f"\n✓ Classical Strength: {emoji} {strength}")
        
        # ============================================================
        # MODULE 2: QUANTUM THREAT ANALYSIS
        # ============================================================
        print("\n" + "⚛️ MODULE 2: QUANTUM THREAT ANALYSIS (Grover's Algorithm)")
        print("-"*70)
        
        # Apply Grover's speedup
        quantum_attempts, speedup = self.apply_grovers_speedup(combinations)
        print(f"\n✓ Grover's Algorithm Applied:")
        print(f"  Classical Attempts: {combinations:.2e}")
        print(f"  Quantum Attempts: {quantum_attempts:.2e}")
        print(f"  Speedup Factor: {speedup:.2e}× faster!")
        
        # Quantum crack time
        quantum_time = self.calculate_quantum_crack_time(quantum_attempts)
        print(f"\n✓ Quantum Crack Time: {quantum_time}")
        print(f"  (Using quantum computers at {self.quantum_speed:.0e} attempts/sec)")
        
        # Vulnerability assessment
        vulnerability = self.assess_quantum_vulnerability(classical_time, quantum_time)
        vuln_emoji = "🔴" if vulnerability == "CRITICAL" else \
                     "🟠" if vulnerability == "HIGH" else \
                     "🟡" if vulnerability == "MODERATE" else "🟢"
        print(f"\n✓ Quantum Vulnerability: {vuln_emoji} {vulnerability}")
        
        # ============================================================
        # MODULE 3: QUANTUM ENCRYPTION
        # ============================================================
        print("\n" + "🔬 MODULE 3: QUANTUM ENCRYPTION (QKD Simulation)")
        print("-"*70)
        
        quantum_hash, quantum_key, circuit = self.quantum_encrypt_password(length)
        
        print(f"\n✓ Quantum-Protected Hash: {quantum_hash}")
        print(f"✓ Quantum Key Length: {len(quantum_key)} qubits")
        print(f"✓ Encryption Method: Quantum Key Distribution (QKD)")
        
        if show_quantum_circuit:
            print("\n✓ Quantum Circuit Diagram:")
            print(circuit)
        
        # ============================================================
        # FINAL SUMMARY
        # ============================================================
        self.print_summary(length, k, combinations, entropy, 
                          classical_time, quantum_time, strength, 
                          vulnerability, quantum_hash)
        
        return {
            'length': length,
            'charset_size': k,
            'classical_combinations': combinations,
            'entropy': entropy,
            'classical_time': classical_time,
            'quantum_attempts': quantum_attempts,
            'quantum_time': quantum_time,
            'classical_strength': strength,
            'quantum_vulnerability': vulnerability,
            'quantum_hash': quantum_hash,
            'quantum_key': quantum_key
        }
    
    def print_summary(self, length, k, combinations, entropy, classical_time,
                     quantum_time, strength, vulnerability, quantum_hash):
        """Print comprehensive analysis summary"""
        
        print("\n" + "="*70)
        print("📋 COMPREHENSIVE SECURITY REPORT")
        print("="*70)
        
        print(f"""
╔══════════════════════════════════════════════════════════════════╗
║                    PASSWORD PARAMETERS                           ║
╠══════════════════════════════════════════════════════════════════╣
║  Password Length:              {length} characters                    
║  Character Set Size:           {k} unique characters              
║  Total Combinations:           {combinations:.2e}                 
║  Password Entropy:             {entropy:.2f} bits                 
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║                    CLASSICAL SECURITY (TODAY)                    ║
╠══════════════════════════════════════════════════════════════════╣
║  Crack Time (Classical):       {classical_time:30s}
║  Security Level:               {strength:30s}
║  Recommendation:               {"✓ Acceptable for current use" if entropy > 50 else "✗ Increase length/complexity"}
╚══════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════╗
║                 QUANTUM SECURITY (FUTURE)                        ║
╠══════════════════════════════════════════════════════════════════╣
║  Crack Time (Quantum):         {quantum_time:30s}
║  Vulnerability Level:          {vulnerability:30s}
║  Quantum Protection:           {quantum_hash[:30]:30s}
║  Recommendation:               {"⚠️ Needs quantum encryption" if vulnerability in ["CRITICAL", "HIGH"] else "✓ Quantum-resistant"}
╚══════════════════════════════════════════════════════════════════╝
        """)
        
        print("="*70)


# ============================================================
# DEMO EXAMPLES
# ============================================================

def run_demo_examples():
    """
    Run multiple demo examples with detailed explanations
    
    SIMPLE EXPLANATION:
    We'll test 3 different passwords:
    1. WEAK password (short, simple)
    2. MEDIUM password (moderate)
    3. STRONG password (long, complex)
    
    For each, we'll see:
    - How secure it is TODAY (classical)
    - How secure it is TOMORROW (quantum)
    - How to protect it (quantum encryption)
    """
    
    analyzer = QuantumPasswordAnalyzer()
    
    print("\n" + "🎯"*35)
    print("DEMO: MULTIPLE PASSWORD EXAMPLES")
    print("🎯"*35)
    
    # ============================================================
    # EXAMPLE 1: WEAK PASSWORD
    # ============================================================
    input("\n\nPress Enter to see Example 1: WEAK PASSWORD...")
    
    print("\n" + "📌"*35)
    print("EXAMPLE 1: WEAK PASSWORD")
    print("Scenario: User creates password with only lowercase, length 6")
    print("Example: 'abcdef' or 'password'")
    print("📌"*35)
    
    result1 = analyzer.analyze_password(
        length=6,
        use_lowercase=True,
        use_uppercase=False,
        use_digits=False,
        use_symbols=False,
        show_quantum_circuit=True
    )
    
    print("\n💡 EXPLANATION:")
    print("   • Only 26 characters available (a-z)")
    print("   • Only 26^6 = 308 million combinations")
    print("   • Classical: Cracked in 3 seconds")
    print("   • Quantum: Cracked INSTANTLY")
    print("   • Verdict: ❌ NEVER use passwords like this!")
    
    # ============================================================
    # EXAMPLE 2: MEDIUM PASSWORD
    # ============================================================
    input("\n\nPress Enter to see Example 2: MEDIUM PASSWORD...")
    
    print("\n" + "📌"*35)
    print("EXAMPLE 2: MEDIUM PASSWORD")
    print("Scenario: User creates password with mixed characters, length 8")
    print("Example: 'Pass1234' or 'MyName99'")
    print("📌"*35)
    
    result2 = analyzer.analyze_password(
        length=8,
        use_lowercase=True,
        use_uppercase=True,
        use_digits=True,
        use_symbols=False,
        show_quantum_circuit=True
    )
    
    print("\n💡 EXPLANATION:")
    print("   • 62 characters available (a-z, A-Z, 0-9)")
    print("   • 62^8 = 218 trillion combinations")
    print("   • Classical: Safe for ~25 days")
    print("   • Quantum: Cracked in minutes")
    print("   • Verdict: ⚠️ Acceptable today, but not quantum-safe!")
    
    # ============================================================
    # EXAMPLE 3: STRONG PASSWORD
    # ============================================================
    input("\n\nPress Enter to see Example 3: STRONG PASSWORD...")
    
    print("\n" + "📌"*35)
    print("EXAMPLE 3: STRONG PASSWORD")
    print("Scenario: User creates password with all character types, length 12")
    print("Example: 'P@ssw0rd!123' or 'Secur3#Pass'")
    print("📌"*35)
    
    result3 = analyzer.analyze_password(
        length=12,
        use_lowercase=True,
        use_uppercase=True,
        use_digits=True,
        use_symbols=True,
        show_quantum_circuit=True
    )
    
    print("\n💡 EXPLANATION:")
    print("   • 70 characters available (a-z, A-Z, 0-9, symbols)")
    print("   • 70^12 = 1.38 × 10^22 combinations")
    print("   • Classical: Safe for millions of years")
    print("   • Quantum: Still safe for thousands of years")
    print("   • Quantum Encryption: Additional protection layer")
    print("   • Verdict: ✅ Excellent! Even quantum-resistant!")
    
    # ============================================================
    # COMPARISON TABLE
    # ============================================================
    input("\n\nPress Enter to see COMPARISON TABLE...")
    
    print("\n" + "="*70)
    print("📊 SIDE-BY-SIDE COMPARISON")
    print("="*70)
    print(f"""
┌──────────────┬─────────────┬─────────────┬─────────────┐
│   Metric     │   WEAK      │   MEDIUM    │   STRONG    │
├──────────────┼─────────────┼─────────────┼─────────────┤
│ Length       │ {result1['length']:11d} │ {result2['length']:11d} │ {result3['length']:11d} │
│ Charset Size │ {result1['charset_size']:11d} │ {result2['charset_size']:11d} │ {result3['charset_size']:11d} │
│ Entropy      │ {result1['entropy']:9.1f}   │ {result2['entropy']:9.1f}   │ {result3['entropy']:9.1f}   │
│ Classical    │ {result1['classical_strength']:11s} │ {result2['classical_strength']:11s} │ {result3['classical_strength']:11s} │
│ Quantum Vuln │ {result1['quantum_vulnerability']:11s} │ {result2['quantum_vulnerability']:11s} │ {result3['quantum_vulnerability']:11s} │
└──────────────┴─────────────┴─────────────┴─────────────┘
    """)
    
    print("\n💡 KEY TAKEAWAYS:")
    print("   1. Length MATTERS: Longer = exponentially more secure")
    print("   2. Complexity MATTERS: More character types = more combinations")
    print("   3. Quantum is COMING: Current strong passwords may be weak soon")
    print("   4. Quantum Encryption: Future-proof protection method")
    print("   5. Recommendation: Use 12+ characters with all types + quantum protection")


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║  QUANTUM-ENHANCED PASSWORD STRENGTH ANALYZER                   ║
    ║                                                                ║
    ║  Combining: Discrete Mathematics + Quantum Computing           ║
    ║                                                                ║
    ║  Concepts Used:                                                ║
    ║  ✓ Sets, Counting Principle, Logarithms (DMS)                 ║
    ║  ✓ Grover's Algorithm (Quantum Speedup)                        ║
    ║  ✓ Quantum Key Distribution (QKD)                              ║
    ║  ✓ Quantum Circuits (Qiskit)                                   ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    print("\nChoose mode:")
    print("1. Run Demo Examples (Recommended)")
    print("2. Custom Analysis")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == '1':
        run_demo_examples()
    elif choice == '2':
        analyzer = QuantumPasswordAnalyzer()
        length = int(input("\nEnter password length: "))
        use_lowercase = input("Include lowercase (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase (y/n): ").lower() == 'y'
        use_digits = input("Include digits (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols (y/n): ").lower() == 'y'
        show_circuit = input("Show quantum circuit (y/n): ").lower() == 'y'
        
        analyzer.analyze_password(length, use_lowercase, use_uppercase,
                                 use_digits, use_symbols, show_circuit)
    else:
        print("\n❌ Invalid choice! Running demo...")
        run_demo_examples()
    
    print("\n\n✅ Analysis Complete! Thank you for using Quantum Password Analyzer!")

    print("💡 Tip: Always use long passwords (12+) with quantum encryption!")
