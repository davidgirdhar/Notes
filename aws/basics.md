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

    Amazon Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.


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
    involves running core services in standby mode, and triggering additional services as needed in case of disaster.

### Amazon LightSail
    It is the managed virtual server service.

### Containers
    Virtualizing an operating system to run multiple workloads on a single OS instance.

### Elastic Container Service
        Amazon Elastic Container Service (ECS) is a cloud computing service in Amazon Web Services (AWS) that manages containers and lets developers run applications in the cloud without having to configure an environment for the code to run in.
### AWS KMS 
    allows you to create and manage encryption keys known as Customer Master Keys (CMKs). CMKs can be either symmetric keys used for encrypting and decrypting data or asymmetric keys used for digital signing and verification.
