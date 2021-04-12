## Flask Named Entity Recognition API

> It's a flask api to perform Named Entity Recognition on scrapped data of Wikipedia and extract entities like city, person, organisation, Date, Geographical Entity, Product etc.

### Feature

- perform Named Entity Recognition on scrapped data of Wikipedia and extrac
- It's a api so it can be used anywhere to perform NER
- It uses Wikipedia api to show the summary of any input

### How to RUN

**This procedure is useful for MAC/LINUX. I'm not sure about Windows.**

**Step 1:**
Frst Install python3 and pip3 in Your system. You can find many tutorials and blog online. (Ignore if already installed)

**Step 2:**
Install Virtial Environment "virtualenv" so that your local Python Dependencies are untouched when installing this Project's dependencies.

```bash
$ pip install virtualenv
```

**Step 4:**

Clone this GITHUB REPO using this Link : https://github.com/Swapnil4Github/project-Flask_ENR_api.git in your desired Directory.

```bash
$ git clone https://github.com/Swapnil4Github/project-Flask_ENR_api.git
```

**Step 5:**
Now you'll be having Project Folder "project-Flask_ENR_api". Navigate to that folder.

```bash
$ cd project-Flask_ENR_api
```

**Step 6:**
Create a Virtual Environment here. You can name anything, but in my case I'm using '_venv_'

```bash
$ virtualenv venv
```

**Step 7:**
Activate the Virtual Environment

```bash
$ source venv/bin/activate
```

Replace the name 'venv' with the name of your virtual environment name, if it's different.

**Step 6:**
Install Dependencies

```bash
$ pip install -r requirements.txt
```

**Step 6:**
Now download required Spacy Model

```bash
$ python -m spacy download en_core_web_sm
```

**Step 6:**
Everything's Done!
Now just run the server

```bash
$ python app.py
```

Wohoo! It's done.
Now go to you browser's search box and paste the server IP **127.0.0.1:8000**

### Example:

**When custom URL already exists**
![Markdown Logo](zimages/1.png)

**When URL is unique**
![Markdown Logo](zimages/2.png)

**After it's done, you get a succes page. Just click on the copy button and paste it in Browser.**
![Markdown Logo](zimages/3.png)

&copy; Swapnil Srivastava 2021