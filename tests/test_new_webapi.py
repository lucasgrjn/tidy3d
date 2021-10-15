""" tests converted webapi """
import pytest

import tidy3d as td
import tidy3d.web as web

from .utils import SIM_CONVERT as sim_original
from .utils import clear_tmp

PATH_JSON = "tests/tmp/simulation.json"
PATH_SIM_DATA = "tests/tmp/sim_data.hdf5"
PATH_DIR_SIM_DATA = "tests/tmp/"


""" core webapi """

task_id_global = []


def _get_gloabl_task_id():
    """returns the task id from the list"""
    return task_id_global[0]

@clear_tmp
def test_webapi_0_run():
    """ test complete run"""
    sim_data = web.run(simulation=sim_original, task_name="test_webapi")

def test_webapi_1_upload():
    """test that task uploads ok"""
    task_id = web.upload(simulation=sim_original, task_name="test_webapi")
    task_id_global.append(task_id)


def test_webapi_2_get_info():
    """test that we can grab information about task"""
    task_id = _get_gloabl_task_id()
    _ = web.get_info(task_id)


def test_webapi_3_start():
    """test that we can start running task"""
    task_id = _get_gloabl_task_id()
    web.start(task_id)


def test_webapi_4_monitor():
    """test that we can monitor task"""
    task_id = _get_gloabl_task_id()
    web.monitor(task_id)


@clear_tmp
def test_webapi_5_download():
    """download the simulation data"""
    task_id = _get_gloabl_task_id()
    web.download(task_id, simulation=sim_original, path=PATH_SIM_DATA)


@clear_tmp
def test_webapi_6_load():
    """load the results into sim_data"""
    task_id = _get_gloabl_task_id()
    sim_data = web.load(task_id, simulation=sim_original, path=PATH_SIM_DATA)
    first_monitor_name = list(sim_original.monitors.keys())[0]
    _ = sim_data[first_monitor_name]


def _test_webapi_7_delete():
    """test that we can monitor task"""
    task_id = _get_gloabl_task_id()
    web.delete(task_id)
    task_info = web.get_info(task_id)
    assert task_info.status in ("deleted", "deleting")


""" Jobs """


jobs_global = []

def _get_gloabl_job():
    """returns the task id from the list"""
    return jobs_global[0]

@clear_tmp
def test_job_0_run():
    """ test complete run"""
    job = web.Job(simulation=sim_original, task_name="test_job")
    job.run()


def test_job_1_upload():
    """test that task uploads ok"""
    job = web.Job(simulation=sim_original, task_name="test_job")
    job.upload()
    jobs_global.append(job)


def test_job_2_get_info():
    """test that we can grab information about task"""
    job = _get_gloabl_job()
    _ = job.get_info()


def test_job_3_start():
    """test that we can start running task"""
    job = _get_gloabl_job()
    job.start()


def test_job_4_monitor():
    """test that we can monitor task"""
    job = _get_gloabl_job()
    job.monitor()


@clear_tmp
def test_job_5_download():
    """download the simulation data"""
    job = _get_gloabl_job()
    job.download(path=PATH_SIM_DATA)


@clear_tmp
def test_job_6_load():
    """load the results into sim_data"""
    job = _get_gloabl_job()
    sim_data = job.load_data(path=PATH_SIM_DATA)
    first_monitor_name = list(sim_original.monitors.keys())[0]
    _ = sim_data[first_monitor_name]


def _test_job_7_delete():
    """test that we can monitor task"""
    job = _get_gloabl_job()
    job.delete()
    task_info = job.get_info()
    assert task_info.status in ("deleted", "deleting")


""" Batches """


batches_global = []

def _get_gloabl_batch():
    """returns the task id from the list"""
    return batches_global[0]

@clear_tmp
def test_batch_0_run():
    """ test complete run"""
    sims = 2*[sim_original]
    simulations = {f'task_{i}': sims[i] for i in range(len(sims))}
    batch = web.Batch(simulations=simulations)
    batch.run()


def test_batch_1_upload():
    """test that task uploads ok"""
    sims = 2*[sim_original]
    simulations = {f'task_{i}': sims[i] for i in range(len(sims))}
    batch = web.Batch(simulations=simulations)
    batch.upload()
    batches_global.append(batch)


def test_batch_2_get_info():
    """test that we can grab information about task"""
    batch = _get_gloabl_batch()
    _ = batch.get_info()


def test_batch_3_start():
    """test that we can start running task"""
    batch = _get_gloabl_batch()
    batch.start()


def test_batch_4_monitor():
    """test that we can monitor task"""
    batch = _get_gloabl_batch()
    batch.monitor()


@clear_tmp
def test_batch_5_download():
    """download the simulation data"""
    batch = _get_gloabl_batch()
    batch.download(path_dir=PATH_DIR_SIM_DATA)


@clear_tmp
def test_batch_6_load():
    """load the results into sim_data"""
    batch = _get_gloabl_batch()
    sim_data_dict = batch.load_data(path_dir=PATH_DIR_SIM_DATA)
    first_monitor_name = list(sim_original.monitors.keys())[0]
    for sim_data in sim_data_dict:
        _ = sim_data[first_monitor_name]

def _test_batch_7_delete():
    """test that we can monitor task"""
    batch = _get_gloabl_batch()
    batch.delete()
    for job in batch:
        task_info = job.get_info()
        assert task_info.status in ("deleted", "deleting")


