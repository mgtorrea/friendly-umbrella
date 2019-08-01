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
		sh 'pip install pytest'
	        sh 'pytest --verbose --junit-xml test-reports/results.xml sources/test_calculations.py'
	}
      }
      post {
        always {
            junit 'test-reports/results.xml' 
        }
      }
    }
  }
}
