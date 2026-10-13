import pubchempy as pcp 
import time
import pandas as pd


#read the compounds from txt file
with open("../data/organic_compounds.txt", 'r', encoding="utf-8") as file:
    compounds = [entry.strip() for entry in file if entry.strip()]


dataset = []

for i, name in enumerate(compounds[20]):
    try:
        results = pcp.get_compounds(name, 'name')
        if results:
            smiles = results[0].canonical_smiles
            dataset.append({"name": name, "smiles": smiles})
            print(f"[{i+1}/500] Success: {name} -> {smiles}")
        else:
            print(f"[{i+1}/500] Warning: No match found for '{name}'")
    except Exception as e:
        print(f"[{i+1}/500] Error fetching '{name}': {e}")

    time.sleep(1)


df = pd.DataFrame(dataset)
df.to_csv("../data/organic_compounds_smiles.csv", index=False)





