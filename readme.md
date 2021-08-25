version control:
##### v0.6b - Edward variant
- This is assume you have your python environment installed and ready to use  
- Install dependencies : `pip install newspaper3k`
- File changes:
	- ADD gspider6b.py
	- REPLACE items.py
	- REPLACE settings.py
- latest commant line:
`scrapy crawl gnews6b -a query=semiconductor -a start=1/1/2020 -a end=1/31/2020 -a region=china -o hello06b.csv`


##### v0.6a - YM variant
- This is assume you have your python environment installed and ready to use  
- File changes:
	- ADD gspider6a.py
	- REPLACE items.py
	- REPLACE settings.py
- introduce excerpt2, excerpt3, and excerp4 -> this is launched for comparison purpose only, only 1 will remains after tested
- drop old region filter from the command line and replace with the new region filter (for testing also)
- latest commant line:
`scrapy crawl gnews6a -a query=semiconductor -a start=1/1/2020 -a end=1/31/2020 -a region=china -o hello26b.csv`

what can be placed under region:
country (i.e. China, japan, russia, south+korea, united+states, etc)  **or**
region (i.e. asia, europe, north+america, etc)

<hr>

##### v0.6   
- File changes:
	- ADD gspider6.py
- allow extract using crawl within crawl from googlenews website
- allow conditional to do crawl within crawl on request only  
`scrapy crawl gnews4 -a query=semiconductor -a start=1/1/2020 -a end=1/31/2020 -a region=US -o hello24.csv`

<hr>

##### v0.5  
- Crawl result is now sent to mySQL database
- 3 files has been updated:
	- REPLACE googlenews/googlenews/items.py
	- REPLACE googlenews/googlenews/settings.py
	- REPLACE googlenews/googlenews/pipelines.py

- All date format on the result is changed to YYYY-MM-DD to comply with mySQL date format. Hence YM code on items.py is adjusted to convert date into accepted date format by mySQL
- Latest command line:
scrapy crawl gnews3 -a query=semiconductor -a start=1/1/2020 -a end=1/31/2020 -a region=US

<hr>

##### v0.4a
- 3 files has been updated: 
	- ADD googlenews/googlenews/spiders/gspider3.py
	- REPLACE googlenews/googlenews/items.py
	- REPLACE googlenews/googlenews/settings.py

- Convert YM code into item loader and incorporate his date function via item loader
- Add link column, to stay true to our old rss crawler
- Rearrange the column so it's now will be : start,end,query,region,title,excerpt,date,source,link (let me know if there is better arrangement)

v0.4
v0.3a
v0.3
v0.2a
v0.2
v0.1
<hr>

1) Fork Edward’s Github 
2) Test the script 
3) Run the script to make sure it works 
4) Check Search engine search number corresponds with CSV download 
5) Tweak different keywords to test


	Open integrated Terminal from main googlenews folder
	Type the following:
source .env/scripts/activate

	You may encounter the following problem
 

<h1 align="center">How to Webcrawl?</h1>

## Installing and run in VSC <br>
Step 1: Download the zip file from Edward's Github.<br>

Step 2: Open VSC, open the downloaded folder.<br>

Step 3: Go to `googlenews` folder, right click and choose 'open in integrated terminal' <br>
*Note: Make sure 'googlenews' is the root directory.*<br>

Step 4: Ensure that you choose `command prompt` in Terminal. <br>
*Note: It doesn't work on Powershell, Bash etc.*<br>

Step 5: Type the following `source .env/scripts/activate` for macOS OR `cd .env/scripts` follow with `activate` on Windows.<br>

Step 6: Type `cd..`<br>

*Note: After this step, the directory WILL end with '.env' .. It should look like this: 'C:\Users\Cindy\Desktop\googlenews-scrapy-main.env'* <br>

Step 7: Type `cd..` <br>

*Note: After this step, the directory WILL NOT end with '.env' .. It should look like this: 	'C:\Users\Cindy\Desktop\googlenews-scrapy-main'* <br>

Step 8: Type `cd googlenews`. <br>

Step 9: Install scrapy by typing `pip install scrapy` <br>

*Note: If you are prompted with “pip not recognised as internal or external command” , you need to quit your VSC. Go to ‘File’ tab > ‘Close folder’ > ‘Close Window’. Relaunch VSC again > Go to Step 2 and continue.* <br>
 
Step 10: Try to run the the crawler by typing `scrapy crawl gnews`.<br>

Step 11: Create a CSV file by typing `scrapy crawl gnews3 -a query=semiconductor -a start=1/1/2020 -a end=1/31/2020 -a region=GB -o hello22.csv` where you can change the 'filename' into what you want. By running this step, web crawling begins and the web crawling results will be stored into this CSV file. <br>

        



