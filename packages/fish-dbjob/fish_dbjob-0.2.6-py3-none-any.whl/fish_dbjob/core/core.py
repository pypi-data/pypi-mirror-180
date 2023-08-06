from fish_dbjob.core.job_list_service import JobListService


def jobs(api_client, name: str = None):
    job_list_service = JobListService(api_client)
    jobs = job_list_service.jobs_by(name)

    print(f'jobs size: {len(jobs)}')
