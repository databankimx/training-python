var debug = false;
var interactive = true;
var base_array = [7, 2, 5, 4, 1, 6, 0, 3];
var array;
var is_sort = true;
var i, j, min, pos, count;
var go = false;
var active = false;

$(document).ready(function() {
    try {
        $(".i, .j").hide();
        if (!interactive) $("#btn_step").hide();
        $("#btn_step").on("click", function() {
            if (active) {
                go = true;
            }
            else {
                count = 0;
                selection_sort();
            }
        });
        $("#btn_reset").on("click", function() {
            reset();
        });
        reset();
        if (!interactive) selection_sort();
        $("#cb_auto").on("change", function() {
            log("cb");
            interactive = !$(this).is(":checked");
            if (!interactive && !active) selection_sort();
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

async function selection_sort()
{
    try {
        $("#min_data").show();
        $("#btn_step").val("step");
        if (!interactive) $("#btn_step").hide();
        active = true;
        $("#btn_reset").hide();
        $(".i, .j").show();
        for (i = 0; i < array.length - 1; i++)
        {
            $("#i").html(i);
            min = array[i];
            $("#min").html(min);
            pos = i;
            $(".i").css("left", (i * 100 + 100) + "px");
            $("#" + i).addClass("active");
            for (j = i + 1; j < array.length; j++)
            {
                $("#" + j).addClass("active");
                $(".j").css("left", (j * 100 + 100) + "px");
                $("#j").html(j);
                increment();
                if (array[j] < min) {
                    if (interactive) {
                        while (!go) {
                            await sleep(.001);
                        }
                        go = false;
                    }
                    else {
                        await sleep(0.5);
                    }
                    min = array[j];
                    pos = j;
                    $(".found").removeClass("found");
                    $("#" + j).addClass("found");
                    $("#min").html(min);
                }
                if (interactive) {
                    while (!go) {
                        await sleep(.001);
                    }
                    go = false;
                }
                else {
                    await sleep(0.5);
                }
                $("#" + j).removeClass("active");
            }
            if (min < array[i]) {
                $(".found").removeClass("found");
                $("#" + i + ", #" + pos).addClass("swapping");
                if (interactive) {
                    while (!go) {
                        await sleep(.001);
                    }
                    go = false;
                }
                else {
                    await sleep(0.5);
                }
                swap(i, pos);
                if (interactive) {
                    while (!go) {
                        await sleep(.001);
                    }
                    go = false;
                }
                else {
                    await sleep(0.5);
                }
                $(".swapping").removeClass("swapping");
            }
            $("#" + i).removeClass("active");
        }
        $(".i, .j, #min_data").hide();
        $(".found").removeClass("found");
        $("#btn_reset").show();
        active = false;
        alert(`List sorted in ${count} steps!`)
        $("#btn_step").show().val("sort");
    }
    catch (e) {
        log("Error in selection_sort()\n" + e);
    }
}

function swap(i, j) {
    var temp = array[i];
    array[i] = min;
    $("#" + i).html(min);
    array[j] = temp;
    $("#" + j).html(temp);
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
        $("#min_data").show();
        array = base_array.map((x) => base_array[x]);
        array.forEach(element => {
            $("#" + array.indexOf(element)).html(element);
        });
        i = j = min = count = 0;
        $("#min, #steps").html(count);
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