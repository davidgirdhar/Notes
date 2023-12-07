
### What is cloud?

    Cloud is just a metaphorical term for the internet, where computing resources such as servers, storage, and applications are made available to users over the internet, on demand and as a service.

    Now cloud computing has two types of models 
    1. deployment model-> There are three types of deployment models -> public, private and hybrid.
    2. Service model -> There are three types of service models -> IAAS(Infra-structure as a service), PAAS(Platform as a service), SAAS( Software as a Service).

### What is virtual machine?

    A virtual machine is a emulation of physical computer using software.
    Server Virtualization allows to create, resize and migrate your server.

### what is virtualization?

    Having differnet virtual machines on a same host machine independent of each other.

### what is hypervisor?

    It is a piece of software used to create the virtualized environments allowing for multiple VMs to be installed on the same host.

### what is object storage ?

    Now first of all let basics right on object in object storage. Object contains four components. first is **id**(which is unique identifier), second is data, third is metadata(which tells about data(i.e. explain type of data in object)) and attributes(tells about access who can add, modify and delete it)

### what is aws?

    AWS is a collection of cloud services that can be used under single unified APIs.


### what is SQS?

    Amazon SQS is a web service that gives you access to a message queue that can be used to store messages while waiting for a computer to process them.

### What is s3?

    S3 stands for Simple Storage Service.It is easy to use with a simple web services interface to store and retrieve any amount of data from anywhere on the web.It is Object-based storage, i.e., you can store the images, word files, pdf files, etc.Files are stored in Bucket. A bucket is like a folder available in S3 that stores the files.Buckets are the containers in S3 that stores the data.S3 Transfer Acceleration uses the AWS backbone network and edge locations to reduce latencies from the end user to Amazon S3.


### What is Infrastructure as Code?


### Four common type of cloud services for IAAS:

1. Compute 2. Database 3. Storage 4. Networking


### What is AWS fargate?

    AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. With Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

### What is CloudFront?

    Amazon Cloudfront is a content delivery network (AWS CDN) that retrieves data stored in the Amazon S3 bucket and distributes it to numerous edge locations across the world. Edge locations are the network of data centers distributed worldwide through which content is delivered.


#### Key Terminology in AWS CloudFront.
    Edge Locations: A worldwide network of data centers that deliver content to the end-user are called edge Locations.

    Latency: It is a measure of delay or time data takes to get to its destination from the source point. 

    Amazon Content Delivery Network (AWS CDN): A content delivery network (CDN) represents a group of servers that are geographically distributed over the globe and provide a fast delivery.

    Amazon S3 Bucket: An Amazon S3 bucket is a public cloud storage resource available in Amazon Web Services.

    Origin Access Identity: An Origin Access Identity (OAI) is used for sharing private content via CloudFront. The OAI is a virtual user identity that will be used to give your CF distribution permission to fetch a private object from your origin server (e.g. S3 bucket).


### What is ElastiCache?

    Amazon ElastiCache allows you to seamlessly set up, run, and scale an in-memory cache in the cloud. ElastiCache is compatible with both Redis and Memcached. Boost your application performance and achieve microsecond latency by caching alongside your existing databases. ElastiCache is a popular choice for real-time use cases like caching, session stores, gaming, geo-spatial services, real-time analytics, and queuing.



### What is Elastic Beanstalk?

    Amazon Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. It is AWS equivalent of **heroku**

    beanstalk setups for you:
    1. Elastic Load Balancer 
    2. Autoscaling Groups 
    3. RDS Database 
    4. EC2 instance 
    5. Monitoring 
    6. Security




