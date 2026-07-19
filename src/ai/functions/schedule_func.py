from .base import BaseFunction, BaseParameters, StringProperty

schedule_function = BaseFunction(
    name="schedule_todo",
    description="Schedules a task with specified description and given time and date",
    parameters=BaseParameters(
        properties={
            "date": StringProperty(description="Date (e.g., '2024-07-29')"),
            "time": StringProperty(description="Time (e.g., '15:00')"),
            "topic": StringProperty(description="The task topic."),
            "description": StringProperty(description="The description of the task."),
            "comment": StringProperty(description="AI Comment of task from the system.")
        },
        required=["date", "topic", "comment"]
    )
)
