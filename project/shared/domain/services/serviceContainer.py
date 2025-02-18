from project.app.professors.domain.services.container import container as professors_container
from project.app.users.domain.services.container import container as user_container
from project.app.schedules.domain.services.container import container as schedule_container

import inspect

container = {
    **professors_container,
    **user_container,
    **schedule_container
}


def get_instance(clazz):
    parameters = inspect.signature(clazz.__init__).parameters
    params = {name: param.annotation for name, param in parameters.items()}

    args = {}
    for name, param_type in params.items():
        if param_type is not inspect._empty:
            args[name] = get_instance(param_type)
    if clazz in container:
        return container[clazz](**args)
    return clazz(**args)
