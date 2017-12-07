var dlgr = window.dlgr || {};

// Consent to the experiment.
$(document).ready(function() {

    // Print the consent form.
    $("#print-consent").click(function() {
        window.print();
    });

    // Consent to the experiment.
    $("#consent").click(function() {
        store.set("hit_id", dallinger.getUrlParameter("hit_id"));
        store.set("worker_id", dallinger.getUrlParameter("worker_id"));
        store.set("assignment_id", dallinger.getUrlParameter("assignment_id"));
        store.set("mode", dallinger.getUrlParameter("mode"));

        dallinger.allowExit();
        window.location.href = '/instructions';
    });

    // Consent to the experiment.
    $("#no-consent").click(function() {
        dallinger.allowExit();
        window.close();
    });

    // Consent to the experiment.
    $("#go-to-experiment").click(function() {
        dallinger.allowExit();
        window.location.href = '/exp';
    });

    // Navigate to the questionnaire.
    $("#end-external-monitoring").click(function() {
        dallinger.allowExit();
        dallinger.goToPage("questionnaire");
    });

    var $external_monitoring = $('#request-external-monitoring');
    if ($external_monitoring.length) {
        $external_monitoring.prop('disabled', true);
        dallinger.createAgent().done(function (resp) {
            dlgr.node_id = resp.node.id;
            $external_monitoring.attr('data-nodeid', dlgr.node_id);
            $external_monitoring.attr('data-experimenturl', window.location.origin);
            $external_monitoring.prop('disabled', false);
        }).fail(function (err) {
            console.log(err);
            errorResponse = JSON.parse(err.response);
            if (errorResponse.hasOwnProperty('html')) {
                $('body').html(errorResponse.html);
            } else {
                dallinger.allowExit();
                dallinger.goToPage('questionnaire');
            }
        });
        $external_monitoring.on('approved', function() {
            window.open('https://www.wikipedia.org', '_blank').focus();
        }).on('rejected', function() {
            alert('Please accept the conditions to continue');
        });
    }
});
