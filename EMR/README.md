# EMR - Elastic MapReduce

**MapReduce**: A programming model for processing large amounts of data in bulk across multiple machines based on the map ("collect") function and reduced ("fold" or "inject") function.

![EMR Components](/images/emr_components.png)


## EMR Components

**Cluster**: A cluster is simply collection of EC2 instances called Nodes. Based on the nodes role, they are categorized in three types. Master, Core and Task Node.

**Master Node**: Manages & monitors the cluster, coordinates the distribution of data and tasks among other nodes. It also tracks the status of tasks.

**Core Node**: Nodes that hold data and execute tasks.

**Task Node**: Provides extra compute power. Does not hold any data.

## EMR Architecture

Amazon EMR service architecture is comprised of four basic layers.

**1. Storage Layer**

AWS provides three option while deciding on storage layer:

    - HDFS using EBS (hdfs://master-ip-address/path-to-data)
    - EMRFS using S3 (s3://bucket-name/path-to-file-in-bucket)
    - HDFS using Instance store

**2. Resource Management**

EMR by default uses YARN as resource manager. With recent release EMR also supports running workload on Kubernetes.

**3. Data Processing Framework**

EMR out-of-the-box supports Hadoop, Spark and Presto framework.

**4. Application Frameworks**:

EMR supports applications like Spark streaming, Hive, Hbase, Presto, Flink, Pig.

## Cluster States

EMR cluster transitions between multiple states during its lifecycle. Below is a diagram that list all of those states and their soft lineage. 

![EMR Cluster Steps](/images/emr_cluster_steps.png)

1. When we create initiate a cluster creation, it enters the STARTING state. In this state AWS EMR service provisions EC2 instance groups based on the hardware configuration we supply.

2. One EC2 instance are provisioned, BOOTSTRAPPING state kicks in. In this state any scripts that we supply, is execute on the instance.
— bootstrap-actions Path=”s3://mybucket/filename”,Args=[arg1,arg2]
[{‘classification’: ‘<conf-type>’,’Properties’: {‘key’: ‘value’}}]

3. After executing the scripts the EMR service installs the applications that we chose to run on the cluster.

4. After all the applications are installed, cluster enters WAITING state. In this state cluster is waiting for any Step that needs to be executed.

5. Once we submit a job or task to the cluster, the state transitions to RUNNING. In this step cluster run any job that we have submitted.

6. Once all the tasks are complete, the cluster either may return back to waiting state or can go to TERMINATING state. In this state EMR removes instances.

7. Depending upon the reason of termination the final state may be TERMINATED or TERMINATED WITH ERROR state.