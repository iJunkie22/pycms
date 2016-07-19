/**
 * Created by ethan on 3/30/15.
 */
var fails = new FailCounter();

function checkValid(input, pattern) {
    var had_pattern = false;
    /*try {
        re_pat = new RegExp(input.pattern);
        had_pattern = True;
    }*/
    if (had_pattern === false) {
        var re_pat = new RegExp(pattern);
    }
    fails.initNode(input.id);

    var input_val = input.value;
    var v_state = (input_val.match(re_pat) !== null);
    var inverted_v_state = Boolean(v_state - 1);

    var myLabel = getLabels(input, false);
    if (v_state === false) {
        myLabel.addClassName("error");
        var virt_ev = new Event('invalid', {
            'target': window,
            'bubbles': true,
            'cancelable': true
        });
        input.dispatchEvent(virt_ev);

        console.log(v_state);
        if (inverted_v_state) {
            fails.increment(input.id);
        }
        console.log("fails for " + input.id + " is " + fails.getValue(input.id));
    }

    return v_state;
}