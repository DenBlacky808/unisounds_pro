
$('audio').on('play', function() {
  alert('playback started!');
});

$("audio").each(function(index) {
  var num = index+1;
  $(this).attr('id','myaudio' + num);
});

document.addEventListener('play', function(e){
    var aplayers = $('audio');
    var leng = $('audio').length;
    //console.log(leng);
    for(var i = 0; i < leng;i++){
        if (aplayers[i] != e.target){
            aplayers[i].pause();
        }
    }
}, true);

