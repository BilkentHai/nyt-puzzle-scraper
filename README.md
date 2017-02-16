# nyt-puzzle-scraper

Scrapes NY Times Mini Crosswords puzzle everyday through AWS Lambda & its cron.

### Setup & Deployment

1. Create connection_string file on root directory with string like `mongodb://<dbuser>:<dbpassword>@ds153239.mlab.com:53239/huseyin`
2. `pip install -t ./ -r requirements.txt`
3. `serverless deploy`


Note: DB & collection names can be changed on main.py.