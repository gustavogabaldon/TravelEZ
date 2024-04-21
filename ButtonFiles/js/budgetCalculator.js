function calculateBudget() {
    var totalBudget = document.getElementById('totalBudget').value;
    if (!totalBudget) {
        alert("Please enter a valid budget amount.");
        return;
    }

    var budget = parseFloat(totalBudget);
    var accommodation = budget * 0.40; // 40% of budget
    var food = budget * 0.20; // 20% of budget
    var activities = budget * 0.10; // 10% of budget
    var transport = budget * 0.15; // 15% of budget
    var other = budget * 0.15; // 15% of budget

    document.getElementById('accommodation').textContent = accommodation.toFixed(2);
    document.getElementById('food').textContent = food.toFixed(2);
    document.getElementById('activities').textContent = activities.toFixed(2);
    document.getElementById('transport').textContent = transport.toFixed(2);
    document.getElementById('other').textContent = other.toFixed(2);
}
