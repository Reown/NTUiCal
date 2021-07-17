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
      slotMinTime: '08:00:00',
      slotMaxTime: '23:30:00',
      slotDuration: '00:30:00',
      timeZone: 'local',
      //events: {
      //    url: 'data',
      //},
      events: '/fe/static/events.json',
      eventTimeFormat: {
        hour: 'numeric',
        minute: '2-digit',
        meridiem: 'short'
      },
      views: {
        dayGridMonth: {
          dayHeaderFormat: {weekday: 'short'},
          displayEventTime: false,
          displayEventEnd: false,
          eventContent: function(info){
          return info.event.title
            }
          }
      },
      eventClick: function(info){ 
          alert('ID: '+ info.event.id + info.event.extendedProps.description); 
      },
    });
    calendar.render();
    document.calendar = calendar;
  });