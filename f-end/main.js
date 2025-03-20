// Fragen aus JSON-Datei laden
async function loadQuestions() {
    const response = await fetch("/questions.json");
    const questions = await response.json();
    displayQuestions(questions);
}

// Fragen in HTML anzeigen
function displayQuestions(questions) {
    const container = document.getElementById("questions-container");
    container.innerHTML = ""; 
    
    questions.forEach(q => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("question");
        questionDiv.innerHTML = `<strong>[${q.type}] ${q.name}</strong><br>${q.text}`;
        container.appendChild(questionDiv);
    });
}

// Event-Listener für den Filter
document.getElementById("filter-btn").addEventListener("click", async () => {
    const keyword = document.getElementById("search").value.toLowerCase();
    
    const response = await fetch("/questions.json");
    let questions = await response.json();
    
    if (keyword) {
        questions = questions.filter(q => q.text.toLowerCase().includes(keyword));
    }
    
    displayQuestions(questions);
});

// Fragen beim Laden der Seite abrufen
loadQuestions();
