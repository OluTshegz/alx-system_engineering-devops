
# 0x11. What happens when you type google.com in your browser and press Enter

DevOps, Network, SysAdmin

## Background Context

Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack.

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area.

Let’s practice by exploring the infrastructure side (network, servers, security…) of the question.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/298/aJPw3mw.jpg)

## Requirements

### General

- You can post your blog post on the platform of your choice, LinkedIn or Medium are good ones
- A  `README.md`  file, at the root of the folder of the project, is mandatory

## More Info

## Tasks

### 0. What happens when

mandatory

This question is a classic and still widely used interview question for many types of software engineering position. It is used to assess a candidate’s general knowledge of how the web stack works on top of the internet. One important guideline to begin answering this question is that you should ask your interviewer whether they would like you to focus in on one specific area of the workflow. For a front-end position they may want you to talk at length about how the DOM is rendering. For an SRE position they may want you to go into the load balancing mechanism.

This question is a good test of whether you understand DNS. Many software engineering candidates struggle with this concept, so if you do well on this question, you are already way ahead of the curve. If you take this project seriously and write an excellent article, it may be something that will grab the attention of future employers.

Write a blog post explaining what happens when you type  `https://www.google.com`  in your browser and press  `Enter`.

Requirements, your post must cover:

- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database

Publish your blog post on Medium or LinkedIn; share the URL of your blog post in your answer file and in the field below.

Technical Write-up (Article/Blog)

Title: Navigating the Depths: A Comprehensive Exploration of the Layers Behind a Web/URL Request

Introduction:
Embarking on the journey of a URL/Web request unveils a labyrinthine network of technologies and protocols, each layer intricately woven into the fabric of Internet communication. In this comprehensive expedition, we'll delve into the depths of DNS resolution, TCP/IP communication, firewall protection, HTTPS encryption, load balancing, web serving, application processing, and database management. Join us as we navigate the complexities of the web stack, unraveling the mysteries that govern the flow of data across the digital landscape. Let's dive deep into each layer involved in the journey of this request.

Before that, let's check out what the url is all about:
The URL "https://google.com" may seem like a simple web address, but it's actually a doorway to a world of technology and security measures that keep our online experiences safe and smooth.

Let's break it down:
1. **https://**: This part tells your browser to use a secure connection (HTTPS) when talking to the Google website. It's like making sure your conversation is private and encrypted so no one else can listen in.
2. **google.com**: This is the name of the website you're visiting. It's like looking up a friend's name in your phone contacts to call them. When you type "google.com" into your browser, your computer needs to figure out the unique number (IP address) associated with that name so it can connect to the right server.

When you hit enter, your computer starts a process called DNS resolution. It's like asking a map where to find Google's house. Your computer sends a request to a DNS server, which is like a big directory that helps match website names to their IP addresses. Once your computer gets the right IP address for "google.com," it's cached so future visits are faster.
The URL doesn't include any extra stuff like subdomains (like "mail.google.com"), paths (like "/search"), or query parameters (like "?q=search"), so it's just pointing directly to Google's main page.
In simpler terms, "https://google.com" is like knocking on Google's front door, but with a secret handshake to make sure no one else can eavesdrop on your conversation. It's a straightforward way to access one of the most popular websites on the internet while keeping your connection secure and private.

1. DNS Request/Resolution:
The Domain Name System (DNS) serves as the cornerstone of Internet navigation. When you type "https://www.google.com" into your browser, the DNS request initiates the process. The DNS system acts as a phone book of the internet, translating human-readable domain names (like google.com) into machine-readable IP addresses (like 216.58.216.164). The DNS request begins with the client (your browser) querying a DNS resolver, which could be your ISP's resolver or a public resolver like Google's Public DNS. Before reaching out to external resolvers, however, the client first checks its local cache, including the browser's cache and the host system OS cache, to see if the requested domain's IP address is already stored locally. If found, this cached IP address is used, bypassing the need for a full DNS resolution process, saving time, improving performance, and reducing network traffic, thereby saving network resources. In the absence of a cached entry, a recursive DNS query is initiated to resolve the IP address associated with the domain. The resolver then iteratively or recursively traverses the DNS hierarchy, starting from the root servers. It first queries the root servers to determine the authoritative DNS servers responsible for the top-level domain (TLD), which in this case is ".com". Once identified, it queries the authoritative DNS servers for the ".com" TLD to obtain the IP address of the authoritative name servers responsible for the "google.com" domain. Continuing the journey, the resolver then queries the authoritative name servers for "google.com" to finally retrieve the IP address associated with the domain. If the domain has subdomains (e.g., "www"), additional DNS queries may be required to resolve the IP addresses of these subdomains. Once the IP address is obtained, it is cached by the resolver for future use, reducing the need for repeated DNS lookups and improving performance. The resolver then returns the IP address to the client, allowing the browser to establish a connection with the web server hosting the requested website. Through caching mechanisms at various levels and iterative querying through the DNS hierarchy, DNS resolution optimizes performance and ensures efficient navigation across the Internet.