### What is aws global infrastructure?

    The aws global infrastructure is globally distributed hardware and datacenters that grouped together to act as a single large resource for end customer.

        1. Now all new services are first available in US-East and not all services are available in all regions
        2. Pricing vary from region to region 
        3. Each region has three availability zone.
        4. While some services are available global like cloudfront but for services like S3 bucket single region must be chosen( but it is global services), while EC2 is a regional service.

    Factor to consider while choosing zones:
    1. What regulatory Compliance does this region meet?
    2. What is the cost of AWS service in this region?
    3. What AWS services are available in this region?
    4. What is the distance or latency to my end user?

    Now What is Availability Zones?
    An availability zone is physical location made up of one or more datacenter.
    AZs are represented by a region code followed by a letter identifer, e.g. us-east-1a
    All AZs are in an AWS region are interconnected  with high-bandwidth, low-latency networking over gully redundant, dedicated metro fiber 

### Fault Tolerance

#### What is Fault Domain?
    A fault domain is a section of a network that is vulnerable to damage if critical device or system fails. the purpose of fault domain is that 


### Point of Prsence (PoP):

    PoP is an intermediate location between an AWS Region and end user.

### Tier-1 Network:
    is a network that can reach every other network on the internet without purchasing IP transit or paying for peering.

### AWS Global Accelerator:

    It provides optimal path from end user to your web server.It is deployed within edge locations so user send traffic to an Edge location instead of directly to your web app.


### Edge Computing:

    Edge computing is basically placing data loads and processing close to edge location to reduce latencty and bandwidth consumption

### AWS Config

    it is a policy as Code service. With this you can create rules to continuous check AWS resources config.

### AWS Ground Station:
    It is a fully managed service that let you control satellite communications, process data and scale your operations.

### AWS Outpost
    AWS Outposts is a fully managed service that offers the same AWS infrastructure, services for a truly hybrid experience.It is basically rack of servers running AWS infrastructure on your physical location.

### NVMe 
    NVMe (nonvolatile memory express) is a new storage access and transport protocol for flash and next-generation solid-state drives (SSDs) that delivers the highest throughput and fastest response times yet for all types of enterprise workloads.

### Elastic Load balancer

    A load balancer allows you to evenly distribute traffic to multiple servers in one or more datacenter. If one of the server bacome unavailable then load balancer shift traffic to available server.

### Auto Scaling Groups (ASG)

    It is an AWS feature that will automatically add or remove servers based on scaling rules you define based on metrics.

### RDS Multi-AZ 
    is when you run a duplicate standby database in another Availability Zone in case your primary database fails. Microsoft SQL Server and PostgreSQL are available on Amazon RDS.

### CloudEndure Disaster Recovery 
    It continuously replicates your machines into a low-cost staging area in your target AWS account and preferred Region enabling fast and reliable recovery.

### Backup and restore
    involves backing up your systems and restoring them from backup in case of disaster. 
 
### Pilot light
    involves running core services  in standby mode, and triggering additional services as needed in case of disaster.

### Amazon LightSail
    It is the managed virtual server service.

### Containers
    Virtualizing an operating system to run multiple workloads on a single OS instance.

### Elastic Container Service
        Amazon Elastic Container Service (ECS) is a cloud computing service in Amazon Web Services (AWS) that manages containers and lets developers run applications in the cloud without having to configure an environment for the code to run in.
### AWS KMS 
    allows you to create and manage encryption keys known as Customer Master Keys (CMKs). CMKs can be either symmetric keys used for encrypting and decrypting data or asymmetric keys used for digital signing and verification.

### IAM Policy Attributes
    Sid -> stands for statement ID, an optional field that lets the reader quickly identify what a statement does.
    Effect -> can be either allow or deny
    Action -> refers to what action are you trying to perform. Format is service:operation.
    Resource -> refers to which resource are you interacting with. Typically you'll use ARN (Amazon Resource Name) which uniquely identify AWS resources.
### Amazon Resource Names(ARNs)
    It Uniquely identify AWS resources.


### AWS Command line Interface

CLI allows users to programmatically interacts with AWS API via commands.It is a python executable program .

### infrastructure as Code
    It is blueprint of our infrastructure.It allows us to easily share,version or inventory our cloud infrastructure.
    So AWS has two offering for infrastructure as Code.(aws cloudFormation)


