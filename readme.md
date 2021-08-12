This readme is originally made by [Hiroshi](https://github.com/GithubHM1) with some revision

1)	Fork this repository
    - Download using ZIP function and then install the files onto your desktop
    - Open files using VScode
    - Look for main googlenews folder in VScode
    - Open integrated terminal by right clicking the googlenews folder at the root
    - Type the following `source .env/scripts/activate` for macOS or `cd .env/scripts` follow with `activate` on Windows
    - Type `cd googlenews` to go into googlenews folder inside the googlenews in the root
    - Try to run the the crawler by typing `scrapy crawl gnews`
        - If you encounter this problem: 
        > Import "scrapy could not be resolved Pylance(reportMissinhImports) [1,8]
        - Install scrapy by typing `pip install scrapy`
        - Run scrapy again by typing `scrapy crawl gnews` or if you want to save to a csv file type `scrapy crawl gnews -o filename.csv` where you cna change filename into other filename that you prefer.
2) Test the script 
3) Run the script to make sure it works 
4) Check Search engine search number corresponds with CSV download 
5) Tweak different keywords to test
        



