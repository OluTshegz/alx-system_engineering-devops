
# 0x19. Postmortem

DevOps, SysAdmin

### Concepts

_For this project, we expect you to look at this concept:_

-   [On-call](https://intranet.alxswe.com/concepts/39)
# On-call

# Being on-call

> (of a person) able to be contacted in order to provide a professional service if necessary, but not formally on duty.
> 
> “our technicians are on call around the clock”
> 
> synonyms: on duty, on standby, available
> 
> “Dr. Merton is on call this evening”

-Google

Users and consumers expect their favorite websites and services to be constantly accessible. Have you ever seen Facebook, Amazon, LinkedIn, Ebay down? Probably not. Any downtime means users frustration and potentially millions of dollars in loss. That’s true for the big players but also for any company where its online presence is crucial, which is the case for a lot of businesses.

This does not happen magically. Software engineers are building reliable systems that are supposed to be up and running 100% of the time, but sometimes things go sideways and the issue needs to be fixed as soon as possible. To achieve quick resolution time, companies are putting in place monitoring systems to detect any anomaly and alert the employee who is on-call. This sometimes happens during working hours, but also at 3am or at night.

# Setup

To be on call you need at least 4 components:

-   A service or website you want to monitor
-   A monitoring tool
-   An oncall management system
-   A software engineer (that’s you)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/35d138aa05cb69a538bd539ce2304eda50f74215.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T181316Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6df593e215c0c289e1ab42152261fc1856c180a1ae0bf24a6867e15aaba460bd)

### A service or website you want to monitor

You can monitor thousands of things:

-   Is my website returning HTTP 200?
-   Is my website loading in less than 500ms?
-   Is my webserver daemon up?
-   Is there more than 50% free disk space on my server?
-   …

### A monitoring tool

You need to configure one or multiple monitoring tool(s) to your on-call system, they are the ones that will actually detect any anomaly and report it to the on-call platform. Check out the  **Monitoring**  concept page for recommandations.

### A on-call management system

A lot of home tools can be used for that, you can for example in Nagios define on-call periods and then hook this up to a 3rd party service that can send a text message for you. This is fine when you are alone on-call but become very complicated when you have a team. That’s what a company started in 2009 is doing in the Cloud: PagerDuty. It’s a service that allows you to define on-call teams, escalation policies and services integration.

# On-call management system flow

Let’s get a bit more into detail about the flow of an on-call management system such as PagerDuty. First of all you have to understand that PagerDuty is not monitoring your website, it acts as a gateway between your monitoring tools and the software engineers that are on-call. Its goal is to alert, as soon as possible, as reliably as possible and as efficiently as possible the person or team on-call. That’s a very hard duty because if PagerDuty goes down then many sites or services going down at the same time won’t be fixed because the alerts won’t reach the on-call persons.

Let’s get into a simple and typical workflow: 1. An incident has been detected by an external monitoring tool that notifies PagerDuty. 2. PagerDuty creates an incident and assigns it to the on-call person, the alert is in a “triggered” mode. 3. The on-call person gets notified and acknowledges the alert meaning that the software engineer is looking into the problem. 4. If the engineer cannot solve the issue, she/he can escalate it (pass it on) to another co-worker. PagerDuty also allows automatic escalation in case the on-call person does not acknowledge the alert (which means that for some reason the on-call person is not available - no battery on the phone, not hearing the ringtone and all sorts of good stuff :-)) 5. A brilliant software engineer (most likely a Holberton School member) solves the issue and marks the incident as solved. Depending on the type of alert and service that notified PagerDuty, it can be auto-resolved.

On-call teams are usually rated on 2 metrics:

-   MTA (Medium Time to Acknowledgement): The time between an alert/incident is created and an on-call person acknowledged it (which means that he or she is working toward a solution)
-   MTR (Medium Time to Resolution): The time between an alert/incident being created and this same incident/alert being marked as solved

You obviously want these mean times to be as low as possible. MTA basically tells how good engineers are at answering their phone. MTR basically tells how good engineers are at solving issues.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/7abaa7f278f15dc952fd770e20922edb53c2b85b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240605%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240605T181316Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3a38164975c2e01ffa558840b4a9f8d8fea42251ad49234361be383b5b5f1aa2)

# PagerDuty

