# Logger by Drew
#
# Simple module for logging messages
#
# Usage:
# Import the module
# import logger
#
# Create a new object of the Logger class (fileLocation/fileName)
# errorLogs = logger.Logger("errorLogFile.log")
#
# Log messages using the LogMessage method (messageCode, messageType, messageDetails)
# errorLogs.LogMessage("404", "Error", "Resource not found")
#
# Clear the log file using the clear method
# errorLogs.Clear()

from datetime import datetime

class Logger():
    #Run on object creation
    #Creates the log file with the starting opening message
    def __init__(self, logPath):
        self.logPath = logPath
        now = datetime.now()
        dateTimeString = now.strftime("%d/%m/%Y %H:%M:%S:%f")
        self._writeText("## Log started @ " + dateTimeString + " ##")

    #Message logging method
    #Formats the message text and writes it to the file
    def LogMessage(self, logCode, logType, logMessage):
        now = datetime.now()
        dateTimeString = now.strftime("%d/%m/%Y %H:%M:%S:%f")

        textToWrite = "[" + dateTimeString + "] [" + logCode + "] [" + logType + "] " + logMessage

        self._writeText(textToWrite)

    #Log file clearing method
    #Emptys out the contents of the log file
    def Clear(self):
        open(self.logPath, "w").close()

    #Internal text writing method
    def _writeText(self, text):
        with open(self.logPath, "a") as f:
            f.write(text + "\n")

    #Internal property method for getting the value of the log path
    def _get_logPath(self):
        return self._logPath

    #Internal property method for setting the value of the log path
    def _set_logPath(self, value):
        self._logPath = value

    #Property declaration for log path
    logPath = property(_get_logPath, _set_logPath)