import os

NGINX = os.environ["NGINX_ROOT"]
STUDENTS_PROJECTS = os.environ["STUDENTS_PROJECTS_ROOT"]
STUDENTS_PROJECTS_DEPLOY = os.environ["STUDENTS_PROJECTS_DEPLOY_ROOT"]

def delete_workspace(context,static):
    delete_folder = os.system("sudo rm -r {}{}".format(STUDENTS_PROJECTS_DEPLOY,context))
    delete_folder_static = os.system("sudo rm -r {}{}".format(STUDENTS_PROJECTS,context))
    stop_container = os.system("docker stop {}".format(context))
    delete_container = os.system("docker rm -f {}".format(context))
    delete_image = os.system("docker rmi {}".format(context))
    delete_proxy_reverse(context)
    delete_static(context,static)


def delete_proxy_reverse(context):
    original = open(NGINX,'r')
    lines = original.readlines()
    original.close()
    
    new_file = open(NGINX,'w') 
    lines_to_delete = 8
    find = False
    for line in lines:
        if "location /{} {{".format(context) in line:
            find = True
            
        if not find:
                new_file.write(line)
        else:
            lines_to_delete = lines_to_delete - 1
            find = lines_to_delete != 0

    new_file.close()

def delete_static(context,static):
    original = open(NGINX,'r')
    lines = original.readlines()
    original.close()
    
    new_file = open(NGINX,'w') 
    lines_to_delete = 3
    find = False
    for line in lines:
        if "location /{}/{}/{{".format(context,static) in line:
            find = True
        if not find:
                new_file.write(line)
        else:
            lines_to_delete = lines_to_delete - 1
            find = lines_to_delete != 0
    new_file.close()


'''
context = input("insert context : ")
static_path = input(" Insert the static path : ")
delete_workspace(context,static_path.split("/")[-1])
'''