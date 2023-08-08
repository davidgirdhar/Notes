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

    S3 stands for Simple Storage Service.It is easy to use with a simple web services interface to store and retrieve any amount of data from anywhere on the web.It is Object-based storage, i.e., you can store the images, word files, pdf files, etc.Files are stored in Bucket. A bucket is like a folder available in S3 that stores the files.Buckets are the containers in S3 that stores the data.


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
    is when you run a duplicate standby database in another Availability Zone in case your primary database fails.

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
    is a highly available, durable, secure, fully  managed pub/sub messaging service that enables you to decouple microservices, distributed systems and serverless applications.

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
    is a managed DDoS protection service that safeguards applications running on AWS.

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

