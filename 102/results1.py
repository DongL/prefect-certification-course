import pandas as pd
from prefect import flow, get_run_logger, task


@task(persist_result=True)
def my_task():
    df = pd.DataFrame(dict(a=[2, 3], b=[4, 5]))
    logger = get_run_logger()
    logger.info("INFO level log message - my task logs.")
    return df


@flow()
def my_flow():
    res = my_task()


my_flow()
