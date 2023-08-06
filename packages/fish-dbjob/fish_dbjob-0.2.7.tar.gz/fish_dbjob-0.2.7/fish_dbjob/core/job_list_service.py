from databricks_cli.jobs.api import JobsApi


class JobListService:

    def __init__(self, api_client):
        self.jobs_api = JobsApi(api_client)
        self.all_jobs = self.list_all_jobs()

    def list_all_jobs(self) -> dict:
        has_more = True
        jobs = []
        offset = 0
        limit = 20

        while has_more:
            jobs_json = self.jobs_api.list_jobs(offset=offset, limit=limit, version='2.1')
            jobs += jobs_json['jobs'] if 'jobs' in jobs_json else []
            has_more = jobs_json.get('has_more', False)  # default to False
            if has_more:
                offset = offset + (len(jobs_json['jobs']) if 'jobs' in jobs_json else 20)

        return [Job(job) for job in jobs]

    def jobs(self, by_name: str) -> []:
        if by_name is None:
            return self.all_jobs
        return [job for job in self.all_jobs if by_name.lower() in job.name.lower()]


class Job():
    def __init__(self, job_dict: dict):
        self.id = job_dict['job_id']
        self.name = job_dict['settings']['name']
        self.tags = job_dict['settings'].get('tags', [])
        # self.tags = [f'{k}:{v}' for (k, v) in self.tags_dict.items()] if len(self.tags_dict)>0 else None

        pass
