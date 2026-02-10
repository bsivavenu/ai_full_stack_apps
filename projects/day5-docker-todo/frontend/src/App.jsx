import { useEffect, useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/todos") 
      .then((res) => res.json())
      .then((data) => {
        setTodos(data)
        console.log("Fetched todos:", data);
      })
      .catch((err) => console.error("Error:", err));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Docker To-Do App</h1>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