2. TCP/IP Communication:
At the core of internet communication lies the symbiotic duo of the Transmission Control Protocol (TCP) and Internet Protocol (IP), collectively referred to as TCP/IP. TCP/IP serves as the foundational framework that enables seamless data exchange across disparate networks. Upon obtaining the IP address of the requested website, the browser initiates a TCP connection with the web server. TCP, a reliable and connection-oriented protocol, orchestrates the intricate dance of data transmission between the client and the server. It implements robust mechanisms such as flow control, error detection, and retransmission to ensure the ordered and error-free delivery of data packets. This process begins with the client sending a SYN (synchronization) segment to the server, indicating its intent to establish a connection. Concurrently, IP governs the routing and addressing of data packets across the network, facilitating the transmission of information between source and destination endpoints. IP breaks down the data into smaller packets and assigns sequence numbers to each packet, ensuring efficient transmission across the network. These packets traverse the internet, navigating through various routers and network devices, until they reach their intended destination. The connection establishment between the client and the server is facilitated by TCP's three-way handshake mechanism. The client sends a SYN segment to the server, which responds with a SYN/ACK (synchronization acknowledgment) segment, acknowledging the SYN request and signaling its readiness to establish a connection. Finally, the client acknowledges the server's SYN/ACK segment with an ACK segment, confirming the successful establishment of the connection. Together, TCP/IP forms the bedrock of internet communication, enabling reliable and efficient data exchange. By seamlessly integrating TCP's connection-oriented approach with IP's routing and addressing capabilities, TCP/IP ensures the smooth transmission of data packets across the internet, facilitating communication between users and servers worldwide.

3. Firewall Protection:
In the intricate dance of internet communication, data encounters formidable guardians known as firewalls before establishing a TCP connection. These network security sentinels stand as bastions of defense, entrusted with enforcing access control policies and shielding against malicious activities. Before data packets can initiate the TCP handshake, they must pass through the vigilant scrutiny of firewalls. These network security barriers operate at the network perimeter, meticulously inspecting incoming and outgoing traffic to filter, block, or allow packets based on predefined rulesets. By leveraging a combination of IP addresses, ports, and protocols, firewalls enact stringent security policies that shield against unauthorized access, network attacks, and malicious activities. Firewalls come in various forms, ranging from hardware appliances to software solutions deployed at network boundaries or on individual machines. Stateful inspection firewalls, in particular, maintain a keen contextual awareness of network connections. They meticulously track the state of sessions, enabling them to discern legitimate traffic from potential threats and permit or deny traffic accordingly. Beyond their primary role as gatekeepers, firewalls are augmented by intrusion detection and prevention systems (IDPS). These systems serve as vigilant watchdogs, detecting and mitigating suspicious network activity in real-time. By thwarting potential threats before they compromise network integrity, IDPS complements the protective capabilities of firewalls, ensuring robust security measures are in place to safeguard against evolving cyber threats. In summary, firewalls stand as stalwart defenders in the realm of internet communication. Their unwavering vigilance, coupled with the capabilities of intrusion detection and prevention systems, fortifies network defenses and bolsters resilience against an ever-evolving landscape of cyber threats.

4. HTTPS (SSL/TLS) Encryption::
In today's digital landscape, where cybersecurity threats loom large, ensuring secure communication over the internet is of paramount importance. Enter Hypertext Transfer Protocol Secure (HTTPS), a fortified version of the traditional HTTP protocol that incorporates cryptographic mechanisms to safeguard the confidentiality, integrity, and authenticity of data exchanged between clients and servers. When a website employs HTTPS, it signifies the initiation of a secure communication protocol that leverages SSL/TLS (Secure Sockets Layer/Transport Layer Security) encryption. This encryption forms the backbone of HTTPS, establishing a secure connection between the client (typically a web browser) and the web server hosting the site. The SSL/TLS handshake process orchestrates the establishment of this secure connection. Initially, the server presents its digital certificate to the client, providing proof of its identity. The client then undertakes the crucial step of verifying the authenticity of the certificate, ensuring it emanates from a trusted source. Following successful authentication, both parties mutually agree upon a shared encryption algorithm and cryptographic keys, laying the foundation for a secure session. The encryption afforded by SSL/TLS protocols ensures the confidentiality and integrity of data transmitted between the client and the server. By encrypting data in transit, HTTPS mitigates the risks posed by eavesdropping, tampering, and impersonation attacks, safeguarding sensitive information exchanged during online interactions. Central to the HTTPS ecosystem are digital certificates, issued by trusted Certificate Authorities (CAs). These certificates serve as the linchpin of trust, validating the identity of websites and facilitating secure key exchange during the SSL/TLS handshake. By instilling trust and confidence in online interactions, digital certificates play a pivotal role in fortifying the security posture of HTTPS-enabled websites. In essence, HTTPS encryption, powered by SSL/TLS protocols and bolstered by digital certificates, serves as a bulwark against cyber threats, ensuring the secure transmission of data across the vast expanse of the internet. By embracing HTTPS, websites demonstrate a commitment to safeguarding user privacy and fostering a secure online environment.

