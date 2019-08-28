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
	container('docker-cli'){
        	sh 'docker build . -t 982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella'
		sh 'docker push 982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella'
	}
      }
    }
  }
}
