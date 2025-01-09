inventory_path = './ansible/inventory.yml'

playbook_init_user_path = './ansible/playbook_init_remote_user.yml'
playbook_set_environment_path = './ansible/playbook_set_environment.yml'
playbook_deploy_frontend_path = './ansible/playbook_deploy_frontend.yml'
playbook_deploy_backend_path = './ansible/playbook_deploy_backend.yml'


######################################
ssh:
	ssh -l admin 158.160.132.225
######################################
prepare_ansible_locally:
	# python3 -m pip install --user ansible
	ansible-galaxy install -r ansible/requirements.yml

vagrant_set_environment:
	ansible-playbook -i $(inventory_path) $(playbook_set_environment_path) --extra-vars hosts=vagrant

vagrant_deploy_frontend:
	ansible-playbook -i $(inventory_path) $(playbook_deploy_frontend_path) --extra-vars hosts=vagrant

vagrant_deploy_backend:
	ansible-playbook -i $(inventory_path) $(playbook_deploy_backend_path) --extra-vars hosts=vagrant


######################################
set_environment:
	ansible-playbook -i $(inventory_path) $(playbook_set_environment_path) --extra-vars hosts=remote-staging-admin

deploy_frontend:
	ansible-playbook -i $(inventory_path) $(playbook_deploy_frontend_path) --extra-vars hosts=remote-staging-admin

deploy_backend:
	ansible-playbook -i $(inventory_path) $(playbook_deploy_backend_path) --extra-vars hosts=remote-staging-admin

######################################
