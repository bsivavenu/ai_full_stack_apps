import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "./api";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    setTasks(await getTasks());
  };

  return (
    <div>
      <h2>To-Do</h2>

      <input value={title} onChange={e => setTitle(e.target.value)} />
      <button onClick={async () => {
        await createTask(title);
        setTitle("");
        loadTasks();
      }}>
        Add
      </button>

      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => updateTask(task.id, !task.completed).then(loadTasks)}
            />
            {task.title}
            <button onClick={() => deleteTask(task.id).then(loadTasks)}>X</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
