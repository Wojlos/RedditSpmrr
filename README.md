# RedditSpmrr

## Requirements

 - python3 (https://phoenixnap.com/kb/how-to-install-python-3-windows)
 - reddit account 

## Script setup:

  1. Clone this repository ( push the green ***Code*** button, and select ***Download ZIP*** )
  2. Unzip the files in folder of your chooseing  
  3. Open folder with script files in comand prompt (cmd) (https://www.wikihow.com/Open-a-Folder-in-Cmd)
  4. Type `pip install praw` and pres enter

## Secrets setup:
 #### We will be following this `https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/` instruction, You can start with point 2 and skipp the first part of point 3 (the code is already posted in this script)
 
  1. Enter `secrets.json` and fill the empty fields to get ***client_id*** and ***client_secret*** follow point 2 of this instruction: 
  `https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/`
  3. While in the folder with application, enter command `python refreshtoken.py`
  4. When prompted paste your ***client_id*** and ***client_secret***, and ***all*** when asked for the list of scopes
  5. Go to `http://localhost:8080` url in your browser and loggin
  6. Copy refresh token and post it in correct field

## Using the script

  1. Enter `subs` file with notepad
  2. Delete example subreddits, 
  3. Paste your subreddits list exactly like the examples (name, new line, name, new line ...) It is very important
  4. Save and exit the notepad file
  5. While your command prompt is open in the folder with `refreshtoken.py` file enter the comand `python refreshtoken.py` and press enter
  6. Wait for the script to finish 
  7. Check the `leftovers` file, it will contain all the subreddits that the script could not post too and the error logs that it has received.
