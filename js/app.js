const potentialTargets = [
    // These are fallback targets if model fails or for decoration
    "Cyclooxygenase-1 (COX-1)",
    "Cyclooxygenase-2 (COX-2)",
    "Dopamin-Rezeptor D2",
    "Serotonin-Rezeptor 5-HT1A",
    "Acetylcholinesterase"
];

async function predictTargets() {
    const smiles = document.getElementById('smilesInput').value.trim();
    const resultDiv = document.getElementById('result');
    const img = document.getElementById('mol-image');
    const tbody = document.getElementById('results-body');
    const note = document.querySelector('.simulation-note');

    if (!smiles) {
        alert("Bitte geben Sie einen gültigen SMILES-String ein.");
        return;
    }

    // Reset display
    resultDiv.style.display = 'none';
    tbody.innerHTML = '<tr><td colspan="2">Lade Daten und berechne...</td></tr>';
    resultDiv.style.display = 'block';

    // Fetch Image
    const imageUrl = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/${encodeURIComponent(smiles)}/PNG?record_type=2d&image_size=300x300`;
    img.onerror = function() {
        this.src = 'https://via.placeholder.com/300x300?text=Struktur+nicht+verfügbar';
    };
    img.src = imageUrl;

    try {
        // Fetch Properties from PubChem for the Model
        // Needed: MW, LogP, TPSA, HBD, HBA, RotBonds
        const propsUrl = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/${encodeURIComponent(smiles)}/property/MolecularWeight,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount,RotatableBondCount/JSON`;

        const response = await fetch(propsUrl);
        if (!response.ok) throw new Error("PubChem API Request Failed");

        const data = await response.json();
        const props = data.PropertyTable.Properties[0];

        // Map to feature vector [mw, logp, tpsa, hbd, hba, rot_bonds]
        // Note: XLogP is used as approximation for RDKit MolLogP
        const features = [
            parseFloat(props.MolecularWeight),
            parseFloat(props.XLogP || 0), // Handle missing LogP
            parseFloat(props.TPSA),
            parseFloat(props.HBondDonorCount),
            parseFloat(props.HBondAcceptorCount),
            parseFloat(props.RotatableBondCount)
        ];

        console.log("Features:", features);

        if (typeof predictWithModel === 'function') {
            const predictions = predictWithModel(features);
            displayResults(predictions, tbody);
            note.innerHTML = "(Hinweis: Vorhersage basiert auf einem Random Forest Modell trainiert mit ChEMBL Daten.)";
        } else {
            throw new Error("Model definition not found");
        }

    } catch (e) {
        console.error("Prediction Error:", e);
        // Fallback to simulation if fetch fails
        tbody.innerHTML = '';
        generateMockResults(tbody);
        note.innerHTML = "(Fehler: Konnte keine echten Daten abrufen. Dies ist eine Simulation.)";
    }
}

function displayResults(results, tbody) {
    tbody.innerHTML = '';
    // Show top 3 or all if fewer
    results.slice(0, 5).forEach(res => {
        const probPercent = (res.probability * 100).toFixed(1);
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${res.name}</td>
            <td>
                <div class="probability-bar-container">
                    <div class="probability-bar" style="width: ${probPercent}%"></div>
                </div>
                ${probPercent}%
            </td>
        `;
        tbody.appendChild(row);
    });
}

function generateMockResults(tbody) {
     // Generate Mock Data (Fallback)
    const numTargets = Math.floor(Math.random() * 3) + 3;
    const shuffled = potentialTargets.slice().sort(() => 0.5 - Math.random());
    const selectedTargets = shuffled.slice(0, numTargets);

    let results = selectedTargets.map(target => {
        return {
            name: target,
            probability: Math.random()
        };
    });

    results.sort((a, b) => b.probability - a.probability);
    displayResults(results, tbody);
}