### The nitro system
    A combination of dedicated hardware and lightweight hypervisor enabling faster innovation and enhanced security


### AWS wavelength
    allows you to build and launch your application in a telecom datacenter.


### Types of storage services

#### Elastic block stores
    data is split into evenly split blocks directly accessed by the operating system

#### Elastic file storage
    file is stored with data and metadata.Multiple connections via a network share, support multiple read, writing locks the file.

#### S3


### S3 storage Classes


### AWS Snow Family
    They are storage and compute devices use to physically move data in or out of the cloud


### Server Message Block (SMB) protocol 
    is a network file sharing protocol that allows applications on a computer to read and write to files and to request services from server programs in a computer network.

### AWS Snow Family
    Process data at the edge and migrate data into and out of aws. 



### Document Store
    A document store is a NOSQL database that documents as its primary data structure. A document could be an XML or JSON.


### DynamoDB 
    Is a serverless NOSQL and document database. It is designed to scale to billions of records with guaranteed consistent data return in at least one second.


### DocumentDb 
    is a NOSQL document that is "MongoDB compatible".


### Keyspaces
    is a fully managed Apache Cassandra database. Cassandra is an open-source NOSQL key/value database similar to DynamoDB 


### Relational Database Service 
    is a relational database service that supports multiple SQL engines.

#### Aurora 
    is a fully managed database of either Mysql or PSQL database.

### RedShift 
    is a petabyteisze data-warehouse.Data-warehouses are for Online Analytical Processing. Data-warehouse can be expensive because they are keeping data "hot" meaning we can run a very complex query on large data and still get that data very fast.

### ElastiCache 
    is a managed database of the in-memory and caching open-source databases Redis or Memcached.

### Neptune 
    is a managed graph database. Data is represented as interconnected nodes.

### Amazon Timestreams 
    is a fully managed time series database. Think of devices that sends lots of data that are time-sensitive such as IOT devices.

### Quantum Ledger Database 
    is a fully managed ledger database that provides transparent, immutable and cryptographically 

### Cloud native Networking Services

### Virtual Private Cloud
    is a logically isolated section of the AWS Network where you launch your AWS resources.

### NACL(Network Access Control List)
    it acts as a firewall at the subnet level.we can allow or deny rules.

### Security groups
    Acts as a virtual firewall at the instance level.Implicity deny all traffic. We create only allow rules.
    With security group you cannot block a single Ip address

### Different Types of Instance Families
    1. General Purpose -> web servers and code repositories.
    2. Compute Optimized -> Scientific modeling, dedicated gaming servers and ad server engines
    3. Memory Optimized -> in-memory cache, in-memory database, real time bug data analytics
    4. Accelerated Optimized -> Machine learning, Computational finance 
    5. Storage Optimized -> NoSQL,in-memory database, data warehousing

#### AMi id is regional based 

### Target groups
    Target groups route requests to one or more registered targets, such as EC2 instances, using the protocol and port number that you specify.Each target group is used to route requests to one or more registered targets.

#### Public ip address get if we restart the server, we can handle it by elastic ip address

### EC2 pricing model
    1. On-demand
    2. Reserve -> Designed for applications that have a steady-state, predictable usage, or require reserved capacity.
    We can reduce price based on 4 attributes
        a. term: For how long you want to commit 1 year or 3 year.
        b. Class: The less flexible the greater the saving
        c. Payment options
        d .Reserved attributes -> Instance type: e.g. : m4.large, Region-> the region in which the reserved instance is purchased, 
                                                    Tenancy -> Whether your instance runs on shared or single-tenant hardware
                                                    platform-> The operating system eg. window or linux.

    3. Capacity Reservation -> is a service of EC2 that allows you to request a reserve of EC2 instance type for a specific region and AZ. 

    4. Spot instances -> idle servers

    5. Dedicated Instances -> designed to meet regulatory requirements

