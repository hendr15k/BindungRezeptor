// verification/test_model.js
const fs = require('fs');
const path = require('path');

// Load the model file content
const modelPath = path.join(__dirname, '../js/model.js');
const modelCode = fs.readFileSync(modelPath, 'utf8');

// Evaluate the model code in the current context
// This makes predictWithModel and predictClass available
eval(modelCode);

// Mock input features: [MW, LogP, TPSA, HBD, HBA, RotBonds]
// Example: Aspirin roughly [180, 1.2, 63, 1, 3, 2]
const input = [180.16, 1.19, 63.6, 1, 3, 2];

try {
    if (typeof predictWithModel !== 'function') {
        throw new Error("predictWithModel is not defined after evaluating model.js");
    }

    const predictions = predictWithModel(input);
    console.log("Predictions for Aspirin-like input:");
    console.log(JSON.stringify(predictions, null, 2));

    if (!predictions || predictions.length === 0) {
        console.error("No predictions returned.");
        process.exit(1);
    }

    const top = predictions[0];
    if (!top.name || typeof top.probability !== 'number') {
        console.error("Invalid prediction format.");
        process.exit(1);
    }

    console.log("Verification Passed!");
} catch (error) {
    console.error("Error during prediction:", error);
    process.exit(1);
}
