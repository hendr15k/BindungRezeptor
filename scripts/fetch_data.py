from chembl_webresource_client.new_client import new_client
import pandas as pd
import time

def fetch_chembl_data():
    target = new_client.target
    activity = new_client.activity

    print("Searching for Targets...")
    # Let's search for a popular target family like "Dopamine receptor"
    # To have a good demo, I will pick 3 distinct targets to classify.

    target_names = ["Dopamine D2 receptor", "Serotonin 1a (5-HT1a) receptor", "Cyclooxygenase-2", "Acetylcholinesterase"]

    all_data = []

    for t_name in target_names:
        print(f"Fetching target info for {t_name}...")
        res = target.filter(pref_name__iexact=t_name)
        if not res:
            print(f"Target {t_name} not found exact, trying search.")
            res = target.search(t_name)

        if not res:
            print(f"Skipping {t_name}")
            continue

        t_chembl_id = res[0]['target_chembl_id']
        print(f"Found {t_name} -> {t_chembl_id}")

        # Fetch bioactivity data
        # IC50 < 1000 nM (active)
        print(f"Fetching bioactivities for {t_chembl_id}...")

        # We want active compounds
        res_act = activity.filter(target_chembl_id=t_chembl_id,
                                  standard_type="IC50",
                                  standard_value__isnull=False).filter(standard_value__lte=1000)

        # Limit to 300 compounds per target to keep things fast and model small
        count = 0
        for act in res_act:
            if count >= 300:
                break
            if 'canonical_smiles' in act and act['canonical_smiles']:
                all_data.append({
                    'SMILES': act['canonical_smiles'],
                    'Target': t_name,
                    'Activity_Value': act['standard_value']
                })
                count += 1
        print(f"Collected {count} active compounds for {t_name}")
        time.sleep(1) # Be nice to API

    df = pd.DataFrame(all_data)

    # Save raw data
    df.to_csv('data/chembl_raw.csv', index=False)
    print(f"Total collected: {len(df)}")
    return df

if __name__ == "__main__":
    fetch_chembl_data()