### Savings Plans
    There are three types of saving plans:
        1. Compute savings plan
        2. EC2 Instance savings plan
        3. Sagemaker savings plan

### AWS CloudTrail
    AWS CloudTrail is an auditing, compliance monitoring, and governance tool from Amazon Web Services (AWS). It’s classed as a “Management and Governance” toola in the AWS console.

    With CloudTrail, AWS account owners can ensure every API call made to every resource in their AWS account is recorded and written to a log. An API call can be made:

    when a resource is accessed from the AWS console
    when someone runs an AWS CLI command
    when a REST API call is made to an AWS resource
    These actions can be coming from:

    Human users (e.g. when someone spins-up an EC2 instance from the console)
    Applications (e.g. when a bash script calls an AWS CLI command)
    another AWS service (e.g. when a Lambda function writes to an S3 bucket)

### AWS GuardDuty
    GuardDuty secures workloads and data on AWS by leveraging both AWS-developed and industry-leading third-party sources. It integrates machine learning, anomaly detection, network monitoring, and the detection of dangerous files.

### AWS Detective
    provides you with security assessments of your applications’ settings and configurations

### Directory service
    A directory service maps the names of network resources to their network addresses

### Identity Provider
    An Identity Provider (IdP) serves as a centralized authentication system that enables users to access multiple applications and services with a single set of credentials.

### Single-sign on
    SSO is an authentication scheme that allows user to login with a single Id and password to different system and software.

### Lightweight Directory Access Protocol 
    is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory infor services over an IP. It allows same sign-on but user has to enter single ID and password evry time he logs in 

### IAM Policies
    written in JSON and contain the permission which determine what API actions are allowed or denied.

### ACL
    Control ownership of objects written to this bucket from other AWS accounts and the use of access control lists (ACLs). Object ownership determines who can specify access to objects.

### AWS Single Sign-On
    is where you create or connect your workforce identities in AWS once and manage access centrally across your AWS organisation.

### Messaging System
    Used to provide asynchronous communication and decouple processes via messages/events from sender and receiver.

### Queueing System
    Queueing system is messaging system that generally will delete messages once they are consumed.Simple communication. Not real-time. Have to pull. Not reactive.

### Simple Queueing Service 
    Fully managed queuing service that enables you to decouple and scale micorservices, distributed system and serverless application.

### Streaming
    Multiple consumers can react to events.Events live in the stream for long periods of time, so complex operations can be applied 

### Kinesis
    is the AWS fully managed solution for collecting, processing and analyzing streaming data in the cloud.

### SNS 
    is a highly available, durable, secure, fully  managed pub/sub messaging service that enables you to decouple microservices, distributed systems and serverless applications.With this we can only send plain text emails.

### State Machine 
    A state machine is an abstract model which decides how one state moves to another based on a series of conditions.Think of state machine as flow chart.

### Step Functions
    Coordinate multiple AWS services into a serverless workflow.It's a graphical console to visualize the components of your applications as a series of steps.

### EventBridge 
    is a serverless event bus that makes it easy to connect applications together from your own applications, third-party services and AWS services.

### Amazon MQ
    is a managed message broker service that uses Apache ActiveMQ

### Managed Kafka Service(MSK)
    is a fully managed Apache kafka service .It is an open-source platform for building real-time streaming data pipelines and applications.Similar to kinesis but more robust.

### Appsync 
    is afully managed GraphQL service. GraphQL is an open source agnostice query adaptor that allows you to query data from various data source.

### AWS Config
    provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.


### AWS Shield 
    is a managed DDoS protection service that safeguards applications running on AWS.AWS Shield Advanced provides expanded DDoS attack protection for web applications running on the following resources: Amazon Elastic Compute Cloud, Elastic Load Balancing (ELB), Amazon CloudFront, Amazon Route 53, AWS Global Accelerator.

### AWS Artifact
    provides on-demand downloads of AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI) reports, and Service Organization Control (SOC) reports.

