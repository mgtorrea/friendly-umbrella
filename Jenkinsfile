pipeline {
  agent {
    kubernetes {
	yamlFile 'JenkinsPod.yaml'
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


