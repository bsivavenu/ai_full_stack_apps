import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const askAI = async () => {
    const res = await fetch("http://127.0.0.1:8000/ask-ai", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: prompt })
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Test</h1>
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter prompt"
        style={{ width: "400px" }}
      />
      <button onClick={askAI}>Ask AI</button>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
}

export default App;
