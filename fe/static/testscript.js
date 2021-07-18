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
      themeSystem: 'standard',
      hiddenDays: [0],
      dayHeaderFormat: {weekday: 'short', day: 'numeric'
        },
      allDaySlot: false,
      fixedWeekCount: false,
      headerToolbar: {
        left: 'dayGridMonth,timeGridWeek',
        center: 'title',
        right: 'today prev,next'
        }, 
      displayEventTime: true,
      displayEventEnd: true,
      slotMinTime: '08:00:00',
      slotMaxTime: '24:00:00',
      slotDuration: '00:20:00',
      timeZone: 'local',
      /*events: { //flask
          url: 'data',
      }, */
      events: '/fe/static/events.json', //local
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
          /*
          eventContent: function(info){
          return info.event.title
            }*/
          }
      },
      eventClick: function(info){ 
          alert('ID: '+ info.event.id + info.event.extendedProps.description); 
      },
    });
    calendar.render();
    document.calendar = calendar;
  });