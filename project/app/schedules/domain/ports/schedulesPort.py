class SchedulePort:

    def get_all_schedules(self):
        raise NotImplementedError
    
    def get_schedule(self, **kwargs):
        raise NotImplementedError
    
    def create_schedule(self, **kwargs):
        raise NotImplementedError
    
    def update_schedule(self, group_id: str, **kwargs):
        raise NotImplementedError
