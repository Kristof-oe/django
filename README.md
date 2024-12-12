install minikube 
minikube start --driver=docker or minikube start --driver=virtualbox or minikube start --driver=hyperv, then use one terminal for minikube dashboard, ui for watching clusters, 
Ther is deployment service, voluem and job, deployment running container, service is responsible for port communication and visibility, volume is storage, and job is one time running job maker
There will be app secret, base 64 coding passwords, app variable for configmap, this contains values will be used by deployments and job
React.yaml is not fully made yet, and there is an nginx.yaml, this is for IPs communicate with each other through specific DNS: these 2 unnecessary now 
