from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Project, db

project_bp = Blueprint('project', __name__)

@project_bp.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    data = request.json
    project = Project(name=data['name'], description=data.get('description'), network=data['network'], rpc_url=data['rpc_url'])
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created"}), 201

@project_bp.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "name": p.name, "network": p.network} for p in projects])
