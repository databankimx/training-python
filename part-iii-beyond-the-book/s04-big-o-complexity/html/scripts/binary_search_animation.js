var debug = false;
var interactive = true;
var base_array = [0, 1, 2, 3, 4, 5, 6, 7];
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
                binary_search();
            }
        });
        $("#btn_reset").on("click", function() {
            reset();
        });
        reset();
        if (!interactive) binary_search();
        $("#cb_auto").on("change", function() {
            log("cb");
            interactive = !$(this).is(":checked");
            if (!interactive && !active) binary_search();
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

async function binary_search(target, low, high)
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
        var low = 0;
        var high = array.length - 1;

        var found = false;
        while (high >= low) {
            var mid = Math.ceil((high + low) / 2.0);
            
            $("#i").html(mid);
            $(".i").css("left", (mid * 100 + 100) + "px");
            $("#" + mid).addClass("active");
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
            
            if (array[mid] === target)
            {
                $("#" + mid).removeClass("active");
                $("#" + mid).addClass("found");
                alert(`Target found after ${count} steps!`);
                for (var j = 0; j < array.length; j++) {
                    if (j !== mid) {
                        $("#" + j).addClass("rejected");
                    }
                }
                found = true;
                break;
            }
            else if (array[mid] < target) {
                for (var j = low; j <= mid; j++)
                {
                    $("#" + j).addClass("rejected");
                }
                low = mid + 1;
                continue;
            }
            else {
                for (var j = mid; j <= high; j++)
                {
                    $("#" + j).addClass("rejected");
                }
                high = mid - 1;
                continue;
            }
        }

        if (!found) {
            for (var j = 0; j < array.length; j++) {
                $("#" + j).addClass("rejected");
            }
            alert("Target not found!");
        }

        $( "#target" ).prop( "disabled", false );
        $(".i").hide();
        $("#btn_reset").show();
        active = false;
        $("#btn_step").show().val("search");
        $( "#target" ).prop( "disabled", false );

        return;
    }
    catch (e) {
        log("Error in binary_search()\n" + e);
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