import os, requests

class Shinigami():
    def __init__(self, lang_os="", version="", build=False):
        self.lang_os = lang_os
        self.version = version
        self.build = build

    def generate_dockerfile(self):
        try:

            # Queries open source Dockerfile repository
            docker_data = requests.get(f"https://raw.githubusercontent.com/stience/StoreDock/main/Docker/{self.lang_os}/{self.version}/Dockerfile")

            # Checks the status code for the repository connection
            if docker_data.status_code == 200:
                with open("Dockerfile", "w") as f:
                    f.write(docker_data.text)

            # Allows the user to build the Docker container during runtime (+ Dockerfile generation)
            if docker_data.status_code == 200 and self.build:
                with open("Dockerfile", "w") as f:
                    f.write(docker_data.text)

                # Builds the Docker container
                # NOTE: This requires Docker to be installed on the user's system and be configured in the PATH
                os.system(f"docker build . -t shinigami-{self.lang_os}{self.version}")

            # If the Dockerfile doesn't exist, we do a simple print statement and unclean exit
            if docker_data.status_code != 200:
                print("This Docker configuration is not currently supported")
                exit(1)
        
        except Exception as e:
            return e