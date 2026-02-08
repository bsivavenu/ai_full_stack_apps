import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setSummary("");
    console.log("Uploading file:", file.name);
    console.log("FormData content:", formData.get("file"));
    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    console.log("Response from server:", data);
    setSummary(data.summary || data.error);
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>AI Document Reader</h2>

      <input
        type="file"
        accept=".pdf,.docx"
        multiple={true}
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Summarize"}
      </button>

      {summary && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
