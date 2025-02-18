# Ports
from project.app.professors.domain.ports.professorsPort import professorPort

# Adapters
from project.app.professors.adapters.professorsAdapter import professorAdapter

container = {
    professorPort: professorAdapter
}
