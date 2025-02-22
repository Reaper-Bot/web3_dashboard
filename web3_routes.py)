@task_bp.route('/contract/balance', methods=['GET'])
@jwt_required()
def check_balance():
    project_id = request.args.get('project_id')
    contract_address = request.args.get('contract_address')

    balance = get_contract_balance(project_id, contract_address)
    if balance is None:
        return jsonify({"error": "Invalid project"}), 400

    return jsonify({"contract_address": contract_address, "balance": balance})
