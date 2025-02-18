# Ports
from project.app.profesors.domain.ports.profesorsPort import ProfesorPort

# Adapters
from project.app.profesors.adapters.profesorsAdapter import ProfesorAdapter

container = {
    ProfesorPort: ProfesorAdapter
}
