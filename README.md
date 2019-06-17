# Locust Homepage

### Description
This is a super basic locust file that is containerized. I needed a container that hammered a homepage that I could deploy.

### Example
`docker run -it --rm -p8089:8089 test:latest /usr/local/bin/locust --host=http://mysite.com`
