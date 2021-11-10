from methods.regular.regular_api import *
from shared.database.task.job.job import Job
from shared.database.user import User
from shared.database.task.task import Task
from shared.database.annotation.instance import Instance

@routes.route('/api/job/<job_id>/stat', methods=["GET"])
def job_stat(job_id):
    with sessionMaker.session_scope() as session:
        job = Task.stats(
            session,
            job_id,
        )
        return jsonify(job)

@routes.route('/api/job/<job_id>/user/<user_id>/stats', methods=["GET"])
def jon_user_stats(job_id, user_id):
    with sessionMaker.session_scope() as session:
        tasks = Task.stats(
            session,
            job_id,
            user_id
        )

        return jsonify(tasks)