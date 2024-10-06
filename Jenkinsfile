pipeline:
  agent:
    docker:
      image: 'python:3.9'

  stages:
    - stage: 'Prepare'
      steps:
        - checkout:
            scm:
              - git:
                  url: 'https://github.com/your-repo/your-project.git'
                  branch: 'main'
        - sh: 'pip install pyodbc'

    - stage: 'Run Sybase Query'
      steps:
        - withCredentials:
            - usernamePassword:
                credentialsId: 'sybase-credential-3'
                usernameVariable: 'SYBASE_USERNAME'
                passwordVariable: 'SYBASE_PASSWORD'
        - sh: 'python sybase_query.py'

    - stage: 'Cleanup'
      steps:
        - sh: 'echo "Performing cleanup tasks..."'