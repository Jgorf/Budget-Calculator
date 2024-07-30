// Function to add new input fields
function addField(containerId) {
    const container = document.getElementById(containerId);
    const newField = document.createElement('div');
    newField.classList.add('input-group', 'mb-3');
    newField.innerHTML = `
        <input class="input-group-text" type="text" placeholder="Description" name="${containerId}_description">
        <img id="dollar-sign" src="../static/images/dollar-sign.png">
        <input class="form-control" type="number" min="0" placeholder="Amount" name="${containerId}_value">
    `;
    container.appendChild(newField);
}

// Event listeners for buttons
document.getElementById('addNeed').addEventListener('click', function() {
    addField('needsFields');
});

document.getElementById('addWant').addEventListener('click', function() {
    addField('wantsFields');
});

document.getElementById('addSaving').addEventListener('click', function() {
    addField('savingsFields');
});
