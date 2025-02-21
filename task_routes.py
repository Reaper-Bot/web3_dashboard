from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Task, db

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.json
    task = Task(title=data['title'], project_id=data['project_id'])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])
