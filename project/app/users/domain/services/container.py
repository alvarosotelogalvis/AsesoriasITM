# Ports
from project.app.users.domain.ports.userPort import UserPort

# Adapters
from project.app.users.adapters.userAdapter import UserAdapter

container = {
    UserPort: UserAdapter
}
