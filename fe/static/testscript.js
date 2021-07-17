$('#datepicker').datepicker({
    uiLibrary: 'bootstrap4',
    format: "dd/mm/yyyy"
});

$(".readonly").on('keydown paste focus mousedown', function(e){
    if(e.keyCode != 9)
    e.preventDefault();
});

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      hiddenDays: [0],
      dayHeaderFormat: {weekday: 'short', day: 'numeric'
        },
      allDaySlot: false,
      headerToolbar: {
        left: 'dayGridMonth,timeGridWeek',
        center: 'title',
        right: 'today prev,next'
        }, 
      displayEventTime: true,
      displayEventEnd: true,
      events: {
          url: 'data',
      },
      eventTimeFormat: {
        hour: 'numeric',
        minute: '2-digit',
        meridiem: 'short'
      },
    });
    calendar.render();
    document.calendar = calendar;
  });
