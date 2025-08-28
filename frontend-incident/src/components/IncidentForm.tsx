import { useState } from "react";

export default function IncidentForm({ onSuccess }: { onSuccess: () => void }) {
  const [title, setTitle] = useState("");
  const [incidentType, setIncidentType] = useState("fire");
  const [description, setDescription] = useState("");
  const [location, setLocation] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("title", title);
    formData.append("incident_type", incidentType);
    if (description) formData.append("description", description);
    if (location) formData.append("location", location);

    await fetch("/api/incidents", {
      method: "POST",
      body: formData,
    });

    setTitle("");
    setIncidentType("fire");
    setDescription("");
    setLocation("");

    onSuccess();
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <h2>Create Incident</h2>
      <div>
        <label htmlFor="title">Title: *</label>
        <input
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="incidentType">Type: *</label>
        <select
          id="incidentType"
          value={incidentType}
          onChange={(e) => setIncidentType(e.target.value)}
        >
          <option value="fire">Fire</option>
          <option value="flood">Flood</option>
          <option value="earthquake">Earthquake</option>
          <option value="other">Other</option>
        </select>
      </div>
      <div>
        <label>Description:</label>
        <textarea
          placeholder="Enter a description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div>
        <label>Location:</label>
        <input
          id="location"
          placeholder="Enter a location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}
