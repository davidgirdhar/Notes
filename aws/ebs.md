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
An EBS volume is a device that works like a hard drive. You can use EBS volumes for creating file systems, storing databases, or running applications.


How to Create a New (Empty) EBS Volume via the Amazon EC2 Console

1. Go to the Amazon EC2 console.
2. Locate the navigation bar, then select a Region.
Region selection is critical. An EBS volume is restricted to its Availability Zone (AZ). That means you won’t be able to move the volume, or attach it to an instance from another AZ. Additionally, each region is priced differently. So do this wisely, and choose in advance prior to initiating the volume.

3. Go to the navigation pane, and then choose ELASTIC BLOCK STORE, Volumes.

4. Click on Create Volume.

5. Choose a Volume Type

If you know what you’re doing, and you know which volume you need, this is where you can choose the volume type of your choice. If you’re not sure what type you need, or if you’re just experimenting, go with the default option (which is set to gp2, as explained above).

6. Choose a Volume Size
7. Choose an Availability Zone. Keep in mind that you can attach EBS volumes only to EC2 instances located in the same AZ.

8. EBS volumes are not encrypted automatically. If you want to do that, now is the time.

For EBS encryption, choose Encrypt this volume, then choose default CMK for EBS encryption. This type of encryption is offered at no additional cost.

For customized encryption, choose Encrypt this volume, then choose a different CMK from Master Key. Note that this is a paid service and you’ll be charged with additional costs.

9. Tag your volume. This is not a must, and you’ll be able to initiate your EBS volume without tagging it. However, tagging can make your process much more efficient, and even save you money. By creating an organized system of tags, you can keep track of your volumes, and make sure that you’re not overspending. Here’s how to tag:

Choose Create additional tags. Provide a tag key and a tag value for each tag.

10. Choose Create Volume.

That’s it! You now have a new empty EBS volume. You can now use it to store data, or attach the volume to an EC2 instance.