### Web Application Firewall
    Protect your web applications from common exploits and bots that can affect availability, compromise security, or consume excessive resources.With AWS WAF, you can create security rules that control bot traffic and block common attack patterns such as SQL injection or cross-site scripting 

### EBS snapshot
    are a point-in-time copy of your data, and can be used to enable disaster recovery, migrate data across regions and accounts, and improve backup compliance.

### Redshift
    Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale.

### Snowball
     a service that provides secure, rugged devices, so you can bring AWS computing and storage capabilities to your edge environments, and transfer data into and out of AWS

### Amazon ElastiCache 
    is a fully managed, Redis- and Memcached-compatible service delivering real-time, cost-optimized performance for modern applications. ElastiCache scales to hundreds of millions of operations per second with microsecond response time, and offers enterprise-grade security and reliability.     

### AWS OpsWork
    is a configuration management service that also provides managed instances of the open-source configuration managed software chef and puppet

### AWS amplify
    a mobile and web application web framework that will provision multiple AWS services as your backend.

### AWS Apprunner
    A fully managed service that make it easy for developers to quickly deploy containerized web application

### AWS Control Tower
    helps Enterprises quickly set-up a secure, AWS multi-account. Provides us with a baseline-environment to get started with a multi-account architecture.

### Change Management 
    is the context of Cloud Infrastructure is when we have formal process to monitor changes, enforce changes and remediate changes

### Compliance as Code
    is when we utilize programming to automate the monitoring, enforcing and remediating chnages to stay compliant with a compliance programs or expected configurations

### Resource Groups 
    are collcetion of resources that share one or more tags.

### SageMaker
    SageMaker provides every developer and data scientist with the ability to build, train, and deploy machine learning models quickly. Amazon SageMaker is a fully-managed service that covers the entire machine learning workflow to label and prepare your data, choose an algorithm, train the model, tune and optimize it for deployment, make predictions, and take action.

### Augemented AI 
    Amazon Augmented AI (Amazon A2I) is a service that brings human review of ML predictions to all developers by removing the heavy lifting associated with building human review systems or managing large numbers of human reviewers.

##Machine Learning And AI services

### CodeGuru
    is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and offers suggestions for improving your Java and Python code.

### lex
    let you build voice and chat bot.

### Personlize
    is a real-time recommendation service.

### Polly
    is a text to speech service.Upload your text and audio file will be generated.

### Rekognition
    is a image and video recognition service.

### Transcribe 
    is a speech to text service.

### Textract

### Translate

### Comprehend

### Forecast
    time-series forecasting service. Forecast business outcomes such as produt demand, resource needs or financial performance.

### Elastic Inference
    allows you to attach low-cost GPU-powered acceleration 


### AWS amplify
    a mobile and web application web framework that will provision multiple AWS services as your backend.

### AWS Apprunner
    A fully managed service that make it easy for developers to quickly deploy containerized web application

### AWS Control Tower
    helps Enterprises quickly set-up a secure, AWS multi-account. Provides us with a baseline-environment to get started with a multi-account architecture.

### Change Management 
    is the context of Cloud Infrastructure is when we have formal process to monitor changes, enforce changes and remediate changes

### Compliance as Code
    is when we utilize programming to automate the monitoring, enforcing and remediating chnages to stay compliant with a compliance programs or expected configurations

### Resource Groups 
    are collcetion of resources that share one or more tags.

### SageMaker
    SageMaker provides every developer and data scientist with the ability to build, train, and deploy machine learning models quickly. Amazon SageMaker is a fully-managed service that covers the entire machine learning workflow to label and prepare your data, choose an algorithm, train the model, tune and optimize it for deployment, make predictions, and take action.

### Augemented AI 
    Amazon Augmented AI (Amazon A2I) is a service that brings human review of ML predictions to all developers by removing the heavy lifting associated with building human review systems or managing large numbers of human reviewers.

