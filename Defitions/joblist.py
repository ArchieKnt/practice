class JobQueue:
    def __init__(self):
        self.jobs = {}
        self.next_id = 1

    def add(self, name, priority):
        job_id = self.next_id
        self.next_id += 1

        self.jobs[job_id] = {
            "name": name,
            "priority": priority,
            "status": "pending"
        }

        return job_id


    def claim_next(self):
        pending = []

        for job_id, job in self.jobs.items():
            if job["status"] == "pending":
                pending.append(job_id)

        if not pending:
            return None

        best_id = min(
            pending,
            key=lambda i: (-self.jobs[i]["priority"], i)
        )

        self.jobs[best_id]["status"] = "running"

        return best_id