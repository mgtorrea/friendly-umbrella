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
        	//sh 'pip install -r requirements.txt'
		sh 'pip install awscli'
	}
	container('docker-cli'){
		sh 'aws sts get-caller-identity'
		sh '$(aws ecr get-login --no-include-email --region us-east-2)'
        	sh 'docker build . -t 982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella'
		sh 'docker push 982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella'
	}
      }
    }
  }
}
