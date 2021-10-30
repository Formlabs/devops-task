pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'build'
		sh "docker build -t devops-task ."
            }
        }
	stage('test') {
            steps {
                echo 'test'
            }
        }
	stage('deploy') {
	    steps {
		echo 'deploy'
		sh """
                   kubectl delete services devops-task
		   kubectl delete deployment devops-task
		   minikube stop
		   minikube start
		   eval \$(minikube docker-env)
		   kubectl create deployment devops-task --image=devops-task
		   kubectl expose deployment devops-task --type=NodePort --port=8081
		   minikube service --url devops-task
		"""
            }
        }
    }
}
