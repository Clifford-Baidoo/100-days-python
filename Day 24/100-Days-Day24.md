## Day 24 - Working with Local Files and Directories 

### 217 - Day 21 Goals
We will improve our snake game by adding a score and high score 
We are going to create a project that will automate our life for us
like writing emails for us with different names

### 218 - Add a High Score to the Snake Game
We will add a new attribute high score to the scoreboard class 
and we will replace the game_over method with a new method called reset

```Python
self.high_score = 0

def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score},High Score: {self.high_score} align=ALIGNMENT, font=FONT")

def reset(self):
    if self.score > self.high_score:
        self.high_score = self.score
    self.score = 0
    self.update_scoreboard()
```

So in the reset method we use an if statement to check if score is greater than high_score and if it is score will become the new high score then score will go back to zero then it will update the scoreboard

We will go into our main.py file 
We will delete the game_is_on = False and where we call game over and replace it with the reset method

After you implement it the code will update the scoreboard but the snake will go out of the border so we will create a snake reset method in snake.py

```Python
def reset(self):
    for seg in self.squares:
        seg.goto(1000,1000)
    self.squares.clear()
    self.create_snake()
    self.head = self.sqaures[0]
```

now we will go into the main.py and use the reset method
and everything will Work 
Try and figure out how the code works but it doesn't save the highscore after we quit the game

In the next lesson we will automate it so that it will save manually

### 219 - How to Open,Read and Write to Files
We are going to learn how to read,write files with pthone

create a file called my_file_txt and type some stuff in it

#### Reading file
You can use the open method to open files
```Python
file = open("my_file_txt")
contents = file.read()
print(contents)
file.close()
```
what this code does is the open function opens the file and the .read() reads the content of the file
which we print out 
and we use the .close() to close the file after we are done

An alternative and much more simpler way is to ouse the with keyword
```Python
with open("my_file_txt") as file:
    contents = file.read()
    print(contents)
```

This does the same thing but in 3 lines and we don't need to close it
The with keyword will manage the file directly which will automatically close the file 

#### Writing
```Python
with open("my_file_txt", mode="w") as file:
    file.write("New.text.")
```
What the .write() does is it writes new stuff into our txt but we need to change the mode from read to write before we can save changes
All the previous text will be deleted

If you want to add new stuff instead of deleting it you can change the mode to a which stands for append
```Python
with open("my_file_txt", mode="a") as file:
    file.write(\n"New.text.")
```
### 220 - Challenge_Read and Write the High Score to a File in Snake
Create a new file called data.txt that will contain a single number zero

#Challenge 
Let your high_score attribute read from the data.txt file
and let it also write into the data.txt file
So that when you quit and open again the high score will be there

### 221 - Understand Relative and Absolute File Paths

#### Absolute and Relative Paths

In the context of file systems, **absolute** and **relative paths** are ways to define the location of a file or directory.

#### Absolute Path
An absolute path is the complete path from the root directory (`/` on Linux/Mac, or a drive letter like `C:\` on Windows) to the target file or directory. It provides the full location, ensuring that you can locate the file regardless of your current working directory.

- **Example (Linux/Mac):** `/home/user/documents/file.txt`
- **Example (Windows):** `C:\Users\User\Documents\file.txt`

#### Key Characteristics
- Always starts from the root directory.
- Unambiguous, providing a unique path to the target.

#### Relative Path
A relative path is the path to a file or directory starting from the current working directory. It doesn't start from the root; instead, it’s defined based on the location you’re currently in.

- **Example:** `documents/file.txt` (when your current directory is `/home/user`)
- `.` represents the current directory, while `..` represents the parent directory.

#### Key Characteristics
- Shorter and more flexible, depending on where you’re currently located.
- Useful for navigating within nested directories without specifying the full path.

#### Comparison
| Aspect               | Absolute Path                           | Relative Path                   |
|----------------------|-----------------------------------------|---------------------------------|
| Starts From          | Root directory                          | Current directory               |
| Dependency           | Independent of current location         | Dependent on current location   |
| Use Case             | Scripts, shortcuts, or full references | Navigating within a directory   |

### 222 - Introducing the Mail Merge Challenge

#### Mail Merging

**Mail merging** is a technique used to create multiple documents or messages based on a single template and a data source. It's commonly used for mass communication, such as personalized letters, emails, labels, or envelopes, allowing each output document to be customized with specific information for each recipient.

#### How Mail Merging Works
Mail merging typically involves two components:

1. **Template Document**: A document with placeholders or fields for variable information, like names, addresses, or other personalized details.
2. **Data Source**: A list of information that feeds into the template, usually stored in a spreadsheet, database, or table (e.g., Excel, CSV, or database file). Each row represents a different recipient or document.

During the merging process, the software (such as Microsoft Word or Google Docs) combines these components, replacing placeholders with corresponding data values from the data source, and generating unique documents for each entry.

#### Steps in a Mail Merge Process

1. **Prepare the Data Source**: Compile information in a table or spreadsheet format where each row corresponds to an individual record, and each column represents a variable field (e.g., `Name`, `Address`).
2. **Create the Template**: Write a template document with placeholders for the fields you want to personalize (e.g., `Dear {Name}`).
3. **Insert Merge Fields**: Insert placeholders in the template document. These will dynamically update with data from the source.
4. **Merge and Generate Output**: Run the merge function to produce individual documents or emails for each record in the data source.

#### Common Applications
- **Personalized Letters and Emails**: Great for addressing each recipient by name in bulk communications.
- **Envelopes and Labels**: Used to print addresses from a list onto envelopes or shipping labels.
- **Certificates and Awards**: Automatically generate certificates by filling in names and other details.

#### Example
Let's say you're creating personalized invitations for an event. With mail merging:
- **Template Document**: "Dear {Name}, you are invited to our event on {Date} at {Location}."
- **Data Source**: A list of recipients with their names, the event date, and the location.

After the merge, each invitation will contain specific details for each individual, streamlining the personalization process.


#TODO: Create a letter using starting_letter.docx
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name
#Save the letters in the folder "ReadyToSend"

#Hint1: This method will help you:[link] (https://www.w3schools.com/python/ref_file_readlines.asp)
#Hint2: This method will also help you:[link]( https://www.w3schools.com/python/ref_string_replace.asp)
#Hint3: THis method will help you: [link](https://www.w3schools.com/python/ref_string_strip.asp)

The folders are already in the mail merge folder
Use it to do the work
