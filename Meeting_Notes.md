# Meeting Overview

| Date       | Participants                           | Agenda                                                                       |
|------------|----------------------------------------|------------------------------------------------------------------------------|
| 2024-11-04 | Isaac, Kalle, Malte, Asim, Jessie, Nas | First meeting, organizational matters                                        |
| 2024-11-07 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Decide ideas for pitch presentation. Create initial slides                   |
| 2024-11-11 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Finalize slides for pitch meeting                                            |
| 2024-11-14 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Discussed Training approaches                                                |
| 2024-11-18 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Discussed Training approaches and data, evaluation methods                   |
| 2024-11-22 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Discussed ML pipeline standardization approaches, training, front-end development, metadata & deployment plans                   |
| 2024-11-26 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Discussed about what the frontend should include, decided whether recall or precision is more important for model training and looked at the ways to deploy using Kubernetes and Docker.                  |
| 2024-11-29 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Merged branches, created new issues. Divide tasks |
| 2024-12-03 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Prepared questions for TA. Evaluated remaining work. Divided tasks. |
| 2024-12-09 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Everyone setup environment for cloud development. Divided tasks |
| 2024-12-10 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Finish remaining features and solve merge conflicts. |
| 2024-12-11 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Finish remaining features and solve merge conflicts. Fix bugs. Deploy system. Fix deployment issues. Work on Assignment 2.|
| 2024-12-12 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Finish remaining features and solve merge conflicts. Fix bugs. Test the deployed system. Fix deployment issues. Work on Assignment 2. |
| 2024-12-13 | Isaac, Kalle, Malte, Asim, Jessie, Nas | Finalize Deployment. Work on Presentation. Divide Tasks. Work on Assignment 2. |
---

# Attendance Tracker
✅ = Present | ❌ = Absent

| Name     | Assignment 1 Meetings  | Assignment 2 Meetings|
|----------|------------------------|----------------------|
| Kalle    | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |
| Malte    | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |
| Isaac    | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |
| Nas      | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |
| Jessie   | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |
| Asim     | ✅✅✅✅✅✅         |✅✅✅✅✅✅✅✅    |

---

# Detailed Meeting Descriptions

### Meeting 1 - Monday, 04-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Formed team
* Discussed expectations: Aiming for a grade of 4.
* Discussed initial ideas: stock market prediction, house price prediction in Sweden with regression models, pdf course outline database with classifiers
* Discussed challenges of obtaining data: Kaggle, openML datasets have many datasets although mainly from US, Sveriges dataportal & scb have some Swedish data. In comparison, scraping data and cleaning it will take more time/effort for project MVP.\

**TODO:** Each team member must generate 1-2 project ideas for discussion at the next meeting.

---

### Meeting 2 - Thursday, 07-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Each team member presented new ideas
* Decided on top-3 ideas by voting
* Created initial slides for ideas-pitch presentation
* Further discussed challenges of obtaining data

**TODO:** Obtain data for top-3 ideas before ideas-pitch presentation

---

### Meeting 3 - Monday, 11-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Updated powerpoint slides for pitch meeting
* Retrieved and stored data using SQLite from Alpaca API for pitch meeting 
* Prepared for presentation 

**TODO:** Present at pitch meeting, plan next steps

---
### Meeting 4 - Thursday, 14-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Discussed training approaches for the system.
* Discussed specific implementation details for the training phase.

**TODO:** Contunue writing assignment 1 

---

### Meeting 5 - Monday, 18-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Further discussed training approaches for the system.
* Further discussed specific implementation details for the training phase.
* Discussed division of initial issues, such as data cleaning, the website and the model training section
* 3 initial issues, 1 for each invesment strategy (RSI, MACD, EMA)


**TODO:** Finish writing Assignment 1, start working  on data cleaning

---

### Meeting 6 - Friday, 22-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* ML pipeline standardization: 
* ML model training: 
* Front-end development: 

**TODO:** TA meeting on Tuesday at 1:30pm. Discussed metadata (scripts, JSON) & deployment plans (K8s, Docker) after training is complete. Start A2.

---

### Meeting 7 - Tuesday, 26-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Frontend development: What it should contain and not. How we want to approach different user roles
* Model training: Which evaluation metric do we value higher? Recall or Precision? And why?
* Deployment: Discussed kubernetes, docker, what the best way to deploy is 

**TODO:** TA meeting on Tuesday at 1:30pm. Finish model training pipeline for now. Start work on the report. Start looking into deployment.

---


### Meeting 8 - Friday, 29-11-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Merge branches and solve merge conflicts
* Create new issues
* Divide tasks among team members

**TODO:** Work on individual tasks. 

---

### Meeting 9 - Tuesday, 03-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Prepare questions for TA meeting
* Divide new tasks between team members
* Ensure every team member has a task to work on until the next meeting
* Discuss what is left to do implementation-wise before work can commence on the report

**TODO:** Work on individual tasks. 

---
### Meeting 10 - Monday, 09-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Kalle and Isaac demo cloud and k8s setup
* Everyone installed and setup environment for cloud development
* Divide tasks among team members

**TODO:** Work on individual tasks. 

---
### Meeting 11 - Tuesday, 10-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Pair-programming and debugging to finish final remaining features
* TA meeting with Yi Peng - clarify requirements for unit testing (redundant to unit test more than 1 classification model as they are all similar)
* Merge bugfixes related to system integration (paths, URLs)

**TODO:** TA meeting with Yi Peng at 13:30. Work on individual tasks. 

---
### Meeting 12 - Wednesday, 11-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Pair-programming and debugging to finish final remaining features
* Solve merge conflicts
* Fix deployment issues (paths)
* Work on Assignment 2 report

**TODO:** Work on individual tasks. 

---

### Meeting 13 - Thursday, 12-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Pair-programming and debugging to finish final remaining features
* Solve merge conflicts
* Fix deployment issues (paths, permissions)
* Test deployed system
* Work on Assignment 2 report

**TODO:** Work on individual tasks. 

---

### Meeting 14 - Thursday, 11-12-24
**Attendance:** Kalle, Malte, Isaac, Nas, Jessie, Asim
* Work on Assignment 2 report - further divide tasks
* Finalize deployment (MVP project)
* Work on Presentation and assign responsibilities

**TODO:** Presentation is on Tuesday, from 10:15-12:00 in Jupiter 243. We will present our MVP project and provide feedback to other groups.