pipeline {
  agent {
    kubernetes {
	podTemplate {
		podRetention: "always()"
		nodeSelector:	'"kops.k8s.io/instancegroup": nodes'
		containers:[
				containerTemplate {
					name 'python'
					image 'python:3.7.2'
					ttyEnabled true
					command 'cat'
				}
		]
		annotations: [podAnnotation(key: "iam.amazonaws.com/role", value: "arn:aws:iam::982989130295:role/podcillo-x.services.datanktzingo.datank.ai")]
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
