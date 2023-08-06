#!/usr/bin python3
import os, socket, json
from typing import List, Dict, Tuple
from .workspace import delete_workspace
from .nginx_automatization import  configure_nginx

root = os.getcwd()
NGINX = os.environ["NGINX_ROOT"]
STUDENTS_PROJECTS = os.environ["STUDENTS_PROJECTS_ROOT"]
STUDENTS_PROJECTS_DEPLOY = os.environ["STUDENTS_PROJECTS_DEPLOY_ROOT"]
LOG_CONTAINER=os.environ["LOGS_CONTAINER"]
LOG_IMAGE=os.environ["LOGS_BUILD"]
logs = ""

def download_project_from_github(url: str, context: str)-> Tuple[bool, str]:
	''' 
	This method gonna  download  the project code  and set into  a folder student 
	'''
	cwd = os.getcwd()
	os.chdir(STUDENTS_PROJECTS_DEPLOY)
	is_download = os.system("sudo git clone {} {} ".format(url,context)) == 0
	commit = ""
	if is_download:
		path_project = os.path.join(STUDENTS_PROJECTS_DEPLOY, context)
		os.chdir(path_project)
		os.system("sudo git log --pretty=format:'%h' -n 1 > commit")
		path_commit = "{}/commit".format(path_project)

		with open(path_commit, "r") as file:
			commit = file.readlines()[0]

		os.system(path_commit)
	os.chdir(STUDENTS_PROJECTS_DEPLOY)

	return (is_download, commit)


def move_statics(static_path:str,context):
	'''
	The static path where you gonna find the js,css 
	'''
	create_folder = os.system("sudo mkdir {}{}".format(STUDENTS_PROJECTS,context))
	copy = os.system("sudo cp -r {}{}/{} {}{}".format(STUDENTS_PROJECTS_DEPLOY,context,static_path,STUDENTS_PROJECTS,context))

	return copy

def create_image(context)->int:
	'''
	The context name of the project
	'''
	create = os.system('sudo bash -c "docker build  -t {} ./{} &> {}/{}"'.format(context,context,context,LOG_IMAGE))

	return create

def delete_env_file():
	os.system("sudo rm .env")

def create_container(context:str,port_container:str)->int:
	'''
	The context name of the project and the port where the service is expose
	'''
	global free_port
	free_port = str(get_free_port())
	create = os.system('sudo bash -c "docker run  -d -p {}:{} --name {} --env-file {}/env {} &> {}/{}" '.format(free_port,port_container,context,context,context,context,LOG_CONTAINER))
	
	return create

def update_logs(context):
	os.chdir(STUDENTS_PROJECTS_DEPLOY)
	os.system('sudo bash -c "docker logs {} &> {}/{}"'.format(context,context,LOG_CONTAINER))

def get_free_port()-> int:
	sock = socket.socket()
	sock.bind(('', 0))
	return sock.getsockname()[1]

def restart_nginx():
	os.system("sudo systemctl restart nginx.service")

def get_logs(context, file,type)->str:
	if type == 2 :
		os.system('sudo bash -c "docker logs {} >& {}/{}"'.format(context,context,LOG_CONTAINER))
	log = ""
	with open("{}/{}".format(context,file),"r") as image:
		lines = image.readlines()
		log += "\n"
		for line in lines :
			log += line

	return log

def load_env_vars(context,env_var):

	create_env_file = os.system("sudo touch {}/env".format(context))
	file = open("{}/env".format(context),"w")

	for key,value in env_var.items():
		file.write('{}="{}" \n'.format(key,value))
	file.close()

def container_is_dead(context):
	os.chdir(STUDENTS_PROJECTS_DEPLOY)
	os.system('sudo bash -c  "sudo docker inspect {} | grep Running > {}/running_log"'.format(context,context))
	file = open("{}/running_log".format(context),"r")
	line = file.readlines()
	
	return "false" in line[0]

def deploy(url, context, port_container, static_path, env_var, delegate)-> None:
	is_download, commit = download_project_from_github(url,context)
	if is_download:
		delegate({
			'message': "Download successful.", 
			'error': '', 
			'stage': 1,
			'data': {'commit': commit},
			'progress': 20
		})
		load_env_vars(context,env_var)	
		if create_image(context) == 0 :
			delegate({
				'message': "Image created succesful.", 
				'error': '', 
				'stage': 2,
				'progress': 40}
			)
			
			if create_container(context,port_container) == 0 and not container_is_dead(context):
				delegate({
					'message': "Container created succesful.", 
					'error': '', 
					'stage': 3,
					'progress': 60}
				)
				if move_statics(static_path,context) == 0:
					delegate({
						'message': "Statics loaded succesful.", 
						'error': '', 
						'stage': 4,
						'progress': 80}
					)
					configure_nginx(free_port,context,static_path.split("/")[-1])
					restart_nginx()
					delegate({
						'message': "Available service.", 
						'error': '', 
						'stage': 5,
						'progress': 100}
					)
				else :
					delegate({
						'message': '', 
						'stage': 4,
						'error': "Failed to load the statics.", 
						'progress': 0}
					)
			else :
				delegate({
					'message': '', 
					'stage': 3,
					'error': "Failed to create container. Please check logs.", 
					'progress': 0}
				)
		else :
			delegate({
				'message': '', 
				'stage': 2,	
				'error': "Failed to create image. Please check logs.", 
				'progress': 0}
				)
	else :
		delegate({
			'message': '',
			'stage': 1,
			'error': "Failed to download the project. Please check your repository.", 
			'progress': 0}
		)

def get_statistics() -> List[Dict]:
	find = os.system('docker stats --no-stream --format "{{json . }}" > statistics')
	if find == 0:
		lines = []
		with open("statistics", "r") as statistics:
			lines = statistics.readlines()
		
		res: List[Dict] = []
		if len(lines) > 0:
			for line in lines:
				res.append(json.loads(line))
		return res

'''
url = input("Please enter your url github : ")
context = input("Please your context app name: ")
port_container = input("please enter the container port: ")
static_path = input("Please insert the static path (dont finish and start with /):")
vars = {"django-key":"django-insecure-w_nf2*3!@c3gc=owm&0gqnsid87yfc2(g2+#qc$yy#-@c7i12e"}
deploy(url,context,port_container,static_path,vars)

'''