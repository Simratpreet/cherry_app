## Cherry Web App
The application is built on flask framework and shows daily bhav data from BSE

#### Installation
1. Install all the python packages in a virtual environment using pip install -r requirements.txt
2. Install a crontab in the system to get daily BSE bhav data

#### Working Application
http://cherry-app-dev.us-east-2.elasticbeanstalk.com/

#### Infrastructure and Deployment
1. The application is deployed on AWS Elastic Beanstalk 
2. It uses Redis Database hosted on Redis Labs
3. The application is built on AWS EC2 instance

#### Code Explanation
1. bhav_csv_generator.py
  * This file is run once daily using cron job at 8PM IST.
  * It downloads daily BSE bhav data using BeautifulSoup library and saves it on a specified location
  * The csv file is read using pandas and converted to msgpack object to write to Redis database
  
2. application.py
  * This file contains one endpoint showing the BSE data
  * The data is read into pandas dataframe and dumped to json for usage of the UI
  
3. constants.py
  * It contains all the setting parameters
