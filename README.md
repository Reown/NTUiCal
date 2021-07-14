# NTUiCal
Python script to parse data from 'Check/Print Courses Registered' to ICS 

## Branch Structure
- main
- feature-fe -> flask experiments
- prod -> deployed to Heroku

## Input Data Required
 - Date of semester's first day according to [NTU calendar](https://www.ntu.edu.sg/admissions/matriculation/academic-calendars)
 - Semester's table data from ['Check/Print Courses Registered'](https://sso.wis.ntu.edu.sg/webexe88/owa/sso_redirect.asp?t=1&app=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_check.check_subject_web2)

## Usage -WIP-


## Supported Edge Cases
- [x] Exempted Modules
- [x] Online Modules
- [x] Recess Week
- [x] Saturday Classes
- [x] Merged rows (Empty Course/Title)
- [ ] Missing Laboratory Codes (Engineering only?)
- [ ] 'Asynchronous online learning' Remark
