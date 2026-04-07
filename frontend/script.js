async function predict() {
    // get values
    const hours = parseFloat(document.getElementById("hours").value);
    const focus = parseFloat(document.getElementById("focus").value);
    const sleep = parseFloat(document.getElementById("sleep").value);
    const difficulty = parseFloat(document.getElementById("difficulty").value);

    const resultEl = document.getElementById("result");

    // 🔒 validation
    if (
        isNaN(hours) ||
        isNaN(focus) ||
        isNaN(sleep) ||
        isNaN(difficulty)
    ) {
        resultEl.innerText = "⚠️ please fill all fields correctly";
        return;
    }

    // loading state
    resultEl.innerText = "⏳ predicting...";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                hours_studied: hours,
                focus_level: focus,
                sleep_hours: sleep,
                difficulty: difficulty
            })
        });

        // check response
        if (!response.ok) {
            throw new Error("server error");
        }

        const data = await response.json();

        // update UI
        resultEl.innerText = `${data.predicted_time} hrs`;

    } catch (error) {
        console.error(error);
        resultEl.innerText = "❌ error connecting to server";
    }
}