##Machine Learning And AI services

### CodeGuru
    is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and offers suggestions for improving your Java and Python code.

### lex
    let you build voice and chat bot.

### Personlize
    is a real-time recommendation service.

### Polly
    is a text to speech service.Upload your text and audio file will be generated.

### Rekognition
    is a image and video recognition service.

### Transcribe 
    is a speech to text service.

### Textract

### Translate

### Comprehend

### Forecast
    time-series forecasting service. Forecast business outcomes such as produt demand, resource needs or financial performance.

### Elastic Inference
    allows you to attach low-cost GPU-powered acceleration 

#### You can change aws support plan only through aws root account.

#### Consolidated billing allows you to pay for multiple aws account with one bill.

### AWS well-architected
    1. Operational Excellent Pillar -> Run and monitor systems
    2. Security Pillar -> Protect data and systems, mitigate risk
    3. Reliability Pillar -> Mitigate and recover from risk
    4. Performance Efficiency Pillar -> Use computing resource effectively
    5. Cost Optimization Pillar -> Get the lowest price

#### Operational Excellence Design Principles 
    1. Perform operations as code
    2. Make frequent, small, reversible changes
    3. Refine operations procedures frequently 
    4. Anticipate failure 
    5. Learn from all operational failures

#### Security Design Principles
    1. Implement a strong Identity foundation
    2. Enable traceability
    3. Apply security at all layers
    4. Automate security best practices
    5. Protect data in transit and at rest
    6. Keep people away from data
    7. Prepare for  

#### Reliablitiy Design Principles
    1. Automatically recover from failure 
    2. Test recovery procedures
    3. Scale horizontly to increase aggregate system availability
    4. Stop guessing capacity
    5. Manage change in automation

#### Performance Efficieny Design Principles
    1. Democratize Advance Technologies
    2. Go global in minutes
    3. Use serverless architecture
    4. Experiment more often
    5. Consider mechanical sympathy

#### Cost Optimization Design Principles
    Implement Cloud Financial management
    Adopt a Consumption Model
    Measure Overall efficiency
    Stop spending money on undifferentiated heavy lifting

### AWS Migration Evaluator 
    is an estimate toll used to determine an organisation existing on-premise cost so it can compare it against AWS cost for planned cloud migration.

### AWS Database Migration Service(DMS)
    allows you to quickly and securely migrate one database to another. 

### Cryptography
    The practice and study of techniques for secure communication in the presence of third parties called adversaries.

### Cypher 
    algorithm that performs encryption and decryption

### ciphertext
    is the result of encription performed on plaintext via an algorithm

### code signing
    When you use a digital signature to ensure computer code has not been tampered.

### Encription in Transit
    Data that is secure when moving between locations. Algorithm : TLS, SSL.
    1. TLS -> An encription protocol for data integrity between two or more communicating computer applicaton.
    2. Secure Socket Layers -> An encription protocol for data integrity between two or more communicating computer application


### Encription At Rest 
    Data that is secure when residing on storage or within a database. Algorithm: AES, RSA

### AWS Artifact 
    is a self-service portal for on demand access to AWS complaince reports.

### Hardening
    The act of eliminating as many security risks as possible. Hardening is common for virtual Machines where you run a collection checks known as a security benchmark.

### AWS inspector
    runs a security benchmark against specific EC2 instances. You can run a variety of security benchmarks.Can perform both Network and Host assessments.

### AWS Shield
    is a managed DDos protection service that safeguards applications running on AWS.It protects you against Layer 3, 4 and 7 attacks
    layer 7 -> Application, Layer 4 -> Transport and Layer 3 -> Network

### IDS(Intrution Detection System)
    A device or software application that monitors a network or systems for malicious activity or policy violations

### AWS Guard Duty
    is a threat detection service that continuously monitors for malicious, suspicious activity and unauthorized behaviour. It uses Machine Learning to analyze the Cloudtrail logs, VSC logs and DNS logs.

