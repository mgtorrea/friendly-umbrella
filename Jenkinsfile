podTemplate(
    name: 'test-pod',
    label: 'test-pod',
    containers: [
        containerTemplate(name: 'python', image: 'python:3.7.2')
    ],
    {
        //node = the pod label
        node('test-pod'){
            //container = the container label
            stage('Build'){
                container('python'){
                    steps {
			sh 'pip install -r requirements.txt'
		      }
                }
            }
            stage('Test'){
                container(‘python’){
                    steps {
			sh 'pytest'
		      }
                }
            }
        }
    })
