inventory_path = './ansible/inventory.yml'

playbook_init_user_path = './ansible/playbook_init_remote_user.yml'
playbook_set_environment_path = './ansible/playbook_set_environment.yml'
playbook_deploy_frontend_path = './ansible/playbook_deploy_frontend.yml'


prepare_ansible:
	# python3 -m pip install --user ansible
	ansible-galaxy install -r ansible/requirements.yml

create_remote_user:
	ansible-playbook -i $(inventory_path) $(playbook_init_user_path) --ask-become-pass

set_environment:
	ansible-playbook -i $(inventory_path) $(playbook_set_environment_path) --ask-become-pass

deploy_frontend:
	ansible-playbook -i $(inventory_path) $(playbook_deploy_frontend_path) --ask-become-pass