5. Load Balancer:
In the realm of high-traffic websites and applications, load balancers emerge as indispensable linchpins, orchestrating the seamless distribution of incoming requests across a multitude of backend web servers. Their role is paramount in optimizing performance, scalability, and availability, ensuring that users experience uninterrupted service even during periods of peak demand. Load balancers operate as sophisticated traffic managers, utilizing a repertoire of algorithms such as round-robin, least connections, and weighted distribution. These algorithms intelligently assess factors like server health, capacity, and proximity to determine the most suitable server to handle each incoming request. By dynamically routing traffic based on these metrics, load balancers ensure that backend servers operate at peak efficiency, maximizing resource utilization and minimizing response times. Moreover, load balancers serve as vigilant guardians of server health, continuously monitoring the performance and availability of backend nodes. In the event of server overload or failure, load balancers swiftly reroute traffic to healthier nodes, preventing service disruptions and maintaining uninterrupted user experiences. The significance of load balancers extends beyond performance optimization; they also bolster the resilience and fault tolerance of web applications. By evenly distributing workload across multiple backend servers, load balancers mitigate the risk of overloading individual nodes and minimize the impact of potential server failures. This redundancy ensures that even in the face of hardware failures or network issues, users can access the application without interruption. In essence, load balancers epitomize the synergy between technology and scalability, enabling web applications to effortlessly navigate the ebb and flow of user demand. Their adept management of incoming traffic not only optimizes performance but also fortifies the reliability and availability of web services, underscoring their indispensable role in the modern digital landscape.

6. Web Server:
In the intricate web of internet communication, HTTPS requests find their way to the backend infrastructure, where they encounter the pivotal role of web servers. These specialized software platforms serve as the linchpin of the client-server interaction, tasked with processing incoming requests and delivering web content with finesse. Upon arrival at the web server, the HTTPS request undergoes meticulous processing, initiating a chain of events orchestrated by the HTTP protocol. Web servers, such as Apache HTTP Server or Nginx, stand at the forefront, ready to tackle the challenges posed by client requests. Leveraging the robust capabilities of the HTTP protocol, they adeptly handle tasks ranging from routing requests to executing server-side scripts like PHP or Python. But the duties of a web server extend beyond mere request handling. They are the custodians of web content, responsible for serving static files such as HTML, CSS, and images, as well as retrieving dynamic content to cater to the ever-evolving needs of users. Whether it's managing sessions or generating HTTP responses tailored to client specifications, web servers excel in their multifaceted roles. In the realm of modular architecture and configuration directives, web servers offer unparalleled flexibility and scalability. They are equipped with a repertoire of request processing modules, allowing them to adapt to diverse requirements and use cases seamlessly. Whether communicating with an application server to retrieve data or independently generating responses based on requested resources, web servers operate with precision and efficiency. In essence, web servers serve as the backbone of web infrastructure, orchestrating the flow of data between clients and servers with finesse. Through their adept handling of HTTP requests and meticulous management of web content, they ensure the seamless delivery of web services to users worldwide.

7. Application Server Processing:
In the realm of dynamic web applications, the role of application servers is paramount. These servers serve as the backbone, executing server-side code to generate dynamic content and manage complex business logic. They act as the engine driving the functionality and interactivity of modern web applications. Application servers are versatile platforms that support a wide array of programming languages and frameworks, including PHP (Laravel), Python (Django), Ruby (Ruby on Rails), and Java (Spring Boot). This flexibility enables seamless integration with databases, external services, and third-party APIs, facilitating the development of robust and feature-rich web applications. From session management and authentication to data processing and presentation logic, application servers play a central role in orchestrating the various components of a web application. They provide developers with the tools and environment needed to implement sophisticated features and deliver personalized user experiences. In the architecture of web applications, web servers often delegate the processing of dynamic content to application servers. These application servers, also referred to as application containers or middleware, handle the heavy lifting of executing server-side scripts, frameworks, and application-specific code. Popular examples of application servers include Tomcat, Jetty, and Node.js. These servers excel in executing the dynamic code of web applications, managing business logic, processing user input, and interacting with databases or external services. In summary, application servers serve as the bridge between web servers and the complex functionality of dynamic web applications. They provide the necessary infrastructure and capabilities for developers to build powerful and scalable web applications that drive innovation and deliver exceptional user experiences.

