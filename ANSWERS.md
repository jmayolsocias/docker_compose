1. How long did it take to finish the test?
4 hours

2. If you had more time, how could you improve your solution?
- An info message could be returned when a request is sent to the root directory
- Security could be improve by using HTTPS for the communication between the reverse-proxy and the web application (although it could impact on performance).
- Nginx behaviour could be more efficient by enabling caching, compression, configuring keepalive, fine tunning worker_processes and worker_connections
- Fine tunning the maximum number of file descriptors in alpine image for both running services

3. What changes would you do to your solution to be deployed in a production environment?
- Run the solution in a public cloud provider
- Use a certificate signed by a CA
- Create a public DNS entry (i.e. www.hello_world.com)
- Enable autoscaling to adapt the infrastructure to the service load, maximizing availability and minimizing costs
- Enable caching
- Export logs
- Implement a CI/CD pipeline to automate testing and deployment for possible changes.


4. Why did you choose this language over others?
- It is open source
- It is easy to learn and use
- Simple syntax
- Improved productivity using modules.

5. What was the most challenging part and why?
Setting up the HTTPS service was the most challenging part because I experienced some conflicts in the nginx configuration.