// This function corrects route
// requests to account for proxies
// (e.g., when running in the web VM)
function getRoute(route, route_prepend = window.location.pathname) {
    if (route.startsWith("/")) {
        return route_prepend + route.substring(1);
    }
    else {
        return route_prepend + route;
    }
}

function getClasslist() {
    logConsole("Getting Class List");
    const Url = getRoute('api/classlist');
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", Url, false); // false for synchronous request
    xmlHttp.send(null);
    localStorage.setItem('classlist', xmlHttp.responseText);
    return xmlHttp.responseText;
}

function getCalendarEvent() {
    const Url = getRoute('/api/calendar');
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", Url, false); // false for synchronous request
    xmlHttp.send(null);
    localStorage.setItem('calendar', xmlHttp.responseText);
    return xmlHttp.responseText;
}

function getSummary() {
    //const Url = 'http://192.168.2.103:5000/api/attendance';//swap IP for class
    const Url = getRoute('/api/attendance');
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", Url, false); // false for synchronous request
    xmlHttp.send(null);
    localStorage.setItem('pastAttendances', xmlHttp.responseText);
    return xmlHttp.responseText;
}

function getAttendance(attendanceID) {
    //const Url = 'http://192.168.2.103:5000/api/attendance/'+ attendanceID;//swap IP for class
    const Url = getRoute('/api/attendance/' + attendanceID);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", Url, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function addAttendance(attendance_json) {
    logConsole("Sending Backend Attendance");

    //const Url = 'http://192.168.2.103:5000/api/attendance/' + attendance_json.id;
    const Url = getRoute('/api/attendance/' + attendance_json.id); //localhost ip, change for class
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", Url, false); // false for synchronous request

    console.log(attendance_json); //log json object for debugging

    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(attendance_json));
}

function updateAttendance(attendance_json) {
    logConsole("Sending Backend Attendance");
    const Url = getRoute('/api/attendance/' + attendance_json.id); //localhost ip, change for class
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("PUT", Url, false); // false for synchronous request

    console.log(attendance_json); //log json object for debugging

    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(JSON.stringify(attendance_json));
}

function fillAttendanceDropdown() {
    const dropDown = document.getElementById("select-5c86");
    const pastAttendance_string = localStorage.getItem('pastAttendances');
    const pastAttendance_json = JSON.parse(pastAttendance_string);
    localStorage.setItem('attendances', pastAttendance_string);

    for (let i = 0; i < pastAttendance_json.ids.length; i++) {
        const newOption = document.createElement("option");
        let label = "Attendance " + pastAttendance_json.ids[i];
        let l = (80 - label.length) % 6;
        newOption.innerHTML = label.padEnd(122 - l, "&emsp;") + " (Completed)";

        newOption.value = pastAttendance_json.ids[i];
        dropDown.appendChild(newOption);
    }
    const futureAttendance_json = JSON.parse(getCalendarEvent());
    for (let i = 0; i < futureAttendance_json.length; i++) {
        const newOption = document.createElement("option");
        newOption.innerText = "Attendance " + futureAttendance_json[i].enterpriseID;
        newOption.value = futureAttendance_json[i].enterpriseID;
        dropDown.appendChild(newOption);
    }
}

function editOldAttendance() {
    console.log("editing old attendances");
}

function submitNewAttendance() {
    const dropDown = document.getElementById("select-5c86");
    const selected = dropDown.value;

    const pastAttendances = localStorage.getItem('pastAttendances')
    const completedAttendance = pastAttendances.includes(selected)

    const nextAttendance = JSON.parse(getCalendarEvent());
    let attendanceString = '{"id": "' + nextAttendance.enterpriseID + '", "records": [';
    let formOptions = document.getElementsByClassName("u-form-radiobutton");
    let numOptions = formOptions.length;
    for (let i = 0; i < numOptions; i++) {
        if (i > 0) {
            attendanceString += ', ';
        }
        attendanceString += '{"studentID": ';
        let label = formOptions[i].lastChild.firstChild.firstChild.id;
        attendanceString += label;
        attendanceString += ', "isPresent": '
        if (formOptions[i].lastChild.firstChild.firstChild.checked) {
            attendanceString += 'true}';
        }
        else {
            attendanceString += 'false}';
        }
    }

    attendanceString += ']}'
    console.log(attendanceString);
    addAttendance(JSON.parse(attendanceString));
}