8. Database Management:
Deep within the intricate backend infrastructure of web applications lies the pivotal nerve center of data management—the database server. When a requested web page or resource necessitates data retrieval, the application server seamlessly interacts with the database management system (DBMS). Databases, whether relational such as MySQL, PostgreSQL, SQL Server, or NoSQL variants like MongoDB or Redis, serve as repositories for vast volumes of structured and unstructured data. In this symbiotic relationship, application servers communicate with the database using standardized protocols such as SQL (Structured Query Language) or other query languages. Through these protocols, application servers submit queries to the database, retrieve the requisite information, and integrate it into the response destined for the client. This cohesive interaction ensures that the web application dynamically delivers accurate and relevant data to users in real-time. Furthermore, databases play a pivotal role in maintaining data integrity, ensuring efficient data retrieval, and offering a suite of advanced features such as indexing, transactions, and replication. These features contribute to the scalability, fault tolerance, and reliability of the underlying data infrastructure. Database servers are the guardians of transactional integrity, concurrency control, and data consistency, guaranteeing the reliability and integrity of mission-critical business data. Through sophisticated indexing techniques, query optimization strategies, and replication mechanisms, databases empower organizations to extract actionable insights, drive informed decision-making, and propel digital transformation initiatives forward. In essence, the synergy between application servers and database servers forms the backbone of data-driven web applications. By leveraging standardized protocols and advanced features offered by modern database management systems, organizations can unlock the full potential of their data assets, driving innovation and competitive advantage in today's digital landscape.

The conclusion encapsulates the holistic journey of a URL request, showcasing the intricate web of technologies and protocols that orchestrate the seamless browsing experience. Beyond mere browsing, it highlights the collaborative dance of DNS resolution, TCP/IP communication, firewall protection, HTTPS encryption, load balancing, web serving, application processing, and database management. In this journey, each layer plays a vital role, ensuring the reliability, security, and efficiency of data transmission from the client's browser to the server hosting the requested website. From the initial DNS resolution to the establishment of a secure TCP/IP connection, and the subsequent processing of the request by web servers and application servers, every step is meticulously orchestrated to deliver web content with precision and speed. By comprehensively understanding the functionality and interplay of these layers, individuals gain profound insights into the complex processes that underpin the digital landscape. Armed with this knowledge, they are equipped to navigate challenges, harness opportunities, and shape the future of the internet with confidence and clarity. It underscores the interconnectedness of technologies and the collaborative effort required to sustain the seamless browsing experience enjoyed by users worldwide.


Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

#### Add URLs here

Save

**Repo:**

- GitHub repository:  `alx-system_engineering-devops`
- Directory:  `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
- File:  `0-blog_post`

Done?

### 1. Everything's better with a pretty diagram

# advanced

Add a schema to your blog post illustrating the flow of the request created when you type  `https://www.google.com`  in your browser and press  `Enter`.

The diagram should show:

- DNS resolution
- that the request hitting server IP on the appropriate port
- that the traffic is encrypted
- that the traffic goes through a firewall
- that the request is distributed via a load balancer
- that the web server answers the request by serving a web page
- that the application server generates the web page
- that the application server request data from the database

[Gliffy](https://intranet.alxswe.com/rltoken/0KvO5Zd6t2GfDUiUHvNJjQ "Gliffy")  is free and what I personally use, but feel free to use what fits you best.

Some unrelated examples:

![](http://i.imgur.com/i9ivkdo.png)

![](http://i.imgur.com/R8R3sqC.png)

Share the URL of your diagram image in your answer file and il the field below.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

#### Add URLs here

Save

**Repo:**

- GitHub repository:  `alx-system_engineering-devops`
- Directory:  `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
- File:  `1-what_happen_when_diagram`

Done?

### 2. Contribute

# advanced

Folks on the Internet have been trying to put together a comprehensive answer to the question. Help them by submitting a pull request. Paste the link in your answer file.

[https://github.com/alex/what-happens-when#the-g-key-is-pressed](https://github.com/alex/what-happens-when#the-g-key-is-pressed "https://github.com/alex/what-happens-when#the-g-key-is-pressed")

Requirements:

- The pull request must bring meaningful value (not a typo correction or style improvement)
- Share the pull request URL in your answer file and in the field below

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

#### Add URLs here

Save

**Repo:**

- GitHub repository:  `alx-system_engineering-devops`
- Directory:  `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
- File:  `2-contribution-to_what-happens-when_github_answer`

Done?
