const API = "http://localhost:8000"

async function analyzeSingle() {
    const text = document.getElementById("inputText").value.trim()
    if (!text) return

    const res = await fetch(`${API}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    })

    const data = await res.json()
    const label = data.prediction.label
    const score = (data.prediction.score * 100).toFixed(1)
    const isPositive = label === "POSITIVE"

    const div = document.getElementById("singleResult")
    div.className = `result ${isPositive ? "positive" : "negative"}`
    div.innerHTML = `
        <span class="label-${isPositive ? "positive" : "negative"}">${label}</span>
        <p class="score">Confidence: ${score}%</p>
        <p style="margin-top:8px;color:#94a3b8">"${text}"</p>
    `
}

async function analyzeBatch() {
    const raw = document.getElementById("batchText").value.trim()
    if (!raw) return

    const texts = raw.split("\n").filter(t => t.trim())

    const res = await fetch(`${API}/predict/batch`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texts })
    })

    const data = await res.json()
    const div = document.getElementById("batchResult")
    div.className = "result"

    div.innerHTML = `<p style="color:#64748b;margin-bottom:12px">${data.total} results</p>` +
        data.results.map(r => {
            const isPositive = r.prediction.label === "POSITIVE"
            const score = (r.prediction.score * 100).toFixed(1)
            return `
                <div class="batch-item">
                    <span class="label-${isPositive ? "positive" : "negative"}">${r.prediction.label}</span>
                    <span class="score"> — ${score}% confidence</span>
                    <p style="color:#94a3b8;margin-top:4px">"${r.text}"</p>
                </div>
            `
        }).join("")
}