### What is cloud?

Cloud is just a metaphorical term for the internet, where computing resources such as servers, storage, and applications are made available to users over the internet, on demand and as a service.

Now cloud computing has two types of models 
1. deployment model-> There are three types of deployment models -> public, private and hybrid.
2. Service model -> There are three types of service models -> IAAS(Infra-structure as a service), PAAS(Platform as a service), SAAS( Software as a Service).

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