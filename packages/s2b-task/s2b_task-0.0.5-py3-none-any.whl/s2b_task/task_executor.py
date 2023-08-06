import os
import sys
import argparse as ap
from .action import GetTaskListAction
from .exc import TaskAlreadyExists, TaskNotExists
from .storage import TASK_MAP


arg_parser = ap.ArgumentParser(description="Parser description")
arg_parser.add_argument("task_name", help="Name of task to execute")
arg_parser.add_argument(
    "-l",
    "--ls",
    action=GetTaskListAction,
    help="List all registered tasks",
)


def task(callback):
    if TASK_MAP.get(callback.__name__):
        raise TaskAlreadyExists

    TASK_MAP[callback.__name__] = callback


def execute_task(task_name: str, *argc, **argv):
    task_callback = TASK_MAP.get(task_name)
    if not task_callback:
        raise TaskNotExists

    task_callback()


def parse_task():
    namespace: ap.Namespace = arg_parser.parse_args()
    print(namespace)
    # execute_task(opt.action.task_name)


def do_task():
    # append current directory into path to get tasks directory
    sys.path.append(os.getcwd())
    try:
        import tasks as t
    except ModuleNotFoundError:
        print("No tasks directory")
        return

    parse_task()
