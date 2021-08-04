# NTUiCal
Python script to parse data from 'Check/Print Courses Registered' to ICS

# Branch Structure
- main
- feature-fes -> flask experiments
- prod -> deployed to Heroku

# Input Data Required
 - Date of semester's first day according to [NTU Calendar](https://www.ntu.edu.sg/admissions/matriculation/academic-calendars)
 - Semester's table data from [Check/Print Courses Registered](https://sso.wis.ntu.edu.sg/webexe88/owa/sso_redirect.asp?t=1&app=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_check.check_subject_web2)

# Usage
### 1. Using the deployed [site](https://ntuical-flask.herokuapp.com/)
- Select date of semester's first day
    <details>
    <summary>Example</summary>
    <br>
    *Monday of Week 1*
    <img src="./images/get_date.png">
    <img src="./images/choose_date.png">
    </details>
- Either upload a `.html` file or paste data from clipboard
    - __OPTION 1:__ Upload `.html` file of [Check/Print Courses Registered](https://sso.wis.ntu.edu.sg/webexe88/owa/sso_redirect.asp?t=1&app=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_check.check_subject_web2) __[RECOMMENDED]__
        <details>
        <summary>Example</summary>
        <br>
        *Right click > Save Page*
        <img src="./images/get_html.png">
        <img src="./images/upload_html.png">
        </details>
    - __OPTION 2:__ Paste table data from [Check/Print Courses Registered](https://sso.wis.ntu.edu.sg/webexe88/owa/sso_redirect.asp?t=1&app=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_check.check_subject_web2)
        <details>
        <summary>Example</summary>
        <br>
        *Only copy the contents within the red box*
        <img src="./images/get_data.png">
        <img src="./images/paste_data.png">
        </details>
- Click `Parse` to view vevents
- Click `Download` to obtain the `.ics` file

### __OR__

### 2. Executing the [vibe.py](https://github.com/Reown/NTUiCal/blob/main/fes/vibe.py) script locally
- Clone the repo
    ```
    $ git clone https://github.com/Reown/NTUiCal
    ```
- Save your [Check/Print Courses Registered](https://sso.wis.ntu.edu.sg/webexe88/owa/sso_redirect.asp?t=1&app=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_check.check_subject_web2) either as a `.html` or copied to a `.txt` file
    <details>
    <summary>Example</summary>
    See <a href ="https://github.com/Reown/NTUiCal/tree/main/samplehtml">samplehtml</a>
    <br>
    or <a href = "https://github.com/Reown/NTUiCal/tree/main/sampletxt">sampletxt</a>
    </details>
- Install the required dependencies
    ```
    pip install -r requirements.txt
    ```
- Run script (2 arguements)
    ```
    python fes/vibe.py <filePath> <DDMMYYYY>
    ```
- A `.ics` file will be saved in the same directory as your `.html` or `.txt` file with the same name

# Supported Edge Cases
- [x] Exempted Modules
- [x] Online Modules
- [x] Recess Week
- [x] Saturday Classes
- [x] Merged rows (Empty Course/Title)
- [ ] Missing Laboratory Codes (Engineering only?)
- [ ] 'Asynchronous online learning' Remark
