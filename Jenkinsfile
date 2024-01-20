pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                git(
                   url: 'https://github.com/quangan186/COSC2767-RMIT-Store',
                   branch: 'main',
                )
            }
        }
        stage('Deploy'){
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: 'ansible-server', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'ansible-playbook /home/ansibleadmin/deployApache.yml', execTimeout: 300000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                build propagate: false, job: 'TestingJob'
            }
            
        }
    }
}