var scheduleArr //= [{class : "B101", time : [ 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
               // {class : "105",  time : [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]}];
                //Test Data

var dropMenuArr = new Array();

window.addEventListener("load", function(){
    let floors = document.querySelectorAll(".floors");
    let clamps = document.querySelectorAll(".clamp");

    for(let floor of floors) floor.addEventListener("click", displayFloor);
    for(let clamp of clamps) clamp.addEventListener("click", displayFloor);

    displayFloor(-1);
});
function ajax(room){//before call setDropMenu
    //ajax
   // loadingshow();
    scheduleArr=new Array();
    let tmpschedule
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'back/classselectajax.php');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            tmpschedule = xhr.responseText;

            //tmpschedule="["B104","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]";
            tmpschedule = JSON.parse(tmpschedule);
            tmpschedulear = new Object();
            tmpschedulear.class = tmpschedule[0];
            tmpschedulear.time = new Array();
            for (let i = 0; i < 26; i++)
                tmpschedulear['time'].push(tmpschedule[i + 1]);
            scheduleArr.push(tmpschedulear);
            //ajax
           // loadinghide();
            setDropMenu(room);
        }
    }
    xhr.send("class=" + room);
}
function setDropMenu(room){
    let schedule;
    dropMenuArr = new Array();

    for(let index of scheduleArr){
        if(index.class == room){
            schedule = index;
            break;
        }
    }
    for(let i = 9; i <= 21; i++){
        if(schedule.time[(i - 9) * 2] == 0){
            let dropMenu = document.createElement("div");

            dropMenu.className = "dropMenu";
            dropMenu.textContent = (i >= 10)? i : "0" + i;
            dropMenu.addEventListener("click", selectDropMenu);

            dropMenuArr.push(dropMenu);
        }
    }
}

function fadeOut(){
    let floorNum = document.querySelector(".floorNum");
    let menuBox = document.querySelector(".menuWrapper");
    let underBar = document.querySelector(".floorNumUnderBar");

    floorNum.style.opacity = "0";
    menuBox.style.opacity = "0";
    underBar.style.width = "0px";
    underBar.style.left = "50%";
}

function fadeOutAll(mode){
    if(mode == 1){
        let floors = document.querySelectorAll(".floors");

        for(let floor of floors){
            floor.style.transition = "200ms";
            floor.style.opacity = "0";
        }
    }
    else{
        let fromToBox = document.querySelectorAll(".fromToBox");
        let backClamp = document.querySelector(".backClamp");
        let reserveClamp = document.querySelector(".reserveClamp");

        backClamp.style.opacity = "0";
        reserveClamp.style.opacity = "0";
        
        for(let box of fromToBox) box.style.opacity = "0";

        withdrawDropMenu();
    }

    fadeOut();
}

