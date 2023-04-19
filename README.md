# Docker Scanner

Docker Scanner is a tool that find unauthenticated Docker registry API for misconfigurations, downloads blobs for a specified repository and tag, and stores them in a directory. The script prompts the user for the API endpoint URL, target repository, target tag, and output directory.

## Installation

To install Docker Misconfig Scanner, clone the repository and run `setup.py`:

```bash
git clone https://github.com/dhina016/dockerscanner.git
cd dockerscanner
python setup.py install
```

```
usage: dockerscanner -u URL

optional arguments:
  -u URL, --url URL  Specify the Docker API URL (e.g. https://IP:Port)
```

### Discovery
```
1. The easiest way to discover this service running is get it on the output of nmap. Anyway, note that as it's a HTTP based service it can be behind HTTP proxies and nmap won't detect it.

2. Some fingerprints:
- If you access / nothing is returned in the response
- If you access /v2/ then {} is returned
- If you access /v2/_catalog you may obtain:
	{"repositories":["alpine","ubuntu"]}
	{"errors":[{"code":"UNAUTHORIZED","message":"authentication required","detail":[{"Type":"registry","Class":"","Name":"catalog","Action":"*"}]}]}
- Do not forget scanning TCP port 5000 on which usually this service is deployed.
- Extract image from private docker registry using blobs and manifests and its digest SHA value.
Pulling image manifest - GET /v2/alpine/manifests/latest. Upon successful response you will get blobsum values in the response as follows:
{
   "name": <name>,
   "tag": <tag>,
   "fsLayers": [
      {
         "blobSum": SHA256:1d4c65f8151f9bcf5d44b3745570c1b8d75f768b7f543c1da20f87b4e5180eec
      },
      ...
    ]
   ],
   "history": <v1 images>,
   "signature": <JWS>
}

Get the SHA256 value including SHA256 and create another request.

Pulling a layer - GET /v2/alpine/blobs/SHA256:1d4c65f8151f9bcf5d44b3745570c1b8d75f768b7f543c1da20f87b4e5180eec
If you are using curl, then you can successfully download the tar file. For a single manifest, download all tar files using all the blobsum values in the single manifest.

Extract and find useful info/secrets/other private items.

=======
- If you can access GET /v2/<name>/tags/list then try bruteforcing <name> and see what all resources of docker registry you can access. Visit the https://docs.docker.com/registry/spec/api/ URL for more resources to list and bruteforce.

```

### Security Issues

1. Improper Authentication/Authorization Checks
- This Docker Registry API is accessible without authentication. 
- A properly secured registry should return 401 when the "/v2/" endpoint is hit without credentials. 
- The response should include a WWW-Authenticate challenge, providing guidance on how to authenticate, such as with basic auth or a token service.

2. Shodan Dorks 
- Docker Private Registries

> "Docker-Distribution-Api-Version: registry" "200 OK" -gitlab

> https://www.shodan.io/search?query=%22Docker-Distribution-Api-Version%3A+registry%22+%22200+OK%22+-gitlab

3. Some Interesting Attack Reads
- https://book.hacktricks.xyz/pentesting/5000-pentesting-docker-registry


### References

```
a. https://www.acunetix.com/vulnerabilities/web/docker-registry-api-is-accessible-without-authentication/
b. https://hackerone.com/reports/924487
c. https://blog.dixitaditya.com/exploiting-docker-registry/
d. https://notsosecure.com/anatomy-of-a-hack-docker-registry/
e. https://github.com/lothos612/shodan
f. https://docs.docker.com/registry/spec/api/
g. https://github.com/harsh-bothra/learn365/blob/main/days/day33.md
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
Docker Misconfiguration Scanner is released under the MIT License.
