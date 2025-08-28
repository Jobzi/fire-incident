
interface Incident {
    id: string;
    title: string;
    incident_type: string;
    description?: string;
    location?: string;
    image?: string;
}

const IMAGE_BASE_URL = "/uploads/";

export default function IncidentList({ incidents }: { incidents: Incident[] }) {
  return (
    <div>
      <h2>Incidents</h2>
      {incidents.length === 0 ? <p>No incidents yet.</p> : (
        <ul>
          {incidents.map((inc) => (
            <li key={inc.id} style={{ marginBottom: "15px" }}>
              <strong>{inc.title}</strong> ({inc.incident_type}) <br />
              {inc.image && <img src={`${IMAGE_BASE_URL}${inc.image}`} alt={inc.title} style={{ maxWidth: "200px", borderRadius: "8px" }} />} <br />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}