from fish_dbjob.core.job_list_service import JobListService


def jobs(api_client, by_name: str = None) -> []:
    job_list_service = JobListService(api_client)
    jobs = job_list_service.jobs(by_name)

    print(f'jobs size: {len(jobs)}')
    return jobs