function changeBoxes(mode){
    if(mode == 1){
        let sideBar = document.querySelector(".sideBar");
        let menuWrapper = document.querySelector(".menuWrapper");
        let backClamp = document.createElement("div");
        let reserveClamp = document.createElement("div");
    
        sideBar.innerHTML = "";
        menuWrapper.innerHTML = "";
    
        backClamp.className = "backClamp";
        backClamp.addEventListener("click", toFloor);
        sideBar.appendChild(backClamp);

        reserveClamp.className = "reserveClamp";
        reserveClamp.addEventListener("click", reserveClassroom);
        menuWrapper.appendChild(reserveClamp);
    
        for(let i = 0; i < 2; i++){
            let fromToBox = document.createElement("div");
    
            fromToBox.className = "fromToBox";
            fromToBox.textContent = (!i)? "From" : "To";
    
            sideBar.appendChild(fromToBox);
        }

        for(let i = 0; i < 2; i++){
            let selectorWrapper = document.createElement("div");
            let dropDownBox = document.createElement("div");
            let dropDownSpan = document.createElement("span");
            let dropDownClamp = document.createElement("div");
            let checkWrapper = document.createElement("div");
            let checkBox = document.createElement("div");
            let checkSpan = document.createElement("span");

            selectorWrapper.className = "selectorWrapper";
            dropDownBox.className = "dropDown";
            dropDownSpan.className = "dropDownSpan";
            dropDownClamp.className = "dropDownClamp";
            checkWrapper.className = "checkWrapper";
            checkBox.className = "checkBox";
            checkSpan.className = "checkSpan";
            checkSpan.textContent = "30'";

            dropDownSpan.id = i + 1;
            dropDownClamp.id = i + 1;
            checkBox.id = i + 1;

            dropDownBox.appendChild(dropDownSpan);
            dropDownBox.appendChild(dropDownClamp);
            checkWrapper.appendChild(checkBox);
            checkWrapper.appendChild(checkSpan);
            selectorWrapper.appendChild(dropDownBox);
            selectorWrapper.appendChild(checkWrapper);
            menuWrapper.appendChild(selectorWrapper);

            dropDownClamp.addEventListener("click", clickDropMenu);
            checkBox.addEventListener("click", clickCheckBox);
        }
    }
    else{
        let sideBar = document.querySelector(".sideBar");
        let menuWrapper = document.querySelector(".menuWrapper");
        let mapWrapper = document.createElement("div");
        
        sideBar.innerHTML = "";
        menuWrapper.innerHTML = "";

        mapWrapper.className = "mapWrapper";

        for(let i = 4; i >= -2; i--){
            if(i == 0) continue;
            
            let floors = document.createElement("div");

            floors.className = "floors";
            floors.id = i;
            floors.textContent = (i > 0)? i : "B" + Math.abs(i);
            floors.addEventListener("click", displayFloor);
            floors.style.opacity = "0";
            floors.style.transition = "200ms";
            
            sideBar.appendChild(floors);
        }

        for(let i = 0; i < 5; i++){
            let room = document.createElement("div");

            room.className = "classroom";

            if(i == 0) room.className += " horizontal left";
            else if(i == 1) room.className += " horizontal right";
            else if(i == 2) room.className += " vertical right";
            else if(i == 3) room.className += " vertical left rotate";
            else room.className += " horizontal center";

            room.addEventListener("click", toReserve);
            mapWrapper.appendChild(room);
        }

        menuWrapper.appendChild(mapWrapper);

        for(let i = 0; i < 2; i++){
            let clamp = document.createElement("div");

            clamp.className = "clamp";

            if(i == 0) clamp.className += " left";
            else clamp.className += " right";

            clamp.addEventListener("click", displayFloor);
            menuWrapper.appendChild(clamp);
        }

        setTimeout(function(){
            let floors = document.querySelectorAll(".floors");

            for(let floor of floors){
                floor.style.opacity = "1";
            }
        }, 200);

        setTimeout(function(){
            let floors = document.querySelectorAll(".floors");

            for(let floor of floors){
                floor.style.transition = "0ms";
            }
        }, 400);
    }
}

function displayFloorNum(floor){
    let floorNum = document.querySelector(".floorNum");
    
    if(floor < 0) floor = "B" + Math.abs(floor);

    floorNum.textContent = floor;
    floorNum.style.opacity = "1";
}

function displayRoomNum(room){
    let roomNum = document.querySelector(".floorNum");

    roomNum.textContent = room;
    roomNum.style.opacity = "1";
}

function displayUnderBar(floor){
    let underBar = document.querySelector(".floorNumUnderBar");
    let length = (floor >= 1 && floor <= 4)? 80 : 120;

    underBar.style.width = length + "px";
    underBar.style.left = "calc(50% - " + length / 2 + "px)";
}

function displayRoomUnderBar(room){
    let underBar = document.querySelector(".floorNumUnderBar");
    let length = (room.length > 3)? 200 : 150;

    underBar.style.width = length + "px";
    underBar.style.left = "calc(50% - " + length / 2 + "px)";
}

function displaySideBar(floor){
    let floors = document.querySelectorAll(".floors");
    
    for(let box of floors){
        if(parseInt(box.id) == floor) box.style.backgroundColor = "#262626";
        else box.style.backgroundColor = "#900";
    }
}

