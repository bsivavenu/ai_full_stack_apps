import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://127.0.0.1:8000/echo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: message,
      }),
    });

    const data = await res.json();
    console.log(data);
    setResponse(data.reply);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h2>Echo App</h2>

      <input
        type="text"
        value={message}
        placeholder="Type something..."
        onChange={(e) => setMessage(e.target.value)}
        style={{ padding: "8px", width: "300px" }}
      />

      <br /><br />

      <button onClick={sendMessage}>Send</button>

      <p><b>Response:</b> {response}</p>
    </div>
  );
}

export default App;
