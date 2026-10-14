var debug = false;
var interactive = true;
var base_array = [7, 2, 5, 4, 1, 6, 0, 3];
var array;
var is_sort = false;
var i, j, count;
var go = false;
var active = false;

$(document).ready(function() {
    try {
        $(".i").hide();
        if (!interactive) $("#btn_step").hide();
        $("#btn_step").on("click", function() {
            if (active) {
                go = true;
            }
            else {
                count = 0;
                linear_search();
            }
        });
        $("#btn_reset").on("click", function() {
            reset();
        });
        reset();
        if (!interactive) linear_search();
        $("#cb_auto").on("change", function() {
            log("cb");
            interactive = !$(this).is(":checked");
            if (!interactive && !active) linear_search();
            if (interactive && active) $("#btn_step").show();
            if (!interactive && active) {
                $("#btn_step").click().hide();
            }
        });
    }
    catch (e) {
        log("Error in document.ready()\n" + e);
    }
});

async function linear_search()
{
    try {
        $(".found").removeClass("found");
        $(".rejected").removeClass("rejected");
        $("#btn_step").val("step");
        if (!interactive) $("#btn_step").hide();
        active = true;
        $("#btn_reset").hide();
        $(".i").show();
        var target = parseInt($("#target").val());
        $( "#target" ).prop( "disabled", true );

        var found = false;
        for (i = 0; i < array.length; i++)
        {
            $("#i").html(i);
            $(".i").css("left", (i * 100 + 100) + "px");
            $("#" + i).addClass("active");
            increment();
            if (interactive) {
                while (!go) {
                    await sleep(.001);
                }
                go = false;
            }
            else {
                await sleep(0.5);
            }
            if (array[i] === target) {
                found = true;
                $("#" + i).removeClass("active").addClass("found");
                for (var j = i + 1; j < array.length; j++) {
                    $("#" + j).addClass("rejected");
                }
                alert(`Target found after ${count} steps!`);
                break;
            }
            else {
                $("#" + i).removeClass("active").addClass("rejected");
            }
        }

        $(".i").hide();
        $("#btn_reset").show();
        active = false;
        $("#btn_step").show().val("search");
        $( "#target" ).prop( "disabled", false );
        if (!found) alert("Target not found!");
    }
    catch (e) {
        log("Error in linear_search()\n" + e);
    }
}

function increment() {
    count++;
    $("#steps").html(count);
}

function sleep(sec) {
    return new Promise(resolve => setTimeout(resolve, sec * 1000));
}

// Reset the page to its start state
function reset() {
    try {
        $(".found").removeClass("found");
        $(".active").removeClass("active");
        $(".rejected").removeClass("rejected");
        array = base_array.map((x) => base_array[x]);
        array.forEach(element => {
            $("#" + array.indexOf(element)).html(element);
        });
        i = j = count = 0;
        $("#steps").html(count);
    }
    catch (e) {
        log("Error in reset()\n" + e);
    }
}

// Log a message to the console (and alert if in debug mode)
function log(message, error = false) {
    if (error) {
        message = "*** ERROR ***\n" + message;
    }
    if (console.log) {
        console.log(message);
    }
    if (debug) {
        alert(message);
    }
}