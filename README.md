# PMHF-Inc
Performing Asset analysis using free sources of online data
===========================================================

Steps to setup Python for Windows to get started using YahooFinance

1. Download the latest version of Python, make a note on where it’s saved to in your hard drive or just redirect it to the highest level of your hard drive: https://www.python.org/downloads/

2. Once it’s installed, since you’ll most likely be using it through the Command Prompt (accessed via pressing Windows Key + R > type “cmd” > press Enter), move the downloaded Python folder from its default location to the highest level of your hard drive instead, so that it’s easy to use the “cd” command to redirect to Python so you can start executing within it directly

3. Once the Python folder is in the simplest directory to access, double-click the “python.exe” file which is the Python Interpreter. This allows simple code testing and makes testing Statements easy as it doesn’t require a Compiler the way many other languages do. Pin this to your Taskbar for easy access

4. Follow the instructions within https://github.com/JECSand/yahoofinancials to download YahooFinancials (you don’t need to download from the GitHub browser directly, and this also requires you to download beautifulsoup4 and pytz). I had some trouble here, but in your Command Prompt try typing the following, pressing Enter after each:

    cd C:\ python

    python -m pip install yahoofinancials

You should see text in the Command Prompt saying that all three (beautifulsoup4, pytz, and yahoofinancials) have installed. You can then check the “Lib” folder within your Python folder to see that the BeautifulSoup and Pytz folders, as well as the YahooFinancials module file, have downloaded.

5. Once everything’s installed, you can write your programming scripts in Notepad++ and save them within the Python folder to easily test/execute them, though long-term it’s better to save them in a separate folder within your top level hard drive (as Python folder updates/downloads can delete/corrupt your program files), mine’s just called “code”.

6. To execute python program/module files outside the main Python folder while you’re in the Python Interpreter, you need to import the ‘os’ module which gives you the commands needed. Below is an example with results, and you press Enter after typing each >>> command below (it’s also possible to re-route the default Python directory route to be “code” and avoid this, but I haven’t done that yet):

'>>> import os

'>>> os.getcwd()

'C:\\Python'

'>>> os.chdir('C:\\code')

'>>> os.getcwd()

'C:\\code'

'>>> exec(open('script1.py').read())

7. The last command is what allows you to actually run a .py script you’ve saved in your “code” folder, or any folder you’re currently pointed to in the Python Interpreter.


Git Commands
============
**To set you home path in git bash follow the below steps**
1. open git bash and run echo $HOME
2. setx HOME "C:\pmhf-project\pmhf-inc"
3. close and reopen git bash and run echo again

git pull :: gets the latest copy from remote

git checkout -b :: use -b to create a new branch and then checkout the new branch

git add :: adds new files

git commit -a -m :: creates a commit | -a adds all changes | -m "insert comment within quotes"

git push origin [branchname] :: pushes to github

git merge ::
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging


Markdown Documentation
----------------------
https://www.markdownguide.org/basic-syntax/