We made a partnership so that Holberton School students can utilize PagerDuty for free. For every student a team is created (team of one), we will also have teams for group projects later on.

Every PagerDuty team has an automatically created and linked: - Escalation policy - Services (which are monitoring tools, we can add more services upon demand to Holberton School staff)

We advise you to create accounts with the recommended monitoring tools and to connect them with PagerDuty using the pre-created services.

Also make sure to configure your profile to fill in your contact information and define the Notification Rules

## Background Context

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/tWUPWmR.png)](https://youtu.be/rp5cVMNmbro)

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

-   To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
-   And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Resources

**Read or watch**:

-   [Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem "Incident Report, also referred to as a Postmortem")
-   [The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem "The importance of an incident postmortem process")
-   [What is an Incident Postmortem?](https://www.pagerduty.com/resources/learn/incident-postmortem/ "What is an Incident Postmortem?")

## More Info

### Manual QA Review

**It is your responsibility to request a review for your postmortem from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

## Tasks

### 0. My first postmortem

mandatory

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)](https://twitter.com/devopsreact/status/834887829486399488)

Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

-   Issue Summary (that is often what executives will read) must contain:
    -   duration of the outage with start and end times (including timezone)
    -   what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
    -   what was the root cause
-   Timeline (format bullet point, format:  `time`  -  `keep it short, 1 or 2 sentences`) must contain:
    
    -   when was the issue detected
    -   how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
    -   actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
    -   misleading investigation/debugging paths that were taken
    -   which team/individuals was the incident escalated to
    -   how the incident was resolved
-   Root cause and resolution must contain:
    
    -   explain in detail what was causing the issue
    -   explain in detail how the issue was fixed
-   Corrective and preventative measures must contain:
    
    -   what are the things that can be improved/fixed (broadly speaking)
    -   a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
-   Be brief and straight to the point, between 400 to 600 words
    

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

#### Add URLs here:

Save

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x19-postmortem`
-   File:  `README.md`

Done?

### 1. Make people want to read your postmortem

#advanced

We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

#### Add URLs here:

Save

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x19-postmortem`
-   File:  `README.md`

Done?

Ready for a  review




Here is a post-mortem report based on the scenario you provided:

# Post-Mortem: Web Server Outage due to Blocked SSH Access

## Issue Summary
The web service experienced a major outage from 2023-08-01 08:00 UTC to 2023-08-01 14:00 UTC, impacting approximately 80% of users. The root cause was a misconfiguration that blocked incoming traffic on port 22 (SSH), preventing access to the web servers and disrupting critical system management and maintenance tasks.

## Timeline
- 08:00 UTC - The monitoring system detected that the web servers were returning 5xx errors and the service was not responding to user requests.
- 08:05 UTC - The on-call engineer was paged and began investigating the issue.
- 08:15 UTC - The engineering team was called in to help diagnose the problem. Initial assumptions were that there was a network connectivity issue or a bug in the latest code deployment.
- 09:00 UTC - After ruling out network and code-related problems, the team suspected that the web servers were not receiving necessary software updates and configuration changes.
- 10:00 UTC - The incident was escalated to the system administration team to investigate the server-level configuration.
- 11:00 UTC - The system administrators discovered that port 22 (SSH) had been blocked, preventing them from accessing the web servers remotely.
- 11:30 UTC - The root cause was identified as a misconfiguration of the firewall rules during the initial server setup, where SSH access had been inadvertently disabled.
- 12:00 UTC - The firewall rules were updated to allow incoming traffic on port 22, and the system administrators were able to connect to the web servers.
- 13:00 UTC - The necessary software updates and configuration changes were applied to the web servers, and the service began to recover.
- 14:00 UTC - After verifying the web service had stabilized, the outage was declared resolved.

## Root Cause and Resolution
The root cause of the incident was a misconfiguration of the firewall rules during the initial setup of the web servers. The SSH port (port 22) had been blocked, preventing the system administrators from remotely accessing and managing the servers. This disrupted the ability to perform critical tasks, such as applying software updates and configuration changes, causing the web service to become unstable and unresponsive.

To resolve the issue, the system administration team quickly identified the problem and updated the firewall rules to allow incoming traffic on port 22. This restored the ability to connect to the web servers and apply the necessary updates and changes, allowing the service to recover and resume normal operation.

## Corrective and Preventative Measures
To prevent similar incidents in the future, the following actions will be taken:

1. Implement a standardized server provisioning and configuration process, with clear checklists and validation steps to ensure all necessary ports and services are properly configured.
2. Enhance the monitoring and alerting system to detect any network connectivity issues or service disruptions, including blocked ports or firewall rule changes.
3. Establish a clear communication protocol between the system administration, network, and engineering teams to ensure timely coordination during incident response.
4. Provide additional training for the system administration team on best practices for server hardening and configuration management.
5. Review and update the incident response and escalation procedures to improve the efficiency and effectiveness of troubleshooting and resolution.
6. Implement regular security audits and vulnerability assessments to identify and address potential configuration issues or security vulnerabilities.


[image_0]: https://pfst.cf2.poecdn.net/base/image/f6961f00ae640276641918bd4434226255543de224dc50d1490e9c7777dab9a3?w=161&h=81&pmaid=95004869
Here's an updated version of the post-mortem report with a touch of humor and a diagram to catch the audience's attention:

# Post-Mortem: The Great SSH Lockout of 2023

## Issue Summary
The web service experienced a major outage from 2023-08-01 08:00 UTC to 2023-08-01 14:00 UTC, leaving approximately 80% of our users feeling like they were trapped in a digital escape room with no way out. The root cause? A classic case of "Oops, I did it again" - a firewall configuration mishap that blocked incoming traffic on port 22 (SSH), preventing access to the web servers and disrupting critical system management and maintenance tasks.

## Timeline
- 08:00 UTC - The monitoring system, ever the vigilant watchdog, detected that the web servers were returning 5xx errors, leading the on-call engineer to exclaim, "Houston, we have a problem!"
- 08:05 UTC - The on-call engineer was paged, and they sprang into action, channeling their inner Sherlock Holmes to unravel the mystery.
- 08:15 UTC - The engineering team, armed with their thinking caps and a healthy dose of caffeine, joined the investigation, exploring various leads, from network connectivity issues to a potential bug in the latest code deployment.
- 10:00 UTC - The incident was escalated to the system administration team, who were summoned like the Avengers, ready to save the day.
- 11:00 UTC - The system administrators, after a thorough examination of the server logs, discovered the culprit: a firewall that was tighter than a drum, blocking SSH access and leaving the team feeling like they were locked out of their own party.
- 12:00 UTC - With a few strategic keystrokes, the system administrators unlocked the doors, allowing the team to apply the necessary updates and configurations, much to the relief of the anxious users.
- 14:00 UTC - The web service was back online, and the team breathed a collective sigh of relief, vowing to never let this happen again (at least until the next time it does).

## Root Cause and Resolution
The root cause of the incident was a classic case of "finger-pointing at the firewall," where the SSH port (port 22) had been blocked, preventing the system administrators from remotely accessing and managing the servers. This disrupted the ability to perform critical tasks, such as applying software updates and configuration changes, causing the web service to become as unstable as a house of cards in a hurricane.

To resolve the issue, the system administration team quickly identified the problem and updated the firewall rules to allow incoming traffic on port 22, restoring the team's ability to connect to the web servers and apply the necessary updates and changes. It was a classic case of "open sesame" - once the door was unlocked, the service was able to recover and resume normal operation.

## Corrective and Preventative Measures
To prevent similar incidents in the future, the team has developed a comprehensive plan that includes:

1. Implementing a standardized server provisioning process, complete with checklists and validation steps to ensure all necessary ports and services are properly configured.
2. Enhancing the monitoring and alerting system to detect any network connectivity issues or service disruptions, including blocked ports or firewall rule changes.
3. Establishing clear communication protocols between the system administration, network, and engineering teams to ensure timely coordination during incident response.
4. Providing additional training for the system administration team on best practices for server hardening and configuration management.
5. Reviewing and updating the incident response and escalation procedures to improve the efficiency and effectiveness of troubleshooting and resolution.
6. Implementing regular security audits and vulnerability assessments to identify and address potential configuration issues or security vulnerabilities.

![Diagram of the Corrective and Preventative Measures][image_0]

By implementing these measures, the team hopes to prevent similar incidents from occurring in the future, ensuring that our users can access the web service without feeling like they're trapped in a digital escape room.
