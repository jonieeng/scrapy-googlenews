1) Fork Edward’s Github 
2) Test the script 
3) Run the script to make sure it works 
4) Check Search engine search number corresponds with CSV download 
5) Tweak different keywords to test





	Open integrated Terminal from main googlenews folder
	Type the following:
source .env/scripts/activate

	You may encounter the following problem
 

HOW TO WEBCRAWL 
Installing and run in VSC 
 
Step 1: Download the zip file from Edward's Github (costhin/googlenews-scrapy) 
 
Step 2: Open VSC, open the downloaded folder 
 
Step 3: Go to googlenews folder, right click and choose 'open in integrated terminal'  
Note: Make sure 'googlenews' is the root directory 
 
 
Step 4: Ensure that you choose command prompt in Terminal.  
Note: It doesn't work on Powershell, Bash etc 
 
Step 5: Type the following source .env/scripts/activate for macOS or  
cd .env/scripts follow with activate on Windows 
 
Step 6: Type cd.. 
Note: After this step, the directory WILL end with '.env' .. It should look like this:  'C:\Users\Cindy\Desktop\Scrapy.env' 
 
Step 7: Type cd.. 
Note: After this step, the directory WILL NOT end with '.env' .. It should look like this:  'C:\Users\Cindy\Desktop\Scrapy’ 
 
Step 8: Type cd googlenews  
 
Step 9: Try to run the crawler by typing scrapy crawl gnews  
 
Step 10: Create a CSV file by typing scrapy crawl gnews -o filename.csv where you can     change the 'filename' into what you want. By running this step, web crawling begins     and the web crawling results will be stored into this CSV file 

        



