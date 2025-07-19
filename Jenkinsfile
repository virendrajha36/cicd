pipeline {
  agent any
  
  stages {
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("weather-app", "-f Dockerfile .")
        }
      }
    }
    
    stage('Run Docker Container') {
      steps {
          sh 'docker run -d -p 5000:5000 weather-app'
      }
    }
  }
  
  post {
    always {
      sh 'echo "Running on port 5000" '
    }
  }
}

