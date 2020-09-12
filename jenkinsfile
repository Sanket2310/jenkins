pipeline {
  agent any
  stages {
    /*Stage for cleanup - removes the folders and cleans the workspace*/
    stage('cleanup')
    {
    steps {
    deleteDir()
    cleanWs()
    }
    }
    /*Stage for checking out SCM - clone the code from github repository*/
    stage('checkout scm'){
    steps{
    sh 'ls -a'
    checkout([$class: 'GitSCM',
    branches: [[name: '*/master']],
    doGenerateSubmoduleConfigurations: false,
    extensions: [],
    submoduleCfg: [],
    userRemoteConfigs: [[credentialsId: 'my-git-creds', url: 'https://github.com/sanket2310/jenkins.git']]])
    }
    }
    /*Stage for creating virtual environment and installing the required packages*/
    stage('build') {
     steps {
        sh 'python3 -m virtualenv env'
        sh 'source env/bin/activate'
        sh 'pip3 install -r requirements.txt --user'
      }
    }
    /*Stage for testing - perform unit testing and find out pylint score*/
    stage('test') {
      steps {
        sh 'python3 linting.py'
        sh 'python3 test.py'
      }
    }
    /*Deploy the application*/
    stage('deploy'){
    steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "sudhanshu-jenkins",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "/bin/rm -rf app"),
                            sshTransfer(execCommand: "/bin/mkdir app"),
                            sshTransfer(sourceFiles: "*",),
                            sshTransfer(execCommand: "/bin/mkdir app/templates"),
                            sshTransfer(sourceFiles: "templates/*",),
                            sshTransfer(execCommand: "/bin/python3 -m virtualenv env"),
                            sshTransfer(execCommand: ". env/bin/activate"),
                            sshTransfer(execCommand: "/bin/pip3 install -r app/requirements.txt --user"),
                            sshTransfer(execCommand: "/bin/python3 app/app.py &")


                        ]
                    )
                ]
            )
        }
    }
  }
}
