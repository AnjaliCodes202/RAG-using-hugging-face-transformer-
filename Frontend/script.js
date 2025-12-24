async function askQuestion() {
    const question = document.getElementById("question").value;
    const loading = document.getElementById("loading");
    const answerBox = document.getElementById("answer-box");
    const answerEl = document.getElementById("answer");
    const sourcesEl = document.getElementById("sources");

    if (!question.trim()) {
        alert("Please enter a question");
        return;
    }

    loading.classList.remove("hidden");
    answerBox.classList.add("hidden");

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        answerEl.innerText = data.answer;
        sourcesEl.innerHTML = "";

        data.sources.forEach(src => {
            const li = document.createElement("li");
            li.innerText = src;
            sourcesEl.appendChild(li);
        });

        answerBox.classList.remove("hidden");

    } catch (error) {
        alert("Error connecting to backend");
        console.error(error);
    }

    loading.classList.add("hidden");
}
