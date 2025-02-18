# Ports
from project.app.professors.domain.ports.professorsPort import ProfesorPort

# Adapters
from project.app.professors.adapters.professorsAdapter import ProfesorAdapter

container = {
    ProfesorPort: ProfesorAdapter
}
