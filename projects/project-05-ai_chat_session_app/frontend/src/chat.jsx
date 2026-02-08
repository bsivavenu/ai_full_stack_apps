// frontend/src/Chat.jsx

import { useState } from "react";
import { sendMessage } from "./api";

const sessionId = crypto.randomUUID();

export default function Chat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  async function handleSend() {
    if (!input) return;

    const res = await sendMessage(sessionId, input);

    setMessages(res.history);
    setInput("");
  }

  return (
    <div>
      <h2>Mini Chatbot</h2>

      <div>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.content}
          </div>
        ))}
      </div>

      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Type..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}
