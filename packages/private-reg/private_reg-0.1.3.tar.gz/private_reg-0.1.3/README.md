# Private Registry


This is a simple python program to manage containers to upload, download and delete in private container regitry



To Install `private reg` use

````
pip install private_reg
````

To use in your py program:

````
from private_reg import container_registry
````

create an object with class `Private_registry` in `container_registry` 
example:
````
x = container_registry.Private_registry()
````






list of functions in container_registry.Private_registry

`is_container_running()` return status true or false whether a container is running with given name or not

`check_repo_in_pvt_reg()` prints the repos in private registry

`setup_pvt_registry()` starts private registry with a given conatiner name as class object

`pull_image()` Pulls image from docker hub if --no-private-reg or pulls image from private-container-registry by default

`push_image()` Push image to private_container_registry 

`delete_image()` Deletes image from private_containe_registry by default 

