pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'build'
		docker build -t devops-task .
            }
        }
	stage('test') {
            steps {
                echo 'test'
            }
        }
	stage('deploy') {
            when {
                branch 'master'
            }
	    steps {
                echo 'deploy'
            }
        }
    }
}
