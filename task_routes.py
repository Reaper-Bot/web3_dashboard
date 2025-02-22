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
    status = request.args.get('status')
    priority = request.args.get('priority')
    sort_by = request.args.get('sort_by', 'created_at')  # Default sorting by created_at
    order = request.args.get('order', 'desc')

    query = Task.query

    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)

    if order == 'desc':
        query = query.order_by(getattr(Task, sort_by).desc())
    else:
        query = query.order_by(getattr(Task, sort_by))

    tasks = query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status, "priority": t.priority} for t in tasks])
