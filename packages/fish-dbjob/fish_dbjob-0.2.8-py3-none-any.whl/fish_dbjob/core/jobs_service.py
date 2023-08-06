from databricks_cli.jobs.api import JobsApi


class JobsService:

    def __init__(self, api_client):
        self.jobs_api = JobsApi(api_client)
        self.all_jobs = self.list_all_jobs()

    def list_all_jobs(self) -> list:
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

    def jobs(self, name_filter: str = None) -> []:
        if name_filter is None:
            return self.all_jobs
        return [job for job in self.all_jobs if name_filter.lower() in job.name.lower()]


class Job():
    def __init__(self, job_dict: dict):
        self.id: str = job_dict['job_id']
        self.name: str = job_dict['settings']['name']
        self.tags: str = Job._tags(job_dict)

    @staticmethod
    def _tags(job_dict: dict) -> str:
        tags_dict = job_dict['settings'].get('tags', {})
        list = [v or k for (k, v) in tags_dict.items()]

        return ','.join(list)