function displayClassroom(floor){
    let classrooms = document.querySelectorAll(".classroom");
    let numIndex = 1;

    if(floor < 0) floor = "B" + Math.abs(floor);
    
    for(let classroom of classrooms){
        classroom.textContent = floor + "0" + numIndex;
        classroom.id = floor + "0" + numIndex++;

        classroom.addEventListener("click", toReserve);
    }
}

function displayDropMenu(room){
    let selectorWrappers = document.querySelectorAll(".selectorWrapper");

    for(let selectorWrapper of selectorWrappers) selectorWrapper.style.opacity = "1";
}

function showDropMenu(id){
    let dropMenuWrapper = document.createElement("div");
    let body = document.querySelector("body");
    let dropDownSpan = document.querySelectorAll(".dropDownSpan");

    dropMenuWrapper.className = "dropMenuWrapper";

    if(dropMenuArr.length >= 5){
        dropMenuWrapper.style.height = "250px";
    }
    else{
        dropMenuWrapper.style.height = dropMenuArr.length * 50 + "px";
    }

    for(let dropMenu of dropMenuArr){
        dropMenuWrapper.appendChild(dropMenu);
    }

    let rect = dropDownSpan[id - 1].getBoundingClientRect();

    dropMenuWrapper.style.top = rect.top + 80 + "px";
    dropMenuWrapper.style.left = rect.left - 20 + "px";
    dropMenuWrapper.id = id;

    body.appendChild(dropMenuWrapper);
}

function withdrawDropMenu(){
    let dropMenuWrapper = document.querySelector(".dropMenuWrapper");
    let body = document.querySelector("body");

    if(dropMenuWrapper != null){
        dropMenuWrapper.innerHTML = "";
        body.removeChild(dropMenuWrapper);
    }
}

function selectDropMenu(menu){
    let value = parseInt(menu.target.textContent);
    let id = parseInt(menu.target.parentElement.id);
    let dropDownSpan = document.querySelectorAll(".dropDownSpan");

    setTimeout(function(){
        withdrawDropMenu();

        dropDownSpan[id - 1].textContent = (value >= 10)? value : "0" + value;
    }, 1);
}

function displayMenuWrapper(floor){
    let menuBox = document.querySelector(".menuWrapper");
    let clamps = document.querySelectorAll(".clamp");

    menuBox.style.opacity = "1";

    clamps[0].id = (floor == 1)? -1 : floor - 1;
    clamps[1].id = (floor == -1)? 1 : floor + 1;
}

function displayRoomMenuWrapper(){
    let menuWrapper = document.querySelector(".menuWrapper");
    let reserveClamp = document.querySelector(".reserveClamp");

    menuWrapper.style.opacity = "1";
    reserveClamp.style.opacity = "1";
}

function displayFloor(floor){
    if(!Number.isInteger(floor)) floor = parseInt(floor.target.id);

    if(floor <= 4 && floor >= -2){
        fadeOut();

        setTimeout(function(){
            displayFloorNum(floor);
            displayUnderBar(floor);
            displaySideBar(floor);
            displayClassroom(floor);
            displayMenuWrapper(floor);
        }, 200);
    }
}

function displayReserveSideBar(){
    let sideBarArr = document.querySelector(".sideBar").childNodes;
    
    for(let node of sideBarArr){
        node.style.opacity = "1";
    }
}

function toReserve(room){
    room = room.target.id;

    fadeOutAll(1);

    setTimeout(function(){
        changeBoxes(1);
        //setDropMenu(room);
        ajax(room);
    }, 200);

    setTimeout(function(){
        displayReserveSideBar();
        displayRoomNum(room);
        displayRoomUnderBar(room);
        displayDropMenu(room);
        displayRoomMenuWrapper();
    }, 400);
}

