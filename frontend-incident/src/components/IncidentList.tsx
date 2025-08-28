
interface Incident {
    id: string;
    title: string;
    incident_type: string;
    description?: string;
    location?: string;
}

export default function IncidentList({ incidents }: { incidents: Incident[] }) {
  return (
    <div>
      <h2>Incidents</h2>
      {incidents.length === 0 ? <p>No incidents yet.</p> : (
        <ul>
          {incidents.map((inc) => (
            <li key={inc.id} style={{ marginBottom: "15px" }}>
              <strong>{inc.title}</strong> ({inc.incident_type}) <br />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}