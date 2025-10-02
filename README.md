
# Leopard-Low-Down
This is the website for the Leopard Low Down, a newspaper run for NHISD.

## Automated Publishing Workflow

### For Publishers (Setup Only)
1. Make sure you have Python and PyInstaller installed.
2. Build the publishing tool:
	 ```
	 pip install pyinstaller
	 pyinstaller --onefile publish_article.py
	 ```
3. Distribute the resulting `publish_article.exe` (found in the `dist` folder) to your users along with the project files.

### For Users (Article Publishers)
- **You only need to have [git](https://git-scm.com/downloads) installed.**
- No need to install Python or any other tools.
- When you finish an article in the admin page, it will save all files and a `publish_config.json` file.
- To publish:
	1. Double-click `publish_article.exe` in your project folder.
	2. The tool will automatically add, commit, and push the new/changed files to GitHub.

**Note:** If you see any errors, make sure you are running the `.exe` in the correct folder (where the files and `publish_config.json` are located) and that git is installed and available in your system PATH.
