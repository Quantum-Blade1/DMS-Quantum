import math
import json
import secrets
import string
import base64
from datetime import timedelta
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from tabulate import tabulate

class QuantumAuthTool:
    def __init__(self):
        self.GUESSES_PER_SEC = 10**8  # 100 Million attempts/sec
        self.backend = Aer.get_backend('qasm_simulator')

    # ============================================================
    # MODULE 1: DISCRETE MATHEMATICS (CLASSICAL ANALYSIS)
    # ============================================================
    def detect_charsets(self, password):
        sets = {
            "lowercase": any(c in string.ascii_lowercase for c in password),
            "uppercase": any(c in string.ascii_uppercase for c in password),
            "digits": any(c in string.digits for c in password),
            "symbols": any(c in string.punctuation for c in password),
            "whitespace": any(c in string.whitespace for c in password)
        }
        
        # Calculate Cardinality (A)
        alphabet_size = (26 if sets["lowercase"] else 0) + \
                        (26 if sets["uppercase"] else 0) + \
                        (10 if sets["digits"] else 0) + \
                        (32 if sets["symbols"] else 0) + \
                        (1 if sets["whitespace"] else 0)
        return sets, max(alphabet_size, 1)

    def classify_security(self, entropy):
        if entropy < 40: return "Very Weak"
        if entropy < 60: return "Weak"
        if entropy < 80: return "Moderate"
        if entropy < 128: return "Strong"
        return "Very Strong"

    # ============================================================
    # MODULE 2: QUANTUM COMPUTING (GROVER'S SIMULATION)
    # ============================================================
    def simulate_quantum_threat(self, N):
        """
        Simulates Grover's Algorithm complexity O(√N).
        NOTE: This is a mathematical simulation of quantum speedup.
        """
        quantum_attempts = math.sqrt(N)
        q_time = quantum_attempts / self.GUESSES_PER_SEC
        speedup = math.sqrt(N) if N > 0 else 1
        return q_time, speedup

    # ============================================================
    # MODULE 3: QUANTUM KEY DISTRIBUTION (QKD SIMULATION)
    # ============================================================
    def simulate_qkd_and_encrypt(self, suggestion):
        """
        Simulates BB84-style QKD using a Bell-state circuit.
        Hadamard (H) creates superposition; CNOT creates entanglement.
        """
        # Create an 8-qubit quantum key
        qc = QuantumCircuit(8)
        for i in range(8):
            qc.h(i)   # Superposition
            if i > 0:
                qc.cx(i-1, i) # Entanglement
        
        qc.measure_all()
        job = self.backend.run(qc, shots=1)
        key_bits = list(job.result().get_counts().keys())[0]
        
        # Simple XOR-style simulation for "Quantum Ciphertext"
        key_int = int(key_bits, 2)
        encrypted_bytes = bytes([b ^ (key_int % 256) for b in suggestion.encode()])
        
        return {
            "ciphertext": base64.b64encode(encrypted_bytes).decode(),
            "qkd_key_fingerprint": hex(key_int)
        }

    # ============================================================
    # SUGGESTION ENGINE
    # ============================================================
    def get_improvements(self, password, entropy):
        recs = []
        if len(password) < 12: recs.append("Increase length to at least 12 characters.")
        if not any(c.isdigit() for c in password): recs.append("Include numbers (0-9).")
        if not any(c in string.punctuation for c in password): recs.append("Add special symbols (e.g., @, #, $).")
        if entropy < 60: recs.append("Current entropy is low; use a passphrase of 4+ random words.")
        return recs

    def generate_random_password(self, length=16):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    # ============================================================
    # MAIN ANALYSIS EXECUTION
    # ============================================================
    def analyze(self, password):
        # 1. Classical DMS Analysis
        charsets, A = self.detect_charsets(password)
        L = len(password)
        N = A**L  # Counting Principle
        entropy = L * math.log2(A) # Logarithms
        c_time = N / self.GUESSES_PER_SEC
        
        # 2. Quantum Analysis
        q_time, speedup = self.simulate_quantum_threat(N)
        
        # 3. Security Scoring
        rating = self.classify_security(entropy)
        
        # 4. Generate Suggestions
        recs = self.get_improvements(password, entropy)
        new_random = self.generate_random_password()
        q_encryption = self.simulate_qkd_and_encrypt(new_random)

        # Build JSON Output
        report = {
            "input_password": password,
            "length": L,
            "charsets": {**charsets, "alphabet_size": A},
            "classical": {
                "combinations": N,
                "entropy_bits": round(entropy, 2),
                "crack_time_seconds": c_time
            },
            "quantum": {
                "quantum_crack_time_seconds": q_time,
                "speedup_factor": speedup
            },
            "security_classification": rating,
            "suggestions": recs,
            "password_suggestions": [
                {"type": "passphrase", "value": "Correct-Horse-Battery-Staple"},
                {"type": "random", "value": new_random},
                {"type": "quantum_encrypted", **q_encryption}
            ]
        }
        return report

    def print_summary(self, data):
        print(f"\n{'='*60}")
        print(f"       SECURE AUDIT: {data['security_classification'].upper()}")
        print(f"{'='*60}")
        
        dms_table = [
            ["Password Length (L)", data['length']],
            ["Alphabet Size (A)", data['charsets']['alphabet_size']],
            ["Entropy (bits)", f"{data['classical']['entropy_bits']} bits"],
            ["Combinations (A^L)", f"{data['classical']['combinations']:.2e}"]
        ]
        
        time_table = [
            ["Method", "Crack Time Estimate", "Algorithm Complexity"],
            ["Classical CPU", self.format_time(data['classical']['crack_time_seconds']), "O(N)"],
            ["Quantum (Grover)", self.format_time(data['quantum']['quantum_crack_time_seconds']), "O(√N)"]
        ]

        print("\n[DMS CALCULATIONS]")
        print(tabulate(dms_table, tablefmt="simple"))
        
        print("\n[CRACK TIME COMPARISON (Theoretical)]")
        print(tabulate(time_table, headers="firstrow", tablefmt="fancy_grid"))
        
        if data['suggestions']:
            print("\n[IMPROVEMENT SUGGESTIONS]")
            for s in data['suggestions']: print(f" - {s}")

        print("\n[QUANTUM-PROTECTED SUGGESTION]")
        qs = data['password_suggestions'][2]
        print(f" QKD Key Fingerprint: {qs['qkd_key_fingerprint']}")
        print(f" Quantum Ciphertext: {qs['ciphertext']}")

    def format_time(self, seconds):
        if seconds < 1: return "Instantaneous"
        if seconds > 10**15: return "Indefinite (Ages of the Universe)"
        try:
            return str(timedelta(seconds=int(seconds)))
        except:
            return f"{seconds:.2e} seconds"

# Run Example
if __name__ == "__main__":
    tool = QuantumAuthTool()
    user_input = input("Enter password to analyze: ")
    result = tool.analyze(user_input)
    
    tool.print_summary(result)
    
    # Save JSON to file or print
    # print("\n[JSON DATA OUTPUT]")
    # print(json.dumps(result, indent=2))
