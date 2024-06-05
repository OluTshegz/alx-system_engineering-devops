
# 0x18. Webstack monitoring

DevOps, SysAdmin, monitoring

### Concepts

_For this project, we expect you to look at these concepts:_

--   [Monitoring](https://intranet.alxswe.com/concepts/13)
# Monitoring

Just as the heart monitor in a hospital that is making sure that a patient’s heart is beating and at the right beat, software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

`You cannot fix or improve what you cannot measure`  is a famous saying in the tech industry. In the age of the data-ism, monitoring how our software systems are doing is an important thing.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

## Here are few famous monitoring tools:

### NewRelic

NewRelic requires you to add a piece of JavaScript to your website, this agent will collect information and send it back to the New Relic servers. It will give you a detailed analysis of how quickly your website loads in a browser, with a detailed analysis at every level of the stack. If the website is loading too slowly or users are experiencing error (500), there is a feature that allows you to trigger an alert. NewRelic now does much more than this, I’ll let you discover the rest.

### DataDog

DataDog allows you to measure and monitor everything with graphs. It gathers performance data from all your application components. The service has a lot of integrations. You usually just need to properly configure your alert and you are good to go with solid monitoring coverage.

### Uptime Robot

Uptime Robot is a simple service that will check that your website is responding from multiple locations in the world. This is the bare minimum when you host a website.

### Nagios

Nagios is an open source project started in 1999, it is among the most widely used monitoring tools in the tech industry. It is, however, seen as outdated. Nagios had trouble adapting to the rise of the Cloud but is slowly trying to catch up.

### WaveFront

Wavefront is a cutting edge monitoring service funded by great software engineers who’ve built monitoring tools for the best tech companies in Silicon Valley. The idea is to be able to analyze anything that can produce data points. A query language that looks like SQL allows users to apply mathematical operations to these data points to extract values or detect anomalies from the time series data. While it takes some time to get used to the tool, it’s the type of monitoring that the best companies are using. To my knowledge, LinkedIn, Facebook and DropBox are using a very similar tool for their monitoring needs.

--   [Server](https://intranet.alxswe.com/concepts/67)
# Server

Servers are located in datacenters which are buildings that host hundreds, or even thousands of computers (servers). You can think of a server as a computer without a keyboard, mouse, or screen, that is accessible only by a network. A server can be physical or virtual. A server runs an OS (operating system).

Read:

-   [What is a server](https://en.wikipedia.org/wiki/Server_(computing) "What is a server")

Watch:

-   [What is a server](https://www.youtube.com/watch?v=B1ANfsDyjeA "What is a server")
-   [Where are servers hosted (data centers)](https://www.youtube.com/watch?t=33&v=iuqXFC_qIvA&feature=youtu.be "Where are servers hosted (data centers)")

Do not mix up  **server**  and  **web server**. (Check out the  **web server**  concept page to know more about this.)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

## Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)

## Resources

**Read or watch**:

-   [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/ "What is server monitoring")
-   [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management "What is application monitoring")
-   [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/ "System monitoring by Google")
-   [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/ "Nginx logging and monitoring")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.alxswe.com/rltoken/Bd9r8twsVT3S_8j7-kOLrg "explain to anyone"),  **without the help of Google**:

### General

-   Why is monitoring needed
-   What are the 2 main area of monitoring
-   What are access logs for a web server (such as Nginx)
-   What are error logs for a web server (such as Nginx)

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass  `Shellcheck`  (version  `0.3.7`) without any error
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing


## Your servers

  

Name: 530478-web-01

Username: `ubuntu`

IP: `52.91.126.218`

State: running

Actions Toggle Dropdown

  

Name: 530478-web-02

Username: `ubuntu`

IP: `54.89.178.237`

State: running

Actions Toggle Dropdown

  

Name: 530478-lb-01

Username: `ubuntu`

IP: `54.175.101.81`

State: running

Actions Toggle Dropdown

  

## Tasks

### 0. Sign up for Datadog and install datadog-agent

mandatory

For this task head to  [https://www.datadoghq.com/](https://www.datadoghq.com/ "https://www.datadoghq.com/")  and sign up for a free  `Datadog`  account. When signing up, you’ll have the option of selecting statistics from your current stack that  `Datadog`  can monitor for you. Once you have an account set up, follow the instructions given on the website to install the  `Datadog`  agent.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T125241Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=72c7bf36d82da08e4cfebd56dcdacf3cafb3ffd102e6f311f42ea9d81e5bc9ec)

-   Sign up for Datadog -  **Please make sure you are using the US website of Datagog (https://app.datadoghq.com)**
-   Use the  **US1**  region
-   Install  `datadog-agent`  on  `web-01`
-   Create an  `application key`
-   Copy-paste in your Intranet user profile ([here](https://intranet.alxswe.com/users/my_profile "here")) your DataDog  `API key`  and your DataDog  `application key`.
-   Your server  `web-01`  should be visible in Datadog under the host name  `XX-web-01`
    -   You can validate it by using this  [API](https://docs.datadoghq.com/api/latest/hosts/ "API")
    -   If needed, you will need to update the hostname of your server

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x18-webstack_monitoring`

Done?  Check your code  Get a sandbox

### 1. Monitor some metrics

mandatory

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some  `monitors`  within the  `Datadog`  dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here:  [System Check](https://docs.datadoghq.com/integrations/system/ "System Check").

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T125241Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f26261140c227cb568ccf619961c0b51195ff82c96e41d9f3c242537a0ff7188)

-   Set up a monitor that checks the number of read requests issued to the device per second.
-   Set up a monitor that checks the number of write requests issued to the device per second.

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x18-webstack_monitoring`

Done?  Check your code  Get a sandbox

### 2. Create a dashboard

mandatory

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

-   Create a new  `dashboard`
-   Add at least 4  `widgets`  to your dashboard. They can be of any type and monitor whatever you’d like
-   Create the answer file  `2-setup_datadog`  which has the  `dashboard_id`  on the first line.  **Note**: in order to get the id of your dashboard, you may need to use  [Datadog’s API](https://docs.datadoghq.com/api/latest/ "Datadog's API")

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x18-webstack_monitoring`
-   File:  `2-setup_datadog`

Done?  Check your code  Get a sandbox
