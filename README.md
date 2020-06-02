# NetworkHostTracking
To track IP addresses/subnets in a LAN network made up of Cisco IOS devices, routers and switches.
Apart from mapping IP addresses to which ports we can also run show commands which will be given
by the user against these ports.

## Use Case Description.
1) We can use the project in cases where the LAN network is made up of Cisco IOS router and switches
and we want to quickly track a couple of IP addresses on the network.
2) At times during network troubleshooting we want know what is common between different IP address that
are facing let say network latency, if tracking them results that all of them are connected to the same
switch we can quickly narrow down the problem.
3) We can also run show commands against the tracked ports, which means that in cases we want to gather
configuration or operational details of these ports, this project will be able to assist you.
4) All the reports this project generates are displayed on the browser and we can download the same as a
CSV file.

## Installation.
Since I have used Docker the installation in pretty easy:
1) Clone the repo on your server running Docker Engine.
2) Change directory into the repo folder.
3) docker-compose up --build

## How to use the repo.
I have used Flask for the Frontend of this project so all the user operation will be performed from the
browser window.
1) You will to begin with uploading an inventory file, a sample inventory file is already present with the
project which you can download using the browser, modify it and upload is back to the server.
2) After uploading the inventory file, you need to perform the Mandatory operations which is Loading data.
3) Once the data has been loaded from the network you can start tracking network IP addresses or subnets.
4) In case you want to load new network data present on server, you can Load Data again and all the previous
data will be deleted and new data will be populated.
5) To modify the inventory file in order to add, delete or modify network devices, you will have to follow
the steps mentioned in point one.


## Getting Help.
If you have any issues with the project, please feel to reach out to me.

## Test.
Test case results will be uploaded to the Repo.

## Features to be worked on in the future.
1) Integrating Databases.
2) A better way to hand device login details.
3) Integrating topology builder.