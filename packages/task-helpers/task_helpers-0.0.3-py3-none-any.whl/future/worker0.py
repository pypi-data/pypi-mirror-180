import time
import multiprocessing
import random
import logging
import queue
import threading
import gc
import datetime


class BaseWorkerHandler:
    count_workers = 1
    iterations_to_restart = 100
    iterations_to_restart_jitter = 20
    worker_class = None
    task_helper_class = None

    def __init__(self, **kwargs):
        self.threads = queue.Queue()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def new_process_starter(self):
        while True:
            try:
                process = multiprocessing.Process(
                    target=self._perform_worker,
                    name=self.worker_class.__name__)
                process.daemon = True
                process.start()
                process.join()
                del process
                gc.collect()
                time.sleep(0.1)
            except Exception as ex:
                print(
                    f"An error has occured on WorkerHandler."
                    f"new_process_starter: {ex}")
                logging.error(
                    f"An error has occured on WorkerHandler."
                    f"new_process_starter: {ex}")
                time.sleep(1)

    def _perform_worker(self):
        try:
            iterations_to_restart = self.iterations_to_restart + \
                random.randint(0, self.iterations_to_restart_jitter)
            task_helper = self.task_helper_class()
            worker = self.worker_class(task_helper=task_helper)
            worker.perform(total_iterations=iterations_to_restart)
            time.sleep(0.1)
        except Exception as ex:
            print(
                f"An error has occured on WorkerHandler._perform_worker: {ex}")
            logging.error(
                f"An error has occured on WorkerHandler._perform_worker: {ex}")

    def perform(self):
        for num in range(1, self.count_workers+1):
            try:
                thread = threading.Thread(target=self.new_process_starter)
                thread.start()
                self.threads.put(thread)
                # print(f"started new thread for worker {self.worker_class}")
            except Exception as ex:
                print(
                    f"An error has occured on WorkerHandler.perform: {ex}")
                logging.error(
                    f"An error has occured on WorkerHandler.perform: {ex}")
        self.threads.join()


class BaseWorker:
    task_helper = None
    queue_name = None
    tasks_per_iteration = 500
    gradient_sleep_time = None  # or (min_sleep_time, max_sleep_time)
    empty_queue_sleep_time = 1
    after_iteration_sleep_time = 1
    iteration_max_sleep_time = 1
    return_task_result = True
    return_task_to_queue_if_error = False
    start_timer_after_first_task = False

    def __init__(self, task_helper, **kwargs):
        self.helper = task_helper
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_sleep_time(self, count_tasks):
        if self.gradient_sleep_time:
            min_sleep_time = min(self.gradient_sleep_time)
            max_sleep_time = max(self.gradient_sleep_time)
            coefficient_tasks = count_tasks / self.tasks_per_iteration
            time_difference = max_sleep_time - min_sleep_time
            return min_sleep_time + (1 - coefficient_tasks) * time_difference
        else:
            if count_tasks > 0:
                return self.after_iteration_sleep_time
            return self.empty_queue_sleep_time

    def perform_many_tasks(self, tasks):
        raise NotImplementedError

    def return_tasks_with_error(self, tasks):
        try:
            for task in tasks:
                self.helper.add_task_to_queue(
                    queue_name=self.queue_name,
                    task_data=task[1])
        except Exception as ex:
            logging.error(
                f"An error has occured on Worker.perform"
                f"when returning tasks to queue after error. "
                f"queue_name: {self.queue_name}, Exception: {ex}"
            )

    def perform_gradient_sleep_time(self, total_iterations):
        # print(f"Worker started. perform in worker. total_iterations: {total_iterations}")
        for _ in range(total_iterations):
            # print(f"{_} iteration of {total_iterations}")
            while True:
                tasks = self.helper.get_tasks(
                    queue_name=self.queue_name,
                    count=self.tasks_per_iteration)
                if tasks:
                    break
                time.sleep(self.get_sleep_time(count_tasks=0))

            try:
                # print("before perform many")
                tasks_results = self.perform_many_tasks(tasks)
                # print(f"performed many")
            except Exception as ex:
                logging.error(f"An error has occured on "
                              f"Worker.perform.perform_many_tasks: {ex}")
                if self.return_task_to_queue_if_error:
                    self.return_tasks_with_error(tasks)
            else:
                # print(f"self.return_task_result: {self.return_task_result}")
                if self.return_task_result:
                    for task_id, task_data in tasks_results:
                        # print("before returning")
                        self.helper.return_task_result(
                            queue_name=self.queue_name,
                            task_id=task_id,
                            task_data=task_data)
            count_tasks = len(tasks) or len(tasks_results) or \
                self.tasks_per_iteration
            time.sleep(self.get_sleep_time(count_tasks=count_tasks))

    def get_tasks(self, timeout, max_count):
        tasks = []
        if isinstance(timeout, int) or isinstance(timeout, float):
            timeout = datetime.timedelta(seconds=timeout)
        end_time = None
        while True:
            count_tasks = self.tasks_per_iteration - len(tasks)
            tasks.extend(self.helper.get_tasks(
                queue_name=self.queue_name,
                count=count_tasks))
            if len(tasks) >= self.tasks_per_iteration:
                return tasks

            if tasks or not self.start_timer_after_first_task:
                if end_time is None:
                    end_time = datetime.datetime.utcnow() + timeout
                if datetime.datetime.utcnow() > end_time:
                    return tasks
            time.sleep(timeout.total_seconds() / 10)

    def perform(self, total_iterations):
        for _ in range(total_iterations):
            # print(f"{_} iteration of {total_iterations}")
            tasks = []
            while not tasks:
                tasks = self.get_tasks(
                    timeout=self.iteration_max_sleep_time,
                    max_count=self.tasks_per_iteration)

            try:
                # print("before perform many")
                tasks_results = self.perform_many_tasks(tasks)
                # print(f"performed many")
            except Exception as ex:
                logging.error(f"An error has occured on "
                              f"Worker.perform.perform_many_tasks: {ex}")
                if self.return_task_to_queue_if_error:
                    self.return_tasks_with_error(tasks)
            else:
                # print(f"self.return_task_result: {self.return_task_result}")
                if self.return_task_result:
                    for task_id, task_data in tasks_results:
                        # print("before returning")
                        self.helper.return_task_result(
                            queue_name=self.queue_name,
                            task_id=task_id,
                            task_data=task_data)
            time.sleep(self.after_iteration_sleep_time)
