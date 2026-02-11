import { useState } from "react";

function App() {
  const [files, setFiles] = useState([]);
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(false);

  const uploadFiles = async () => {
    if (files.length === 0) {
      alert("Select files first");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    files.forEach((file) => {
      formData.append("files", file);
    });

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    // BACKEND RETURNS: { saved, invoices }
    setInvoices(data.invoices || []);
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>AI Invoice Intelligence</h2>

      <input
        type="file"
        multiple
        onChange={(e) => setFiles(Array.from(e.target.files))}
      />

      <br /><br />

      <button onClick={uploadFiles} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      <hr />

      <h3>Saved Invoices</h3>

      {invoices.length === 0 && <p>No invoices yet</p>}

      {invoices.map((inv) => (
        <div key={inv.id}>
          #{inv.id} — {inv.filename}
        </div>
      ))}
    </div>
  );
}

export default App;
