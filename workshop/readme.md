# Building a custom docker image and deploying to artifactory
This repository contains all the necessary code for building a custom image on gitlab using the kaniko executor and deploying it to artifactory. The use of docker commands has been explicitly disabled for shared runners due to security concerns as root access is required for the same. More documentation is found at: https://devops.swisscom.com/docs/source-version-control-gitlab/cicd.html
In this exercise, we would like to build a simple python docker image and release the same to artifactory:
* Building and pushing the docker image to artifactory with a temporary tag is done using the Kaniko executor
* Kaniko is a tool to build container images from a Dockerfile, inside a container or Kubernetes cluster. Kaniko doesn't depend on a Docker daemon and executes each command within a Dockerfile completely in userspace. This enables building container images in environments that can't easily or securely run a Docker daemon.
* Cleanup or retagging of image in artifactory using crane-kaniko executor
* Crane-kaniko executor allows to perform separate docker operations (pull, push, retag etc) in contrast to binding operations all together as in kaniko only executor with the build command.

# Explanation of the project files
* *.gitlab-ci.yml*: The .gitlab-ci. yml file defines scripts that should be run during the CI/CD pipeline and their scheduling, additional configuration files and templates, dependencies, caches, commands. GitLab should run sequentially or in parallel and instructions on where the application should be deployed to.
* *Dockerfile*: The Dockerfile is essentially the build instructions to build the required image for your execution environment.
* *requirements.txt*: Defines all the dependencies (in our case couple of python dependencies) that would be needed to build the image using the Dockerfile.
* Tests
    * *input.xml*: sample xml file which is used as an input to perform units tests using the required python dependency.
    * unit_tests
        * *test_parse_xml.py*: unit test for parse_xml.py.
    * *parse_xml.py*: the parsing of the input.xml.
    * *scanning_results.sh*: using the container scanning result report to check level of vulnerabilities (uses jq).

# What is already defined
* CICD variables 
    * *CI_REGISTRY_PASSWORD*: The password of the service account sa-pf00-artifactory2 required to authenticate to artifactory
    * *DOCKER_AUTH_CONFIG*: defines the method of authentication to a private registry, in this case it uses basic auth with username: password

# Prerequisites for the hands-on exercise
* Options for setting up SSH connectivity (you can follow any one depending upon your case)

    * With existing BitBucket SSH public key
        Copy what you have as a SSH public key in bitbucket "Account Settings -> SSH Keys" as a new SSH key in Gitlab here https://code.swisscom.com/-/profile/keys"
    * Starting from scratch: On Linux environment
        1. Create a private/public key pair (note - gitlab only supports above 3072 and it is recommended to use a passphrase)
        ```
          ssh-keygen -t rsa -b 4096 -C "your comment" -f ~/.ssh/id_rsa.my-gitlab-key
        ```
          
        2. Configure the config file at ~/.ssh/id_rsa.my-gitlab-key to handle multiple ssh keys
        ``` 
            Host code.swisscom.com
                PreferredAuthentications publickey
                    IdentityFile ~/.ssh/id_rsa.my-gitlab-key
        ```
        3. Copy the contents of  ~/.ssh/id_rsa.my-gitlab-key.pub at https://code.swisscom.com/-/profile/keys

    * Starting from scratch: On Windows
        1. Install git for windows from: https://git-scm.com/download/win, follow the steps at: https://www.educative.io/answers/how-to-install-git-bash-in-windows
        2. Make sure you have the OpenSSH Client and OpenSSH Server installed. If not, then go to Settings → Apps → Optional features → Add a feature
        3. Install OpenSSH Client and OpenSSH Server
        4. Open the Services app on your local machine → double click OpenSSH Server → Select Startup type as Automatic → Start the service
        5. The above should auto populate config files under C.\ProgramData\ssh 
        6. Repeat steps 1 & 2 from the section 'On Linux environment' on your .ssh folder (usually at C:\Users\<your user>\.ssh) → make sure the path of the Identity file in Step 2 corresponds to the private key path on Windows
        7. If there was no auto creation ssh_config file at C.\ProgramData\ssh, then create it manually (requires admin rights) and copy the content of the ssh_config as mentioned in 2 (change the Identity file path such that  it corresponds to your private key path).
        8. Repeat step 3 (Linux section)
* Debugging the ssh connectivity
    ```
      ssh -vvv git@code.swisscom.com
    ```
* Cloning the GitLab project
    ```
      git clone ssh://git@code.swisscom.com:2222/swisscom/sre-shs-support/sre-cop-event-hands-on/sre-gettogether-gitlab-hands-on.git
    ```

* Create your branch on the project as <your_location>/<your_user> - use the GitLab UI to create a branch for testing the given code directly!

# Step-by-step goal of the hands-on exercise with relation to project files
* What errors do you encounter with the given pipeline?
* The container scanning is done using the Security/Container-Scanning.gitlab-ci.yml. 
* Perform tests 
    * what does the container scanning results report say about image vulnerabilities?
    * Use an image with less vulnerabilities [Dockerfile], Image with less vulnerabilities: remote-docker.artifactory.swisscom.com/python:3.8-slim
* Cleaning image or retagging image on artifactory depending on scanning results using the crane-kaniko executor [.gitlab-ci.yml, artifactory repo: https://artifactory.swisscom.com/artifactory/sre-gettogether-docker-repo-docker-local]
    * Your final image on artifactory should be located at: sre-gettogether-docker-repo-docker-local/<your_location>/<your_user>





