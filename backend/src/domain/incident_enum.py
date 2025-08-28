import enum


class IncidentType(str, enum.Enum):
    FIRE = "fire"
    FLOOD = "flood"
    EARTHQUAKE = "earthquake"
    OTHER = "other"
