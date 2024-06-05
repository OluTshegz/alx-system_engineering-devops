
# 0x17. Web stack debugging #3

DevOps, SysAdmin, Scripting, Debugging

### Concepts

_For this project, we expect you to look at these concepts:_

--   [Web Server](https://intranet.alxswe.com/concepts/17)
# Web Server

**Do not mix up web server and server.**

A web server is a software that delivers web pages. A server is an actual computer.

But you might hear people referring to a  **web server**  using the word  **server**. (Check out the  **server**  concept page to learn more about this.)

As mentioned above, a server is a physical machine, an actual computer, but in the Cloud era that could also be a virtual computer, generally called a VM ([Virtual Machine](https://en.wikipedia.org/wiki/Virtual_machine "Virtual Machine")) or  [container](https://www.cio.com/article/247005/what-are-containers-and-why-do-you-need-them.html "container").

### Readme:

-   [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server "Wikipedia page about web server")
-   [Web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server "Web server")
-   [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server "What is a Web Server?")

--   [Web stack debugging](https://intranet.alxswe.com/concepts/68)
# Web stack debugging

# Intro

Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b05652c0f486.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T121504Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e6adb5a2a7d90d2f91a1bff86c9de43151091b4ca455bf07eddec6448a27a64c)

# Non-exhaustive guide to debugging

## School specific

If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the  **Docker**  concept page for more info.

## Test and verify your assumptions

The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

-   Is the web server started? - You can check using the service manager, also double check by checking process list.
-   On what port should it listen? - Check your web server configuration
-   Is it actually listening on this port? -  `netstat -lpdn`  - run as  `root`  or  `sudo`  so that you can see the process for each listening port
-   It is listening on the correct server IP? -  `netstat`  is also your friend here
-   Is there a firewall enabled?
-   Have you looked at logs? - usually in  `/var/log`  and  `tail -f`  is your friend
-   Can I connect to the HTTP port from the location I am browsing from? -  `curl`  is your friend

There is a good chance that at this point you will already have found part of the issue.

## Get a quick overview of the machine state

[Youtube video First 5 Commands When I Connect on a Linux Server](https://intranet.alxswe.com/rltoken/qdIjs52RG3ym8Z6JnNZ6hQ "Youtube video First 5 Commands When I Connect on a Linux Server")

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with  [5 commands](https://intranet.alxswe.com/rltoken/C7hcMJxfvZqGpaNk3J2A9g "5 commands")  in a minute or less:

### `w`

-   shows server  [uptime](https://intranet.alxswe.com/rltoken/q2_-xo61t3A4L5F9KjUy5A "uptime")  which is the time during which the server has been continuously running
-   shows which users are connected to the server
-   load average will give you a good sense of the server health - (read more about load  [here](https://intranet.alxswe.com/rltoken/klMEJTuMU7fNeZuBoQrBBw "here")  and  [here](https://intranet.alxswe.com/rltoken/lSGxl2xK-4BOEO92l5GvvA "here"))

### `history`

-   shows which commands were previously run by the user you are currently connected to
-   you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
-   where you might want to start your debugging work

### `top`

-   shows what is currently running on this server
-   order results by CPU, memory utilization and catch the ones that are resource intensive

### `df`

-   shows disk utilization

### `netstat`

-   what port and IP your server is listening on
-   what processes are using sockets
-   try  `netstat -lpn`  on a Ubuntu machine

## Machine

Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

-   Does the server have free disk space? -  `df`
-   Is the server able to keep up with CPU load? -  `w`,  `top`,  `ps`
-   Does the server have available memory?  `free`
-   Are the server disk(s) able to keep up with read/write IO? -  `htop`

If the answer is  **no**  for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

-   free up resources (stop process(es) or reduce their resource consumption)
-   increase the machine resources (adding memory, CPU, disk space…)
-   distributing the resource usage to other machines

## Network issue

For the machine level, you want to ask yourself these questions:

-   Does the server have the expected network interfaces and IPs up and running?  `ifconfig`
-   Does the server listen on the sockets that it is supposed to?  `netstat`  (`netstat -lpd`  or  `netstat -lpn`)
-   Can you connect from the location you want to connect from, to the socket you want to connect to?  `telnet`  to the IP + PORT (`telnet 8.8.8.8 80`)
-   Does the server have the correct firewall rules?  `iptables`,  `ufw`:
    -   `iptables -L`
    -   `sudo ufw status`

## Process issue

If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

-   Is the software started?  `init`,  `init.d`:
    -   `service NAME_OF_THE_SERVICE status`
    -   `/etc/init.d/NAME_OF_THE_SERVICE status`
-   Is the software process running?  `pgrep`,  `ps`:
    -   `pgrep -lf NAME_OF_THE_PROCESS`
    -   `ps auxf`
-   Is there anything interesting in the logs? look for log files in  `/var/log/`  and  `tail -f`  is your friend

## Debugging is fun

Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bae58c9f066a9668001ef4b4c39778407439d2f9.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T121504Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20d47732a60100fdb8691b921f33a3559cb34022c46215f2cf95c058e0a67df4)

## Background Context

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It  [actually powers 26% of the web](https://managewp.com/blog/statistics-about-wordpress-usage "actually powers 26% of the web"), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements

### General

-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   Your Puppet manifests must pass  `puppet-lint`  version 2.1.1 without any errors
-   Your Puppet manifests must run without error
-   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
-   Your Puppet manifests files must end with the extension  `.pp`
-   Files will be checked with Puppet v3.4

## More Info

### Install  `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

```

## Tasks

### 0. Strace is your friend

mandatory

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/f5af5167e65bd3101f76.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T110244Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a5782a975f1181751412c2fab2bad0935934519c9f8d0e7fefb6bc4ec8c4ebd1)](https://youtu.be/uHEzt1QuASo)

Using  `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

-   `strace`  can attach to a current running process
-   You can use  [tmux](https://hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/ "tmux")  to run  [strace](https://strace.io/ "strace")  in one window and  `curl`  in another one

Requirements:

-   Your  `0-strace_is_your_friend.pp`  file must contain Puppet code
-   You can use whatever Puppet resource type you want for you fix

Example:

```
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#

```

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x17-web_stack_debugging_3`
-   File:  `0-strace_is_your_friend.pp`

Done?  Get a sandbox
