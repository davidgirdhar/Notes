#### AWS Elastic Block Store
EBS is Amazon’s block-level storage solution used with the EC2 cloud service to store persistent data. This means that the data is kept on the AWS EBS servers even when the EC2 instances are shut down. EBS offers the same high availability and low-latency performance within the selected availability zone, allowing users to scale storage capacity at low subscription-based pricing model. The data volumes can be dynamically attached, detached and scaled with any EC2 instance, just like a physical block storage drive. As a highly dependable cloud service, the EBS offering guarantees 99.999% availability.
The AWS EBS offers the following storage volume options:

* General Purpose SSD (gp2): An optimum balance between cost and performance for a variety of IT workloads. Use cases include virtual desktops, apps, dev and test environments, among others.
* Provisioned IOPS SSD (io1): The high-performance functionality serves particularly well for mission-critical IT workloads. Suitable use cases include large databases and business apps that require 16,000 IOPS or 250 MiB/s of throughput per volume.
* Throughput Optimized HDD (st1): A low cost alternative for large storage volume workloads with high performance throughput requirements. Examples include streaming workloads, big data applications, log processing and data warehousing.
* Cold HDD (sc1): An inexpensive alternative for use cases with a requirement to maintain minimal cost for large volume data storage. Examples include workloads that are accessed less frequently.

From the platform, you can configure backup and recovery options for your data:

EBS replication — EBS automatically replicates volumes within an Availability Zone (AZ). If something happens to the volume, you’ll have a copy to recover.
AWS backup — this is a paid service offered by AWS, for an additional price.
EBS snapshots — point-in-time versions of your data that serve as incremental backups. You can learn more about EBS snapshots here.

What Is an EBS Volume?


