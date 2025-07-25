Python has a set of methods available for the file object.

|Method       |Description
|-------------|---------------------
|close()	  |  Closes the file
|detach()	  | Returns the separated raw stream from the buffer
|fileno()	  | Returns a number that represents the stream, from the operating system's perspective
|flush()	  |  Flushes the internal buffer
|isatty()	  | Returns whether the file stream is interactive or not
|read()	      | Returns the file content
|readable()	  | Returns whether the file stream can be read or not
|readline()	  | Returns one line from the file
|readlines()  |  Returns a list of lines from the file
|seek()	      | Change the file position
|seekable()	  | Returns whether the file allows us to change the file position
|tell()	      | Returns the current file position
|truncate()	  | Resizes the file to a specified size
|writable()	  | Returns whether the file can be written to or not
|write()	  |  Writes the specified string to the file
|writelines() |  Writes a list of strings to the file