const API = "http://localhost:8000";

export const getTasks = async () =>
  fetch(`${API}/tasks`).then(res => res.json());

export const createTask = async (title) =>
  fetch(`${API}/tasks?title=${title}`, { method: "POST" });

export const updateTask = async (id, completed) =>
  fetch(`${API}/tasks/${id}?completed=${completed}`, { method: "PUT" });

export const deleteTask = async (id) =>
  fetch(`${API}/tasks/${id}`, { method: "DELETE" });