### Amazon Macie
    is a fully managed service that continuously monitors S3 data access activity for anamolies and generates detailed alerts when it detects risk of unauthorized access or inadvertent data leaks.

### AWS WAF
    Web application Firewall protect your web applications from common web exploits.

### Hardware Security Module
    It's a piece of hardware designed to store encryption keys. HSM holds keys in memory and never write them to disk.
    
### KMS
    is am managed service that makes it easy for to create and control encryption keys used to encrypt data.

### Cloud HSM
    is a sinel tenant HSM as a Service that automates hardware provisioning, software patching, high availablity and backups.

### AWS Config
    is a governance tool for compliance as Code. WIth this you can create rules to check if resourcesa are configured as you want them to be.

### AWS Appconfig
    is use to automate the process of deploying application configuration variable changes to your web-application. with the help of it you can write a validator to ensure changed variable doesnot break your web-app.

### SES
    Emails that should be triggered ased on in app action. With this we can send html email and can set email template

### Amazon Pinpoint
    Emails for marketing

### Storage Gateway
    AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage.

### AWS Elastic File System
    Amazon EFS is a simple, serverless, elastic, set-and-forget file system that automatically grows and shrinks as you add and remove files with no need for management or provisioning. You can use Amazon EFS with Amazon EC2, AWS Lambda, Amazon ECS, Amazon EKS and other AWS compute instances, or with on-premises servers.Allows for file sharing between multiple Amazon EC2 instances. Amazon EFS supports two forms of encryption for file systems, encryption of data in transit and encryption at rest. This is an optional feature and has to be enabled by user if needed.


Amazon EC2 Dedicated Hosts allow you to use your eligible software licenses from vendors such as Microsoft and Oracle on Amazon EC2, so that you get the flexibility and cost effectiveness of using your own licenses, but with the resiliency, simplicity and elasticity of AWS. An Amazon EC2 Dedicated Host is a physical server fully dedicated for your use, so you can help address corporate compliance requirements.

#### Compute service
    1. EC2
    2. ECS
    3. Lambda
    4. Lightsail
    5. Nitro system
    6. AWS Batch

### AWS Batch
    AWS Batch enables you to run batch computing workloads on the AWS Cloud. Batch computing is a common way for developers, scientists, and engineers to access large amounts of compute resources. AWS Batch removes the undifferentiated heavy lifting of configuring and managing the required infrastructure.

### Amazon Aurora:
    provides automated backups of data by default.It is a relational database compatible with MySQL and PostgreSQL.

### Amazon Cognito
     helps you implement customer identity and access management (CIAM) into your web and mobile applications.

### ElastiCache
    in-memory data store service    


    AWS has the concept of a Region, which is a physical location around the world where we cluster data centers. We call each group of logical data centers an Availability Zone. Each AWS Region consists of multiple, isolated, and physically separate AZ's within a geographic area. Unlike other cloud providers, who often define a region as a single data center, the multiple AZ design of every AWS Region offers advantages for customers. Each AZ has independent power, cooling, and physical security and is connected via redundant, ultra-low-latency networks. AWS customers focused on high availability can design their applications to run in multiple AZ's to achieve even greater fault-tolerance. AWS infrastructure Regions meet the highest levels of security, compliance, and data protection.

### AWS Direct Connect 
    is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. AWS Direct Connect lets you establish a dedicated network connection between your network and one of the AWS Direct Connect locations.

### virtual private gateway 
    is a logical, fully redundant distributed edge routing function that sits at the edge of your VPC. As it is capable of terminating VPN connections from your on-prem or customer environments, the VPG is the VPN concentrator on the Amazon side of the Site-to-Site VPN connection.

### Amazon Virtual Private Cloud (Amazon VPC) 
    lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including the selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications. A VPC can span all Availability Zones within an AWS Region.

### Identities 
    are the IAM resource objects that are used to identify and group. You can attach a policy to an IAM identity. These include users, groups, and roles.

