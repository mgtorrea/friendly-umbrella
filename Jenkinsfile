pipeline {
  agent {
    kubernetes {
	    yamlFile 'JenkinsPod.yaml'
    }
  }
  
  stages { 
    stage('test'){
      steps{
        container('python'){
	  sh 'env'
          sh 'pip install -r requirements.txt'
          sh 'pip install -r requirements-test.txt'
          sh 'pytest'
        }
      }
     }
    stage('build') {
      steps {
        container('docker-cli'){
          sh 'docker build . -t "982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella:build_${env.BUILD_ID}"'
        }
        container('aws-cli'){
          sh 'aws sts get-caller-identity'
          sh '$(aws ecr get-login --no-include-email --region us-east-2)'
          sh 'docker push "982989130295.dkr.ecr.us-east-2.amazonaws.com/test/friendly-umbrella:build_${env.BUILD_ID}"'
        }
      }
    }
    stage('deploy'){
      steps{
        container('kubectl'){
          sh 'cat deploy-test-pod.yaml | sed "s/{{VERSION}}/$build_${env.BUILD_ID}/g" | kubectl apply -f -'
          //sh 'kubectl apply -f deploy-test-pod.yaml'
        }
      }
    }
  }
}
