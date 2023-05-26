import datetime

class HealthEvent:
    def __init__(self, event_type, date, description, possible_causes):
        self.event_type = event_type
        self.date = date
        self.description = description
        self.possible_causes = possible_causes

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - Event Type: {self.event_type}, Description: {self.description}, Possible Causes: {', '.join(self.possible_causes)}"

class HealthLog:
    def __init__(self):
        self.events = []

    def log_event(self, event_type, description, possible_causes):
        event = HealthEvent(event_type, datetime.datetime.now(), description, possible_causes)
        self.events.append(event)
        print(f"Event logged.")

    def review_events(self):
        for event in self.events:
            print(str(event))

# Sample usage
if __name__ == "__main__":
    health_log = HealthLog()

    health_log.log_event("Daydream", "Got caught in a daydream for a few minutes.", ["High-pitched noise from broken electronics"])
    health_log.log_event("Memory issue", "Couldn't remember where I put my keys.", ["Possible lead in tooth implant"])
    health_log.log_event("Muscle spasm", "Felt a spasm in my throat and jaw.", ["Possible cyst from smoking"])

    print("\nReviewing events:")
    health_log.review_events()
