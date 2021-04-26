# Airflow Components

![Airflow Components](/images/airflow_comp.png)

**Scheduler** Orchestrates the execution of jobs on a trigger or schedule. The Scheduler chooses how to prioritize the running and execution of tasks within the system.

**Worker Queue** is used by scheduler in most Airflow installations to deliver tasks that need to be run to the Workers.

**Worker** processes execute the operations defined in each DAG. In most Airflow installations, workers pull from work queue when it is ready to process a task. When the worker completes the execution of the task, it will attempt to process more work from the work queue until there is no further work remaining. When work in the queue arrives, the worker will begin to process it. In multi-node airflow architecture, daemon processes are distributed across all worker nodes. The web server and scheduler are installed at the master node, and workers would be installed at each different worker nodes. To this mode of architecture, Airflow has to be configured with CeleryExecutor.

**Database** saves credentials, connections, history, and configuration. The database, often referred to as the metadata database, also stores the state of all tasks in the system. Airflow components interact with the database with the Python ORM, SQLAlchemy.

**Web Interface** provides a control dashboard for users and maintainers. The web interface is built using the Flask web-development micro-framework.


![Airflow Example](/images/airflow_example.png)