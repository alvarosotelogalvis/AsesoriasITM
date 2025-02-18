# Ports
from project.app.schedules.domain.ports.schedulesPort import SchedulePort

# Adapters
from project.app.schedules.adapters.schedulesAdapter import ScheduleAdapter

container = {
    SchedulePort: ScheduleAdapter
}
