function calculateBudget() {
    const totalBudget = document.getElementById('totalBudget').value;
    if (!totalBudget) {
        alert("Please enter a valid budget amount.");
        return;
    }

    const budget = parseFloat(totalBudget);
    const accommodation = budget * 0.40;
    const food = budget * 0.20;
    const activities = budget * 0.10;
    const transport = budget * 0.15;
    const other = budget * 0.15;

    document.getElementById('accommodation').textContent = accommodation.toFixed(2);
    document.getElementById('food').textContent = food.toFixed(2);
    document.getElementById('activities').textContent = activities.toFixed(2);
    document.getElementById('transport').textContent = transport.toFixed(2);
    document.getElementById('other').textContent = other.toFixed(2);

  
    saveData();
}

function saveData() {
    const budget = {
        userId: '123',  
        data: {
            accommodation: document.getElementById('accommodation').textContent,
            food: document.getElementById('food').textContent,
            activities: document.getElementById('activities').textContent,
            transport: document.getElementById('transport').textContent,
            other: document.getElementById('other').textContent
        }
    };

    fetch('/budget/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(budget)
    })
    .then(response => response.json())
    .then(data => console.log('Data saved:', data))
    .catch(error => console.error('Error:', error))
}
