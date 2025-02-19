class SchedulePort:

    def get_all_schedules(self):
        raise NotImplementedError
    
    def get_schedules_by_group(self, group_id: int, professor_id: int):
        raise NotImplementedError
    
    def create_schedule(self, **kwargs):
        raise NotImplementedError