function fillPastAttendance() { //triggered by the retrieve attendance button
    const page = document.getElementById("page-base");
    const form = document.getElementById("form-students");
    form.innerHTML = "";

    const dropDown = document.getElementById("select-5c86");
    const selected = dropDown.value;

    const students = JSON.parse(localStorage.getItem('classlist'));

    const pastAttendances = localStorage.getItem('attendances');

    const completedAttendance = pastAttendances.includes(selected)

    if (completedAttendance) {
        const attendance = JSON.parse(getAttendance(selected));

        for (let i = 0; i < attendance.records.length; i++) {
            const name_label = document.createElement("p");
            name_label.classList.add("u-form-group", "u-form-partition-factor-3", "u-form-text", "u-text", "u-text-1");
            name_label.innerText = attendance.records[i].studentID;

            const number_label = document.createElement("p");
            number_label.classList.add("u-form-group", "u-form-partition-factor-3", "u-form-text", "u-text", "u-text-2");
            number_label.innerText = attendance.records[i].studentID;

            const form_group = document.createElement("div");
            form_group.classList.add("u-form-group", "u-form-input-layout-horizontal", "u-form-partition-factor-3", "u-form-radiobutton", "u-form-group-5");

            const hidden_label = document.createElement("label");
            hidden_label.classList.add("u-form-control-hidden", "u-label");

            const buttonWrapper = document.createElement("div");
            buttonWrapper.classList.add("u-form-radio-button-wrapper");

            const rowPresent = document.createElement("div");
            rowPresent.classList.add("u-input-row");

            const presentRadio = document.createElement("input");
            presentRadio.type = "radio";
            presentRadio.value = "Present";
            presentRadio.required = "required"; {
                if (attendance.records[i].isPresent)
                    presentRadio.checked = "checked";
            }
            presentRadio.id = students[i].studentNumber;
            presentRadio.name = "radio" + i;
            const presentLabel = document.createElement("label");
            presentLabel.htmlFor = "radio" + i;
            presentLabel.classList.add("u-label", "u-spacing-10", "u-label-4");
            presentLabel.innerText = "Present";

            const rowAbsent = document.createElement("div");
            rowAbsent.classList.add("u-input-row");

            const absentRadio = document.createElement("input");
            absentRadio.type = "radio";
            absentRadio.value = "Absent";
            absentRadio.required = "required";
            if (!attendance.records[i].isPresent) {
                absentRadio.checked = "checked";
            }
            absentRadio.name = "radio" + i;
            const absentLabel = document.createElement("label");
            absentLabel.htmlFor = "radio" + i;
            absentLabel.classList.add("u-label", "u-spacing-10", "u-label-4");
            absentLabel.innerText = "Absent";


            rowPresent.appendChild(presentRadio);
            rowPresent.appendChild(presentLabel);

            rowAbsent.appendChild(absentRadio);
            rowAbsent.appendChild(absentLabel);

            buttonWrapper.appendChild(rowPresent);
            buttonWrapper.appendChild(rowAbsent);

            form_group.appendChild(hidden_label);
            form_group.appendChild(buttonWrapper);

            form.appendChild(name_label);
            form.appendChild(number_label);
            form.appendChild(form_group);

            var buttonText = "Re-Submit";
            var buttonFunction = function () { editOldAttendance(); };
        }
    }
    else {
        for (let i = 0; i < students.length; i++) {
            const name_label = document.createElement("p");
            name_label.classList.add("u-form-group", "u-form-partition-factor-3", "u-form-text", "u-text", "u-text-1");
            name_label.innerText = students[i].firstname + students[i].lastname;

            const number_label = document.createElement("p");
            number_label.classList.add("u-form-group", "u-form-partition-factor-3", "u-form-text", "u-text", "u-text-2");
            number_label.innerText = students[i].studentNumber;

            const form_group = document.createElement("div");
            form_group.classList.add("u-form-group", "u-form-input-layout-horizontal", "u-form-partition-factor-3", "u-form-radiobutton", "u-form-group-5");

            const hidden_label = document.createElement("label");
            hidden_label.classList.add("u-form-control-hidden", "u-label");

            const buttonWrapper = document.createElement("div");
            buttonWrapper.classList.add("u-form-radio-button-wrapper");

            const rowPresent = document.createElement("div");
            rowPresent.classList.add("u-input-row");

            const presentRadio = document.createElement("input");
            presentRadio.type = "radio";
            presentRadio.value = "Present";
            presentRadio.required = "required";
            presentRadio.checked = "checked";
            presentRadio.id = students[i].studentNumber;
            presentRadio.name = "radio" + i;
            const presentLabel = document.createElement("label");
            presentLabel.htmlFor = "radio" + i;
            presentLabel.classList.add("u-label", "u-spacing-10", "u-label-4");
            presentLabel.innerText = "Present";

            const rowAbsent = document.createElement("div");
            rowAbsent.classList.add("u-input-row");

            const absentRadio = document.createElement("input");
            absentRadio.type = "radio";
            absentRadio.value = "Absent";
            absentRadio.required = "required";
            absentRadio.name = "radio" + i;
            const absentLabel = document.createElement("label");
            absentLabel.htmlFor = "radio" + i;
            absentLabel.classList.add("u-label", "u-spacing-10", "u-label-4");
            absentLabel.innerText = "Absent";


            rowPresent.appendChild(presentRadio);
            rowPresent.appendChild(presentLabel);

            rowAbsent.appendChild(absentRadio);
            rowAbsent.appendChild(absentLabel);

            buttonWrapper.appendChild(rowPresent);
            buttonWrapper.appendChild(rowAbsent);

            form_group.appendChild(hidden_label);
            form_group.appendChild(buttonWrapper);

            form.appendChild(name_label);
            form.appendChild(number_label);
            form.appendChild(form_group);

            var buttonText = "Submit";
            var buttonFunction = function () { submitNewAttendance(); };
        }
    }



    const buttonRow = document.createElement("div");
    buttonRow.classList.add("u-form-group", "u-form-submit", "u-label-left");

    const buttonSpacer = document.createElement("label");
    buttonSpacer.classList.add("u-label", "u-spacing-10", "u-label-17");

    const buttonContainer = document.createElement("div");
    buttonContainer.classList.add("u-align-left", "u-btn-submit-container");

    const buttonInput = document.createElement("input");
    buttonInput.type = "submit";
    buttonInput.value = "submit";
    buttonInput.classList.add("u-form-control-hidden");

    const button = document.createElement("a");
    button.classList.add("u-btn", "u-btn-round", "u-btn-submit", "u-btn-style", "u-radius-50", "u-btn-2");
    button.onclick = buttonFunction;
    button.innerText = buttonText;

    buttonContainer.appendChild(button);
    buttonContainer.appendChild(buttonInput);

    buttonRow.appendChild(buttonSpacer);
    buttonRow.appendChild(buttonContainer);

    form.appendChild(buttonRow);
    page.appendChild(form);
}


/*------------------------------------------------------------------------------------------
* Function	        :	logConsole()
* Description	    :	This Function is used to log request and responses to the console.			
* Parameters	    :	String : the request or response to log to the console
* ------------------------------------------------------------------------------------------*/
function logConsole(loggingValue) {
    //Gets the date time
    if (loggingValue) {
        const d = Date();
        console.log("[" + loggingValue + "] " + d);
        return ("[" + loggingValue + "] " + d);
    }
    else {
        //logging page load
        const d = Date();
        console.log("[Page Load]" + " " + d);
        return ("[Page Load]" + " " + d);
    }
}

module.exports = {
    logConsole, addAttendance, updateAttendance, getRoute
};