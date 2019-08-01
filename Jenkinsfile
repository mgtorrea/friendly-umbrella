pipeline {
  agent {
    kubernetes {
	containerTemplate {
		name 'python'
		image 'python:3.7.2'
		ttyEnabled true
		command 'cat'
        }
    }

  }
  stages {
    stage('build') {
      steps {
	container('python'){
        	sh 'pip install -r requirements.txt'
	}
      }
    }
    stage('test') {
      steps {
	container('python'){
		sh 'pip install -r requirements-test.txt'
	        sh 'pytest'
	}
      }
    }
  }
}
