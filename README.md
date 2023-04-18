# Docker Misconfig Scanner

Docker Misconfig Scanner is a tool that find unauthenticated Docker registry API for misconfigurations, downloads blobs for a specified repository and tag, and stores them in a directory. The script prompts the user for the API endpoint URL, target repository, target tag, and output directory.

## Installation

To install Docker Misconfig Scanner, clone the repository and run `setup.py`:

```bash
git clone https://github.com/dhina016/docker-misconfig-scanner.git
cd docker-misconfig-scanner
python setup.py install
```

```
usage: dockerscanner -u URL

optional arguments:
  -u URL, --url URL  Specify the Docker API URL (e.g. https://IP:Port)
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
Docker Misconfiguration Scanner is released under the MIT License.
