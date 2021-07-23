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
      slotDuration: '00:15:00',
      slotLabelFormat: [
      {
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      }],
      timeZone: 'local',
      html: true,
      events: { //flask
          url: 'data',
      },
      views: {
        dayGridMonth: {
          dayHeaderFormat: {
            weekday: 'short'
          },
          displayEventTime: true,
          displayEventEnd: false,
          eventTimeFormat: { 
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
          },
          eventContent: function(info){
            temp = this.eventContent
            return temp
          },
          eventClick: function(info){ 
            startmec1 = info.event.start.getHours()
            startmec2 = info.event.start.getMinutes()

            endmec1 = info.event.end.getHours()
            endmec2 = info.event.end.getMinutes()

            titlemec = info.event.title
            descmec = info.event.extendedProps.description.split("\n")
            locamec = info.event.extendedProps.location
            alert('ID: '+ startmec1 + ':' + startmec2 + ' - ' + endmec1 + ':' + endmec2 + '\n' + titlemec + '\t' + descmec[1] + '\n' + locamec + '\n' + descmec[0]); 
          },
        },
        timeGridWeek: {
          dayHeaderFormat: {
            weekday: 'short', day: 'numeric'
          },
          eventContent: function(info){
            startwci1 = info.event.start.getHours()
            startwci2 = info.event.start.getMinutes()

            endwci1 = info.event.end.getHours()
            endwci2 = info.event.end.getMinutes()

            titlewci = info.event.title
            descwci = info.event.extendedProps.description.split("\n")
            locawci = info.event.extendedProps.location

            finalwci = startwci1 + ':' + startwci2 + ' - ' + endwci1 + ':' + endwci2 + '<br>' + titlewci + ' ' + descwci[1] + '<br>' + locawci + '<br>' + descwci[0]
            return { html: finalwci }
          },
        }
      },
    });
    calendar.render();
    document.calendar = calendar;
});