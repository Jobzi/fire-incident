import { useState, useEffect } from "react";
import IncidentForm from "./components/IncidentForm";
import IncidentList from "./components/IncidentList";

export default function App() {
  const [incidents, setIncidents] = useState([]);

  const fetchIncidents = async () => {
    const res = await fetch("/api/incidents");
    const data = await res.json();
    setIncidents(data.incidents);
  };

  useEffect(() => {
    fetchIncidents();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>🔥 Fire Incident Mini-Portal</h1>
      <IncidentForm onSuccess={fetchIncidents} />
      <hr />
      <IncidentList incidents={incidents} />
    </div>
  );
}