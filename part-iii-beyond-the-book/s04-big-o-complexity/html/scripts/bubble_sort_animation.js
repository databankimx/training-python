var debug = false;
var interactive = true;
var base_array = [7, 2, 5, 4, 1, 6, 0, 3];
var array;
var is_sort = true;
var i, j, count;
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
                bubble_sort();
            }
        });
        $("#btn_reset").on("click", function() {
            reset();
        });
        reset();
        if (!interactive) bubble_sort();
        $("#cb_auto").on("change", function() {
            log("cb");
            interactive = !$(this).is(":checked");
            if (!interactive && !active) bubble_sort();
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

async function bubble_sort()
{
    try {
        $("#btn_step").val("step");
        if (!interactive) $("#btn_step").hide();
        active = true;
        $("#btn_reset").hide();
        $(".i, .j").show();
        for (i = 0; i < array.length; i++)
        {
            $("#i").html(i);
            min = array[i];
            var swaps = 0;
            for (j = 0; j < array.length - 1; j++)
            {
                $(".active").removeClass("active");
                $(".i").css("left", (j * 100 + 100) + "px");
                $(".j").css("left", (j * 100 + 200) + "px");
                $("#" + j + ", #" + (j + 1)).addClass("active");
                $("#i").html(j);
                $("#j").html(j + 1);

                increment();

                if (array[j + 1] < array[j])
                {
                    if (interactive) {
                        while (!go) {
                            await sleep(.001);
                        }
                        go = false;
                    }
                    else {
                        await sleep(0.5);
                    }
                    $("#" + j + ", #" + (j + 1)).addClass("swapping");
                    swaps++;
                    if (interactive) {
                        while (!go) {
                            await sleep(.001);
                        }
                        go = false;
                    }
                    else {
                        await sleep(0.5);
                    }
                    swap(j, j + 1);
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
                if (interactive) {
                    while (!go) {
                        await sleep(.001);
                    }
                    go = false;
                }
                else {
                    await sleep(0.5);
                }
            }
            if (swaps === 0) {
                $(".active").removeClass("active");
                break;
            }
        }
        $(".i, .j").hide();
        $("#btn_reset").show();
        active = false;
        alert(`List sorted in ${count} steps!`)
        $("#btn_step").show().val("sort");
    }
    catch (e) {
        log("Error in bubble_sort()\n" + e);
    }
}

function swap(i, j) {
    var temp = array[i];
    array[i] = array[j];
    $("#" + i).html(array[i]);
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