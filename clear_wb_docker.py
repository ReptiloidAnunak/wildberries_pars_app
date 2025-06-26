from docker import DockerClient



def kill_project_containers():
    docker_client = DockerClient()
    for cont in docker_client.containers.list():
        if cont.name.startswith('wb_'):
            print(cont.name)
            cont.remove(force=True)


    for img in docker_client.images.list():
        for tag in img.tags:
            if 'wildberries' in tag:
                docker_client.images.remove(image=img.id, force=True)



if __name__ == '__main__':
    kill_project_containers()