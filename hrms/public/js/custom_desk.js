frappe.ui.on('ready', function() {
    // Check if we are on the main dashboard page
    if (frappe.get_route_str() === 'desktop') {

        // Initially hide all dashboard widgets
        $('.dashboard-widget').addClass('dashboard-widget-hidden');

        // Animate each widget one-by-one
        $('.dashboard-widget').each(function(index) {
            var $widget = $(this);
            // Add the 'visible' class with a staggered delay
            setTimeout(function() {
                $widget.removeClass('dashboard-widget-hidden').addClass('dashboard-widget-visible');
            }, 150 * index); // 150ms delay between each widget
        });
    }
});