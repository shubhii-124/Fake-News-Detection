import React, { useState } from "react";

function App() {
    const [newsText, setNewsText] = useState("");
    const [manualResult, setManualResult] = useState(null);
    
    // 📌 **Fake News Detection using FastAPI**
    const checkFakeNews = async () => {
        try {
            console.log("Sending request to backend..."); // Debugging
            const response = await fetch("http://localhost:8080/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: newsText }),
            });

            if (!response.ok) throw new Error(`HTTP Error! Status: ${response.status}`);

            const data = await response.json();
            setManualResult(`Prediction: ${data.prediction} (Confidence: ${data.confidence})`);


        } catch (error) {
            console.error("Error checking fake news:", error);
            alert("Error connecting to backend. Make sure it is running.");
        }
    };

    return (
        <div>
            <h1>📰 Fake News Detector</h1>
            <textarea
                value={newsText}
                onChange={(e) => setNewsText(e.target.value)}
                placeholder="Enter news text here..."
            />
            <button onClick={checkFakeNews}>Check News</button>
            {manualResult && <p>{manualResult}</p>}
        </div>
    );
}

export default App;
