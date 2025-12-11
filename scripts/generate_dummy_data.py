import pandas as pd
import random
from rdkit import Chem
from rdkit.Chem import AllChem

# List of dummy targets
TARGETS = [
    "Cyclooxygenase-1 (COX-1)",
    "Cyclooxygenase-2 (COX-2)",
    "Dopamin-Rezeptor D2",
    "Serotonin-Rezeptor 5-HT1A",
    "Acetylcholinesterase",
    "Angiotensin-Konversionsenzym (ACE)",
    "Beta-2 Adrenerger Rezeptor",
    "Muscarinischer Acetylcholinrezeptor M3",
    "Histamin-H1-Rezeptor",
    "Cannabinoid-Rezeptor 1",
    "Estrogen-Rezeptor Alpha",
    "Glucocorticoid-Rezeptor",
    "P2Y Purinozeptor 12"
]

# Generate some valid SMILES (Aspirin derivatives / common drugs for testing)
SMILES_LIST = [
    "CC(=O)OC1=CC=CC=C1C(=O)O", # Aspirin
    "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", # Caffeine
    "CC1=CC=C(C=C1)O", # p-Cresol
    "C1=CC=C(C=C1)O", # Phenol
    "CC(=O)NC1=CC=C(C=C1)O", # Paracetamol
    "C1=CC=C(C=C1)C(=O)O", # Benzoic acid
    "C1=CC=C(C=C1)N", # Aniline
    "CCO", # Ethanol
    "CCN(CC)CC", # Triethylamine
    "C1CCCCC1", # Cyclohexane
]

# Generate more synthetic SMILES by simple mutations (invalid chemically but valid string for test)
# or just repeat with different targets
data = []

print("Generating dummy dataset...")

for i in range(100):
    smiles = random.choice(SMILES_LIST)
    # Assign 1-3 random targets
    n_targets = random.randint(0, 3)
    targets = random.sample(TARGETS, n_targets)

    # Store as SMILES, Target1, Target2, ... (One hot encoded or list)
    # Ideally, for multi-label, we have columns for each target
    row = {'SMILES': smiles}
    for t in TARGETS:
        row[t] = 1 if t in targets else 0
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('data/dummy_molecules.csv', index=False)
print(f"Dataset with {len(df)} samples saved to data/dummy_molecules.csv")
