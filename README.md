# Logger
Simple Python logging module

**Usage:**\
**Import the module**\
```import logger```

**Create a new object of the Logger class (fileLocation/fileName)**\
```errorLogs = logger.Logger("errorLogFile.log")```

**Log messages using the LogMessage method (messageCode, messageType, messageDetails)**\
```errorLogs.LogMessage("404", "Error", "Resource not found")```

**Clear the log file using the clear method**\
```errorLogs.Clear()```

As I use the module in my own projects I will be testing out this script and updating and debugging any issues that it may have.\
I'm not the most experienced python dev, so bare with me :)
