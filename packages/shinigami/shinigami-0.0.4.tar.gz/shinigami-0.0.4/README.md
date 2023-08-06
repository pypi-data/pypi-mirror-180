# Shinigami

Shinigami is an open source Python module allowing the user to generate and build a Dockerfile during runtime.

## Usage
Shinigami was created to be simplistic and maintainable. This means we've created a simple class called `Shinigami`, which can be called anywhere in your application. From here, you can call the `generate_dockerfile()` function. This allows the flexibility to only require a single call in your application, but multiple file generations.

### Quick Example
```python
from shinigami.shinigami import Shinigami

def create_file():
    Shinigami(lang_os="python", version="3.9", build=True).generate_dockerfile()

if __name__ == '__main__':
    create_file()
```

There are currently 3 seperate parameters you can choose from:

- `lang_os` (`str`)   - The language or operating system you should like to pull from Docker Hub (Example: `ubuntu`)
- `version` (`str`)   - The version of the language or operating system (Example: `22.04`)
- `build`   (`bool`)  - This allows you to choose if you would like to build the Docker container or just pull the Dockerfile without building