### Resources 
    are the user, group, role, policy, and identity provider objects that are stored in IAM. As with other AWS services, you can add, edit, and remove resources from IAM.

### network access control list (NACL)
    is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups to add an additional layer of security to your VPC.

With the IAM policy simulator, you can test and troubleshoot identity-based policies, IAM permissions boundaries, Organizations service control policies, and resource-based policies.

### IAM entities 
    are the users (IAM users and federated users) and roles that are created and used for authentication.

### Amazon Route 53 
    is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost-effective way to route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect. Amazon Route 53 is fully compliant with IPv6 as well.

### S3 Lifecycle Policy
    ou can add rules in an S3 Lifecycle configuration to tell Amazon S3 to transition objects to another Amazon S3 storage class. For example:

    When you know that objects are infrequently accessed, you might transition them to the S3 Standard-IA storage class.

    You might want to archive objects that you don't need to access in real time to the S3 Glacier storage class.

### AWS CodePipeline 
    is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This enables you to rapidly and reliably deliver features and updates. 

### AWS CloudFormation 
    provides a common language for you to model and provision AWS and third-party application resources in your cloud environment. AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts.

### AWS Systems Manager 
    gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user interface so you can view operational data from multiple AWS services and allows you to automate operational tasks across your AWS resources.

### Application Load Balancer 
    is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers.

### internet gateway 
    is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. An internet gateway serves two purposes: to provide a target in your VPC route tables for internet-routable traffic, and to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.

### AWS Trusted Advisor 
    is an online tool that provides you real-time guidance to help you provision your resources following AWS best practices. Trusted Advisor checks help optimize your AWS infrastructure, increase security and performance, reduce your overall costs, and monitor service limits. Whether establishing new workflows, developing applications, or as part of ongoing improvement, take advantage of the recommendations provided by Trusted Advisor on a regular basis to help keep your solutions provisioned optimally.

### Amazon Simple Queue Service (SQS)
    is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.


### An IAM role 
    is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

You must provide your AWS access keys to make programmatic calls to AWS or to use the AWS Command Line Interface or AWS Tools for PowerShell.

When you create your access keys, you create the access key ID (for example, AKIAIOSFODNN7EXAMPLE) and secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY) as a set. The secret access key is available for download only when you create it. If you don't download your secret access key or if you lose it, you must create a new one.

### AWS X-Ray 
    provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components. You can use X-Ray to analyze from simple three-tier applications to complex microservices applications consisting of thousands of services

AWS Infrastructure Event Management is a structured program available to Enterprise support customers (and Business Support customers for an additional fee) that helps you plan for large-scale events, such as product or application launches, infrastructure migrations, and marketing events.
With Infrastructure Event Management, you get strategic planning assistance before your event, as well as real-time support during these moments that matter most for your business.

The Business Plan is the cheapest plan that will still provide the full set of Trusted Advisor checks.

### Amazon Elastic Container Registry (Amazon ECR)
    can be used to store, manage, and deploy Docker container images. Amazon Elastic Container Registry (Amazon ECR) eliminates the need to operate your container repositories. You can then pull your docker images from Amazon Elastic Container Registry (Amazon ECR) and run those on Amazon Elastic Container Service (Amazon ECS).


### AWS Global Accelerator
    is a service that improves the availability and performance of your applications with local or global users. It provides static IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers, or Amazon EC2 instances. AWS Global Accelerator uses the AWS global network to optimize the path from your users to your applications, improving the performance of your traffic by as much as 60%.

    AWS Global Accelerator improves performance for a wide range of applications over TCP or UDP by proxying packets at the edge to applications running in one or more AWS Regions. AWS Global Accelerator is a good fit for non-HTTP use cases, such as gaming (UDP), IoT (MQTT), or Voice over IP, as well as for HTTP use cases that specifically require static IP addresses or deterministic, fast regional failover.