pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'python -m pip install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
       
        stage('TestCase'){
            steps{
                bat 'python test.py'
                echo 'Test Done'
                
            }
           
        }
                stage('Run'){
                     steps{
                        bat 'python main.py'
                        echo 'Success'
            }
                }

    }
}
