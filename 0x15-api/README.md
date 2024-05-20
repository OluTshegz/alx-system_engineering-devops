# 0x15. API

Python, Scripting, Back-end, API

### Concepts

_For this project, we expect you to look at this concept:_

-   [Portfolio Project Deeper Overview](https://intranet.alxswe.com/concepts/102042)

# Portfolio Project Deeper Overview

# Portfolio Project Guide

Welcome to an exciting phase in your ALX journey—**Section 3**, where you’ll embark on a Portfolio Project. This guide aims to provide you with all the necessary details to navigate this project successfully.

We also had a Q & A Session on Zoom. If you prefer watching a video you can use this. *_Recording - *_  [Link](https://sandtech.zoom.us/rec/component-page?action=viewdetailpage&sharelevel=meeting&useWhichPasswd=meeting&clusterId=us06&componentName=need-password&meetingId=BuQjDtQ54Uxhv9Rm7sSQIycBH6gyQNnGNN4t5L-j8YpT9nbD7B1TE6rQWhfNj0z5.aRAKudyt7NQREtKj&originRequestUrl=https%3A%2F%2Fsandtech.zoom.us%2Frec%2Fshare%2F-Dsl_R4DA_rNh7FCWsa8uUX2OR6_Pe2cC-ci2BMvPBAbhIseR11nrwqqfIk-ErwQ.0Z3ySSLrT70FcKWB "Link")  *_Password - *_  @W3h5u2$
[Link](https://sandtech.zoom.us/rec/play/CVGDXPed0OqcZnKY_rgCdWmtUEOr2YGqtZuX3O237FcNxSvYVeouPJAZTDJUR1Ap2tiMJ9piwp9SVGkv.JaUj9rEZ-IjQJwYM?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fsandtech.zoom.us%2Frec%2Fshare%2F-Dsl_R4DA_rNh7FCWsa8uUX2OR6_Pe2cC-ci2BMvPBAbhIseR11nrwqqfIk-ErwQ.0Z3ySSLrT70FcKWB "Link")

## What is a Portfolio Project?

The Portfolio Project is a capstone endeavor designed to encapsulate all the skills and knowledge you’ve acquired during the ALX Foundations program. You will be tasked with creating a project from scratch, showcasing your ability to apply what you’ve learned in a real-world context.

## Freedom to Explore

We’re setting you free on this one. There are  **no strict guidelines**  on what to build. Your heart’s desire, guided by your creative spirit, is the limit. Mobile apps, web applications, game development—pick your passion and run with it.

## Project Structure Overview

Your Portfolio Project will unfold in three distinct stages, each with its own set of objectives and deliverables.

### 1. Research Phase

**Duration:**  3 weeks, comprising 3 mini-projects.

-   **Idea Generation:**  Begin with brainstorming and documenting your project idea.
-   **MVP Design:**  Develop a concept for a Minimum Viable Product (MVP).
-   **Project Planning:**  Draft a detailed plan on how you’ll execute the projects.

### 2. Building Phase

**Duration:**  3 weeks, also with 3 projects.

-   **Development:**  This is where your project starts to take shape. Begin with the MVP and expand from there.
-   **Landing Page Creation:**  Develop a compelling landing page for your project.
-   **Presentation Preparation:**  Start preparing for your project presentation.

### 3. Post-Project Phase

**Duration:**  1-2 weeks

-   **Blog Post:**  Write about your experience and what you learned during the project development process.
-   **GitHub Clean-up:**  Refine your project’s GitHub repository, focusing on improving the README and documentation.
-   **Final Presentations:**  If you haven’t presented your project yet, now is the time.

## Key Considerations

### Teams

You can choose to work individually or collaborate in teams of up to three. However, the team you choose for the Research and Project Approval (Part 1) is the team you’ll work with throughout these seven weeks. Team adjustments won’t be possible.

We highly encourage you to make informed decisions when picking your teammates. Whoever you pick in Research and Project Approval (Part 1) is the person you will be stuck with for the next 8 weeks. Don’t randomly pair up with people. Before making a pairing request to someone or accepting a pairing request from someone, make sure to have a conversation with them.

If you want to work in a team of 3 people, you are supposed to send a request to the 2 other people at the same time. If you make a request to only one person, you will end up in a team of 2 people.

Team Repairing is not going to be done for the portfolio project, therefore kindly follow the instructions.

### Time Management

We’ve seen so many cases of learners under-estimating the amount of work required in their portfolio project. Please begin working on your project as soon as possible. Don’t wait until the last minute. Plan your time really well. The Reasrach and Planning project Part 3 will help you with this, make sure you follow the plan you come up with.

### Presentation

After you are done building you will be expected to present your project to senior learners. There is a process in place for this you will learn more when we get to this part. The presentation is very important. If you fail to present your project and consequently not get scored for the Portfolio project you will not be validated and you won’t be able to proceed to specialization.

### No Project Idea?

As indicated in the other concept page, if you are unable to come up with your own idea, you can build the Maze Project. If you pick the maze project you are still expected to do all the other projects i.e Research, Building … The only difference is that your project idea is provided by ALX. You will do your Research Part of the project around the Maze Project.

## Support and Questions

If you have any questions or need clarifications, feel free to ask on Discord. We’ll also have sessions throughout the 7-week period to help you overcome any obstacles.

**We’re thrilled to see the amazing projects you’ll create. Your ALX journey is reaching new heights, and we’re here to support you every step of the way.**

## Background Context

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240520%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240520T112521Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=771865ff920b6b3b47b6909d1939904ea5f5c3829764052386ea64c1b2270749)](https://youtu.be/-2kyU6-j8ZQ)

[https://youtu.be/-2kyU6-j8ZQ]()
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources

**Read or watch**:

-   [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script "Friends don't let friends program in shell script")
-   [What is an API](https://www.webopedia.com/definitions/api/ "What is an API")
-   [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/ "What is an API? In English, please")
-   [What is a REST API](https://www.sitepoint.com/rest-api/ "What is a REST API")
-   [What are microservices](https://smartbear.com/learn/api-design/microservices/ "What are microservices")
-   [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/ "PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"),  **without the help of Google**:

### General

-   What Bash scripting should not be used for
-   What is an API
-   What is a REST API
-   What are microservices
-   What is the CSV format
-   What is the JSON format
-   Pythonic Package and module name style
-   Pythonic Class name style
-   Pythonic Variable name style
-   Pythonic Function name style
-   Pythonic Constant name style
-   Significance of CapWords or CamelCase in Python

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   **Libraries imported in your Python files must be organized in alphabetical order**
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version  `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   You must use  [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get "get")  to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
-   Your code should not be executed when imported (by using  `if __name__ == "__main__":`)

## Tasks

### 0. Gather data from an API

mandatory

Write a Python script that, using this  [REST API](https://jsonplaceholder.typicode.com/ "REST API"), for a given employee ID, returns information about his/her TODO list progress.

Requirements:

-   You must use  `urllib`  or  `requests`  module
-   The script must accept an integer as a parameter, which is the employee ID
-   The script must display on the standard output the employee TODO list progress in this exact format:
    -   First line:  `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
        -   `EMPLOYEE_NAME`: name of the employee
        -   `NUMBER_OF_DONE_TASKS`: number of completed tasks
        -   `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
    -   Second and N next lines display the title of completed tasks:  `TASK_TITLE`  (with 1 tabulation and 1 space before the  `TASK_TITLE`)

Example:

```
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
sylvain@ubuntu$
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x15-api`
-   File:  `0-gather_data_from_an_API.py`

Done?  Check your code  Get a sandbox

### 1. Export to CSV

mandatory

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

-   Records all tasks that are owned by this employee
-   Format must be:  `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
-   File name must be:  `USER_ID.csv`

Example:

```
sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
"2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
"2","Antonette","True","aliquam aut quasi"
"2","Antonette","True","veritatis pariatur delectus"
"2","Antonette","False","nesciunt totam sit blanditiis sit"
"2","Antonette","False","laborum aut in quam"
"2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
"2","Antonette","False","repudiandae totam in est sint facere fuga"
"2","Antonette","False","earum doloribus ea doloremque quis"
"2","Antonette","False","sint sit aut vero"
"2","Antonette","False","porro aut necessitatibus eaque distinctio"
"2","Antonette","True","repellendus veritatis molestias dicta incidunt"
"2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
"2","Antonette","False","sunt cum tempora"
"2","Antonette","False","totam quia non"
"2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
"2","Antonette","True","totam atque quo nesciunt"
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x15-api`
-   File:  `1-export_to_CSV.py`

Done?  Check your code  Get a sandbox

### 2. Export to JSON

mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

-   Records all tasks that are owned by this employee
-   Format must be:  `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
-   File name must be:  `USER_ID.json`

Example:

```
sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x15-api`
-   File:  `2-export_to_JSON.py`

Done?  Check your code  Get a sandbox

### 3. Dictionary of list of dictionaries

mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

-   Records all tasks from all employees
-   Format must be:  `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
-   File name must be:  `todo_all_employees.json`

Example:

```
sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
sylvain@ubuntu$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false}, {"username": "Bret", "task": "fugiat veniam minus", "completed": false}, {"username": "Bret", "task": "et porro tempora", "completed": true}, {"username": "Bret", "task": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false}, {"username": "Bret", "task": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false}, {"username": "Bret", "task": "illo expedita consequatur quia in", "completed": false}, {"username": "Bret", "task": "quo adipisci enim quam ut ab", "completed": true}, {"username": "Bret", "task": "molestiae perspiciatis ipsa", "completed": false}, {"username": "Bret", "task": "illo est ratione doloremque quia maiores aut", "completed": true}, {"username": "Bret", "task": "vero rerum temporibus dolor", "completed": true}, {"username": "Bret", "task": "ipsa repellendus fugit nisi", "completed": true}, {"username": "Bret", "task": "et doloremque nulla", "completed": false}, {"username": "Bret", "task": "repellendus sunt dolores architecto voluptatum", "completed": true}, {"username": "Bret", "task": "ab voluptatum amet voluptas", "completed": true}, {"username": "Bret", "task": "accusamus eos facilis sint et aut voluptatem", "completed": true}, {"username": "Bret", "task": "quo laboriosam deleniti aut qui", "completed": true}, {"username": "Bret", "task": "dolorum est consequatur ea mollitia in culpa", "completed": false}, {"username": "Bret", "task": "molestiae ipsa aut voluptatibus pariatur dolor nihil", "completed": true}, {"username": "Bret", "task": "ullam nobis libero sapiente ad optio sint", "completed": true}], "2": [{"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false}, {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": true}, {"username": "Antonette", "task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false}, {"username": "Antonette", "task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false}, {"username": "Antonette", "task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true}, {"username": "Antonette", "task": "aliquam aut quasi", "completed": true}, {"username": "Antonette", "task": "veritatis pariatur delectus", "completed": true}, {"username": "Antonette", "task": "nesciunt totam sit blanditiis sit", "completed": false}, {"username": "Antonette", "task": "laborum aut in quam", "completed": false}, {"username": "Antonette", "task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true}, {"username": "Antonette", "task": "repudiandae totam in est sint facere fuga", "completed": false}, {"username": "Antonette", "task": "earum doloribus ea doloremque quis", "completed": false}, {"username": "Antonette", "task": "sint sit aut vero", "completed": false}, {"username": "Antonette", "task": "porro aut necessitatibus eaque distinctio", "completed": false}, {"username": "Antonette", "task": "repellendus veritatis molestias dicta incidunt", "completed": true}, {"username": "Antonette", "task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true}, {"username": "Antonette", "task": "sunt cum tempora", "completed": false}, {"username": "Antonette", "task": "totam quia non", "completed": false}, {"username": "Antonette", "task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false}, {"username": "Antonette", "task": "totam atque quo nesciunt", "completed": true}], "3": [{"username": "Samantha", "task": "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit", "completed": false}, {"username": "Samantha", "task": "rerum perferendis error quia ut eveniet", "completed": false}, {"username": "Samantha", "task": "tempore ut sint quis recusandae", "completed": true}, {"username": "Samantha", "task": "cum debitis quis accusamus doloremque ipsa natus sapiente omnis", "completed": true}, {"username": "Samantha", "task": "velit soluta adipisci molestias reiciendis harum", "completed": false}, {"username": "Samantha", "task": "vel voluptatem repellat nihil placeat corporis", "completed": false}, {"username": "Samantha", "task": "nam qui rerum fugiat accusamus", "completed": false}, {"username": "Samantha", "task": "sit reprehenderit omnis quia", "completed": false}, {"username": "Samantha", "task": "ut necessitatibus aut maiores debitis officia blanditiis velit et", "completed": false}, {"username": "Samantha", "task": "cupiditate necessitatibus ullam aut quis dolor voluptate", "completed": true}, {"username": "Samantha", "task": "distinctio exercitationem ab doloribus", "completed": false}, {"username": "Samantha", "task": "nesciunt dolorum quis recusandae ad pariatur ratione", "completed": false}, {"username": "Samantha", "task": "qui labore est occaecati recusandae aliquid quam", "completed": false}, {"username": "Samantha", "task": "quis et est ut voluptate quam dolor", "completed": true}, {"username": "Samantha", "task": "voluptatum omnis minima qui occaecati provident nulla voluptatem ratione", "completed": true}, {"username": "Samantha", "task": "deleniti ea temporibus enim", "completed": true}, {"username": "Samantha", "task": "pariatur et magnam ea doloribus similique voluptatem rerum quia", "completed": false}, {"username": "Samantha", "task": "est dicta totam qui explicabo doloribus qui dignissimos", "completed": false}, {"username": "Samantha", "task": "perspiciatis velit id laborum placeat iusto et aliquam odio", "completed": false}, {"username": "Samantha", "task": "et sequi qui architecto ut adipisci", "completed": true}], "4": [{"username": "Karianne", "task": "odit optio omnis qui sunt", "completed": true}, {"username": "Karianne", "task": "et placeat et tempore aspernatur sint numquam", "completed": false}, {"username": "Karianne", "task": "doloremque aut dolores quidem fuga qui nulla", "completed": true}, {"username": "Karianne", "task": "voluptas consequatur qui ut quia magnam nemo esse", "completed": false}, {"username": "Karianne", "task": "fugiat pariatur ratione ut asperiores necessitatibus magni", "completed": false}, {"username": "Karianne", "task": "rerum eum molestias autem voluptatum sit optio", "completed": false}, {"username": "Karianne", "task": "quia voluptatibus voluptatem quos similique maiores repellat", "completed": false}, {"username": "Karianne", "task": "aut id perspiciatis voluptatem iusto", "completed": false}, {"username": "Karianne", "task": "doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit", "completed": false}, {"username": "Karianne", "task": "ut sequi accusantium et mollitia delectus sunt", "completed": false}, {"username": "Karianne", "task": "aut velit saepe ullam", "completed": false}, {"username": "Karianne", "task": "praesentium facilis facere quis harum voluptatibus voluptatem eum", "completed": false}, {"username": "Karianne", "task": "sint amet quia totam corporis qui exercitationem commodi", "completed": true}, {"username": "Karianne", "task": "expedita tempore nobis eveniet laborum maiores", "completed": false}, {"username": "Karianne", "task": "occaecati adipisci est possimus totam", "completed": false}, {"username": "Karianne", "task": "sequi dolorem sed", "completed": true}, {"username": "Karianne", "task": "maiores aut nesciunt delectus exercitationem vel assumenda eligendi at", "completed": false}, {"username": "Karianne", "task": "reiciendis est magnam amet nemo iste recusandae impedit quaerat", "completed": false}, {"username": "Karianne", "task": "eum ipsa maxime ut", "completed": true}, {"username": "Karianne", "task": "tempore molestias dolores rerum sequi voluptates ipsum consequatur", "completed": true}], "5": [{"username": "Kamren", "task": "suscipit qui totam", "completed": true}, {"username": "Kamren", "task": "voluptates eum voluptas et dicta", "completed": false}, {"username": "Kamren", "task": "quidem at rerum quis ex aut sit quam", "completed": true}, {"username": "Kamren", "task": "sunt veritatis ut voluptate", "completed": false}, {"username": "Kamren", "task": "et quia ad iste a", "completed": true}, {"username": "Kamren", "task": "incidunt ut saepe autem", "completed": true}, {"username": "Kamren", "task": "laudantium quae eligendi consequatur quia et vero autem", "completed": true}, {"username": "Kamren", "task": "vitae aut excepturi laboriosam sint aliquam et et accusantium", "completed": false}, {"username": "Kamren", "task": "sequi ut omnis et", "completed": true}, {"username": "Kamren", "task": "molestiae nisi accusantium tenetur dolorem et", "completed": true}, {"username": "Kamren", "task": "nulla quis consequatur saepe qui id expedita", "completed": true}, {"username": "Kamren", "task": "in omnis laboriosam", "completed": true}, {"username": "Kamren", "task": "odio iure consequatur molestiae quibusdam necessitatibus quia sint", "completed": true}, {"username": "Kamren", "task": "facilis modi saepe mollitia", "completed": false}, {"username": "Kamren", "task": "vel nihil et molestiae iusto assumenda nemo quo ut", "completed": true}, {"username": "Kamren", "task": "nobis suscipit ducimus enim asperiores voluptas", "completed": false}, {"username": "Kamren", "task": "dolorum laboriosam eos qui iure aliquam", "completed": false}, {"username": "Kamren", "task": "debitis accusantium ut quo facilis nihil quis sapiente necessitatibus", "completed": true}, {"username": "Kamren", "task": "neque voluptates ratione", "completed": false}, {"username": "Kamren", "task": "excepturi a et neque qui expedita vel voluptate", "completed": false}], "6": [{"username": "Leopoldo_Corkery", "task": "explicabo enim cumque porro aperiam occaecati minima", "completed": false}, {"username": "Leopoldo_Corkery", "task": "sed ab consequatur", "completed": false}, {"username": "Leopoldo_Corkery", "task": "non sunt delectus illo nulla tenetur enim omnis", "completed": false}, {"username": "Leopoldo_Corkery", "task": "excepturi non laudantium quo", "completed": false}, {"username": "Leopoldo_Corkery", "task": "totam quia dolorem et illum repellat voluptas optio", "completed": true}, {"username": "Leopoldo_Corkery", "task": "ad illo quis voluptatem temporibus", "completed": true}, {"username": "Leopoldo_Corkery", "task": "praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt", "completed": false}, {"username": "Leopoldo_Corkery", "task": "a eos eaque nihil et exercitationem incidunt delectus", "completed": true}, {"username": "Leopoldo_Corkery", "task": "autem temporibus harum quisquam in culpa", "completed": true}, {"username": "Leopoldo_Corkery", "task": "aut aut ea corporis", "completed": true}, {"username": "Leopoldo_Corkery", "task": "magni accusantium labore et id quis provident", "completed": false}, {"username": "Leopoldo_Corkery", "task": "consectetur impedit quisquam qui deserunt non rerum consequuntur eius", "completed": false}, {"username": "Leopoldo_Corkery", "task": "quia atque aliquam sunt impedit voluptatum rerum assumenda nisi", "completed": false}, {"username": "Leopoldo_Corkery", "task": "cupiditate quos possimus corporis quisquam exercitationem beatae", "completed": false}, {"username": "Leopoldo_Corkery", "task": "sed et ea eum", "completed": false}, {"username": "Leopoldo_Corkery", "task": "ipsa dolores vel facilis ut", "completed": true}, {"username": "Leopoldo_Corkery", "task": "sequi quae est et qui qui eveniet asperiores", "completed": false}, {"username": "Leopoldo_Corkery", "task": "quia modi consequatur vero fugiat", "completed": false}, {"username": "Leopoldo_Corkery", "task": "corporis ducimus ea perspiciatis iste", "completed": false}, {"username": "Leopoldo_Corkery", "task": "dolorem laboriosam vel voluptas et aliquam quasi", "completed": false}], "7": [{"username": "Elwyn.Skiles", "task": "inventore aut nihil minima laudantium hic qui omnis", "completed": true}, {"username": "Elwyn.Skiles", "task": "provident aut nobis culpa", "completed": true}, {"username": "Elwyn.Skiles", "task": "esse et quis iste est earum aut impedit", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui consectetur id", "completed": false}, {"username": "Elwyn.Skiles", "task": "aut quasi autem iste tempore illum possimus", "completed": false}, {"username": "Elwyn.Skiles", "task": "ut asperiores perspiciatis veniam ipsum rerum saepe", "completed": true}, {"username": "Elwyn.Skiles", "task": "voluptatem libero consectetur rerum ut", "completed": true}, {"username": "Elwyn.Skiles", "task": "eius omnis est qui voluptatem autem", "completed": false}, {"username": "Elwyn.Skiles", "task": "rerum culpa quis harum", "completed": false}, {"username": "Elwyn.Skiles", "task": "nulla aliquid eveniet harum laborum libero alias ut unde", "completed": true}, {"username": "Elwyn.Skiles", "task": "qui ea incidunt quis", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui molestiae voluptatibus velit iure harum quisquam", "completed": true}, {"username": "Elwyn.Skiles", "task": "et labore eos enim rerum consequatur sunt", "completed": true}, {"username": "Elwyn.Skiles", "task": "molestiae doloribus et laborum quod ea", "completed": false}, {"username": "Elwyn.Skiles", "task": "facere ipsa nam eum voluptates reiciendis vero qui", "completed": false}, {"username": "Elwyn.Skiles", "task": "asperiores illo tempora fuga sed ut quasi adipisci", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui sit non", "completed": false}, {"username": "Elwyn.Skiles", "task": "placeat minima consequatur rem qui ut", "completed": true}, {"username": "Elwyn.Skiles", "task": "consequatur doloribus id possimus voluptas a voluptatem", "completed": false}, {"username": "Elwyn.Skiles", "task": "aut consectetur in blanditiis deserunt quia sed laboriosam", "completed": true}], "8": [{"username": "Maxime_Nienow", "task": "explicabo consectetur debitis voluptates quas quae culpa rerum non", "completed": true}, {"username": "Maxime_Nienow", "task": "maiores accusantium architecto necessitatibus reiciendis ea aut", "completed": true}, {"username": "Maxime_Nienow", "task": "eum non recusandae cupiditate animi", "completed": false}, {"username": "Maxime_Nienow", "task": "ut eum exercitationem sint", "completed": false}, {"username": "Maxime_Nienow", "task": "beatae qui ullam incidunt voluptatem non nisi aliquam", "completed": false}, {"username": "Maxime_Nienow", "task": "molestiae suscipit ratione nihil odio libero impedit vero totam", "completed": true}, {"username": "Maxime_Nienow", "task": "eum itaque quod reprehenderit et facilis dolor autem ut", "completed": true}, {"username": "Maxime_Nienow", "task": "esse quas et quo quasi exercitationem", "completed": false}, {"username": "Maxime_Nienow", "task": "animi voluptas quod perferendis est", "completed": false}, {"username": "Maxime_Nienow", "task": "eos amet tempore laudantium fugit a", "completed": false}, {"username": "Maxime_Nienow", "task": "accusamus adipisci dicta qui quo ea explicabo sed vero", "completed": true}, {"username": "Maxime_Nienow", "task": "odit eligendi recusandae doloremque cumque non", "completed": false}, {"username": "Maxime_Nienow", "task": "ea aperiam consequatur qui repellat eos", "completed": false}, {"username": "Maxime_Nienow", "task": "rerum non ex sapiente", "completed": true}, {"username": "Maxime_Nienow", "task": "voluptatem nobis consequatur et assumenda magnam", "completed": true}, {"username": "Maxime_Nienow", "task": "nam quia quia nulla repellat assumenda quibusdam sit nobis", "completed": true}, {"username": "Maxime_Nienow", "task": "dolorem veniam quisquam deserunt repellendus", "completed": true}, {"username": "Maxime_Nienow", "task": "debitis vitae delectus et harum accusamus aut deleniti a", "completed": true}, {"username": "Maxime_Nienow", "task": "debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis", "completed": true}, {"username": "Maxime_Nienow", "task": "et praesentium aliquam est", "completed": false}], "9": [{"username": "Delphine", "task": "ex hic consequuntur earum omnis alias ut occaecati culpa", "completed": true}, {"username": "Delphine", "task": "omnis laboriosam molestias animi sunt dolore", "completed": true}, {"username": "Delphine", "task": "natus corrupti maxime laudantium et voluptatem laboriosam odit", "completed": false}, {"username": "Delphine", "task": "reprehenderit quos aut aut consequatur est sed", "completed": false}, {"username": "Delphine", "task": "fugiat perferendis sed aut quidem", "completed": false}, {"username": "Delphine", "task": "quos quo possimus suscipit minima ut", "completed": false}, {"username": "Delphine", "task": "et quis minus quo a asperiores molestiae", "completed": false}, {"username": "Delphine", "task": "recusandae quia qui sunt libero", "completed": false}, {"username": "Delphine", "task": "ea odio perferendis officiis", "completed": true}, {"username": "Delphine", "task": "quisquam aliquam quia doloribus aut", "completed": false}, {"username": "Delphine", "task": "fugiat aut voluptatibus corrupti deleniti velit iste odio", "completed": true}, {"username": "Delphine", "task": "et provident amet rerum consectetur et voluptatum", "completed": false}, {"username": "Delphine", "task": "harum ad aperiam quis", "completed": false}, {"username": "Delphine", "task": "similique aut quo", "completed": false}, {"username": "Delphine", "task": "laudantium eius officia perferendis provident perspiciatis asperiores", "completed": true}, {"username": "Delphine", "task": "magni soluta corrupti ut maiores rem quidem", "completed": false}, {"username": "Delphine", "task": "et placeat temporibus voluptas est tempora quos quibusdam", "completed": false}, {"username": "Delphine", "task": "nesciunt itaque commodi tempore", "completed": true}, {"username": "Delphine", "task": "omnis consequuntur cupiditate impedit itaque ipsam quo", "completed": true}, {"username": "Delphine", "task": "debitis nisi et dolorem repellat et", "completed": true}], "10": [{"username": "Moriah.Stanton", "task": "ut cupiditate sequi aliquam fuga maiores", "completed": false}, {"username": "Moriah.Stanton", "task": "inventore saepe cumque et aut illum enim", "completed": true}, {"username": "Moriah.Stanton", "task": "omnis nulla eum aliquam distinctio", "completed": true}, {"username": "Moriah.Stanton", "task": "molestias modi perferendis perspiciatis", "completed": false}, {"username": "Moriah.Stanton", "task": "voluptates dignissimos sed doloribus animi quaerat aut", "completed": false}, {"username": "Moriah.Stanton", "task": "explicabo odio est et", "completed": false}, {"username": "Moriah.Stanton", "task": "consequuntur animi possimus", "completed": false}, {"username": "Moriah.Stanton", "task": "vel non beatae est", "completed": true}, {"username": "Moriah.Stanton", "task": "culpa eius et voluptatem et", "completed": true}, {"username": "Moriah.Stanton", "task": "accusamus sint iusto et voluptatem exercitationem", "completed": true}, {"username": "Moriah.Stanton", "task": "temporibus atque distinctio omnis eius impedit tempore molestias pariatur", "completed": true}, {"username": "Moriah.Stanton", "task": "ut quas possimus exercitationem sint voluptates", "completed": false}, {"username": "Moriah.Stanton", "task": "rerum debitis voluptatem qui eveniet tempora distinctio a", "completed": true}, {"username": "Moriah.Stanton", "task": "sed ut vero sit molestiae", "completed": false}, {"username": "Moriah.Stanton", "task": "rerum ex veniam mollitia voluptatibus pariatur", "completed": true}, {"username": "Moriah.Stanton", "task": "consequuntur aut ut fugit similique", "completed": true}, {"username": "Moriah.Stanton", "task": "dignissimos quo nobis earum saepe", "completed": true}, {"username": "Moriah.Stanton", "task": "quis eius est sint explicabo", "completed": true}, {"username": "Moriah.Stanton", "task": "numquam repellendus a magnam", "completed": true}, {"username": "Moriah.Stanton", "task": "ipsam aperiam voluptates qui", "completed": false}]}sylvain@ubuntu$

```

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x15-api`
-   File:  `3-dictionary_of_list_of_dictionaries.py`

Done?  Check your code  Get a sandbox
