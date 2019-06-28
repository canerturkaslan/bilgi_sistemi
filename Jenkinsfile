@Library('sky-jenkins-utils') _

pipeline {

  agent any

  options { skipDefaultCheckout() }

  environment {
    PACKAGE_TYPE = 'Project'
    APP_URL = '//'
  }

  stages {


    stage('Test') {
        when {
            expression { should.test(env.BRANCH_NAME, env.PACKAGE_TYPE) == true }
        }
         steps{
            drmTestAndAnalysis()
         }
    }


  }

  post {
    success {

    }
    failure {

    }
  }
}
