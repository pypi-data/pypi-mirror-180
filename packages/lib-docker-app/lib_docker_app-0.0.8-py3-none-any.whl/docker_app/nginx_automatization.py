import os

NGINX = os.environ["NGINX_ROOT"]
STUDENTS_SERVER_IP = os.environ["STUDENTS_SERVER"]
STUDENTS_PROJECTS = os.environ["STUDENTS_PROJECTS_ROOT"]

def configure_nginx(container_port,context,folder_static):
	'''
	folder_satic example : assets
	'''
	original = open(NGINX,'r')
	lines = original.readlines()
	original.close()

	del lines[len(lines)-1]

	new_file = open(NGINX,'w') 
	for line in lines:
		new_file.write(line)

	new_file.write('\n \tlocation /{}/{}/{{\n  \troot {};\n  \t}}\n \n'.format(context,folder_static,STUDENTS_PROJECTS))
	new_file.write('\tlocation /{} {{\n \t\t\n'.format(context))
	new_file.write('\t\tproxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n')
	new_file.write('\t\tproxy_set_header X-Forwarded-Proto $scheme;\n')
	new_file.write('\t\tproxy_set_header X-Real-IP $remote_addr;\n')
	new_file.write('\t\tproxy_set_header Host $http_host;\n')
	new_file.write('\t\tproxy_pass http://{}:{}/{};\n'.format(STUDENTS_SERVER_IP,container_port,context))
	new_file.write('\t}\n')
	new_file.write('}\n')
	new_file.close()

