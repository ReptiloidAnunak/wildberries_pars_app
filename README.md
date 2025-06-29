<h1>Widberry parser</h1>

Selenium parsers. Auto-browser that collects orders from https://funpay.com and https://www.g2g.com/ and send it to web-server.
User input is required to solve the captcha. After login is autonom.
<br><br>

<h2>Run app</h2>
Run in the terminal follow commands:

```bash
./run_menu.sh
```


<h2>Logs</h2>

Logs directory: `/logs`

<h4>Run logs in Grafana</h4>

```bash
cd monitoring && docker-compose up -d
```

See your parsers logs there on Dashboard:<br>
http://localhost:3000

Your initial login data:<br>

Login:`admin`<br>
Password: `admin`<br>

Open dashboards menu:
http://localhost:3000/dashboard/new?orgId=1

After your registragion and login your should set your dashboard with logs.

Add Loki to Data sources (http://localhost:3000/connections/datasources)

Add `http://loki:3100` to the Connection URL field:


![alt text](doc/image.png)

Save this changes.

Click to Explore:

![alt text](doc/image-1.png)


Enter the job request: `{job="python_project_logs"}`

![alt text](doc/image-2.png)


Click "Add to dashboard" and save it.

![alt text](doc/image-3.png)

Ready!