function toFloor(){
    let room = document.querySelector(".floorNum").textContent;
    let floor;

    if(room.length > 3){
        room = room.replace("B", "");

        floor = parseInt(parseInt(room) / 100) * -1;
    }
    else{
        floor = parseInt(parseInt(room) / 100);
    }

    fadeOutAll(2);

    setTimeout(function(){
        changeBoxes(2);
    }, 200);

    setTimeout(function(){
        displayFloor(floor);
    }, 400);
}

function clickDropMenu(id){
    id = parseInt(id.target.id);

    withdrawDropMenu();
    showDropMenu(id);
}

function clickCheckBox(id){
    let checkBox = document.querySelectorAll(".checkBox");
    let tmpId = parseInt(id.target.id);

    if(Number.isNaN(tmpId)){
        id = parseInt(id.target.parentElement.id);
    }
    else id = tmpId;

    if(id > 0){
        id = id * -1;

        let smallCheck = document.createElement("div");

        smallCheck.className = "smallCheck";
        checkBox[Math.abs(id) - 1].appendChild(smallCheck);
        checkBox[Math.abs(id) - 1].id = id;
    }
    else{
        id = id * -1;

        checkBox[Math.abs(id) - 1].innerHTML = "";
        checkBox[Math.abs(id) - 1].id = id;
    }
}

function reserveClassroom(){
    let startTimeH = parseInt(document.querySelectorAll(".dropDownSpan")[0].textContent);
    let endTimeH = parseInt(document.querySelectorAll(".dropDownSpan")[1].textContent);
    let startTimeM = (document.querySelectorAll(".checkBox")[0].id > 0)? 0 : 1;
    let endTimeM = (document.querySelectorAll(".checkBox")[1].id > 0)? 0 : 1;
    let roomNum = document.querySelector(".floorNum").textContent;
    let schedule;
    let tmpschedule=new Object();
    tmpschedule.time=new Array();
    for(let i=0;i<26;i++) tmpschedule.time.push("0");
    if(isNaN(startTimeH)||isNaN(endTimeH)||(startTimeH+startTimeM*0.5 >endTimeH + endTimeM*0.5)){
        alert("error");
        return -1;
    }
    for(schedule of scheduleArr) if(schedule.class == roomNum) break;
    tmpschedule.class=schedule.class;
    for(let i = 9; i <= 21; i++){
        if(i == startTimeH){
            if(startTimeM) schedule.time[(i - 9) * 2 + startTimeM] = "1";
            else{
                tmpschedule.time[(i - 9) * 2] = "1";
                tmpschedule.time[(i - 9) * 2 + 1] = "1";
            }
        }
        else if(i > startTimeH && i < endTimeH){
            tmpschedule.time[(i - 9) * 2] = "1";
            tmpschedule.time[(i - 9) * 2 + 1] = "1";
        }
        else if(i == endTimeH){
            tmpschedule.time[(i - 9) * 2] = "1";
            if(endTimeM) schedule.time[(i - 9) * 2 + endTimeM] = "1";
        }
    }
    //if(eval(tmpschedule.time.join('+'))==0){alert("error"); return -1;}
   // for(let i=0;i<26;i++)if(tmpschedule.time[i]=="1"&&schedule.time[i]=="1"){alert("error"); return -1;}
sendPost(JSON.stringify(tmpschedule));
   alert(roomNum + " " + startTimeH + ":" + ((startTimeM)? "30" : "00") + " ~ " + endTimeH + ":" + ((endTimeM)? "30" : "00"));
    
    //toFloor();
}
function loadingshow(){
    document.getElementById('loading').style.display="block";
}
function loadinghide(){
    document.getElementById('loading').style.display="none";
}
function sendPost( params) {
let action="back/backregister.php"
	var form = document.createElement('form');

	form.setAttribute('method', 'post');

	form.setAttribute('action', action);

	document.charset = "utf-8";

		var hiddenField = document.createElement('input');

		hiddenField.setAttribute('type', 'hidden');

		hiddenField.setAttribute('name', 'json');

		hiddenField.setAttribute('value', params);

		form.appendChild(hiddenField);

	

	document.body.appendChild(form);

	form.submit();

}