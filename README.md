## Flask Named Entity Recognition API

> It's a flask api to perform Named Entity Recognition on scrapped data of Wikipedia 
> and extract entities like city, person, organisation, Date, Geographical Entity, Product etc.

![alt text](https://res.cloudinary.com/trinitytuts/image/upload/v1585627329/REST_API_jqcrkq.png)

- Streamlit App built by me for this project(Github link) : https://github.com/Swapnil4Github/Display_NER_Streamlit
- Flask API deployed link : http://swapnilsrivastava.pythonanywhere.com/
- Streamlit App of this Project deployed link : https://display-ner-streamlit.herokuapp.com

### Feature

- perform Named Entity Recognition on scrapped data of Wikipedia and extract entities like city, person, organisation, Date, Geographical Entity, Product etc.
- It's a api so it can be used anywhere to perform NER
- It uses Wikipedia api to show the summary of any input

![alt text](https://cdn.pixabay.com/photo/2021/04/12/20/47/20-47-42-229_1280.jpg)

### How to RUN

**This procedure is useful for MAC/LINUX. I'm not sure about Windows.**

**Step 1:**
Frst Install python3 and pip3 in Your system. You can find many tutorials and blog online. (Ignore if already installed)

**Step 2:**
Install Virtial Environment "virtualenv" so that your local Python Dependencies are untouched when installing this Project's dependencies.

```bash
$ pip install virtualenv
```

**Step 3:**

Clone this GITHUB REPO using this Link : https://github.com/Swapnil4Github/project-Flask_ENR_api.git in your desired Directory.

```bash
$ git clone https://github.com/Swapnil4Github/project-Flask_ENR_api.git
```

**Step 4:**
Now you'll be having Project Folder "project-Flask_ENR_api". Navigate to that folder.

```bash
$ cd project-Flask_ENR_api
```

**Step 5:**
Create a Virtual Environment here. You can name anything, but in my case I'm using '_venv_'

```bash
$ virtualenv venv
```

**Step 6:**
Activate the Virtual Environment

```bash
$ source venv/bin/activate
```

Replace the name 'venv' with the name of your virtual environment name, if it's different.

**Step 7:**
Install Dependencies

```bash
$ pip install -r requirements.txt
```

**Step 8:**
Now download required Spacy Model

```bash
$ python -m spacy download en_core_web_sm
```

**Step 9:**
Everything's Done!
Now just run the server

```bash
$ python app.py
```
**Step 10:**
Give Input through endpoint to perform NER on it

Now go to you browser's search box and paste the server IP **127.0.0.1:8000/"USER_INPUT"



&copy; Swapnil Srivastava 2021
