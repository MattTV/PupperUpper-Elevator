function daysbetweendates(startdate, enddate) {
    var start = new Date(startdate);
    var end = new Date(enddate);
    var diff = end.getTime() - start.getTime();
    var days = diff / 1000 / 60 / 60 / 24;
    return days;
}

function sayhello() {
    console.log("Hello World");
}

function webserver