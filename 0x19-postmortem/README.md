# Summery:
MySQL Replica stopped replicating data from the source(master) server database starting from December 18, 2024, 06:30 PM - December 23, 2024 07:30 AM GMT+3. It decreased the read speed from the server leaving it vulnerable for potential data loss.

## Timeline
I discovered the issue accidentally on January 20, 2024, 08:00 AM GMT+3, while I was monitoring the slave database. After finding out the issue, I tried to fix the replication by restarting it, but it was not successful

## Root cause
This issue was caused due to improper installation and configuration of the Master-Slave replication. It has been fixed by reinstalling and re-configuring the the replication as follows:
## Installing MySQL and configuring the slave-database.
Dumping the data from the master(slave) server, copying to the slave server, restoring the data to the slave-database.
Starting the replication
Verifying the replication

