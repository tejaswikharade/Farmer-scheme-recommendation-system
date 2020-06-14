$(function() {
 $('.rating').barrating({
  theme: 'fontawesome-stars',
  onSelect: function(value, text, event) {

   // Get element id by data-id attribute
   var el = this;
   var el_id = el.$elem.data('id');

   // rating was selected by a user
   if (typeof(event) !== 'undefined') {
 
     var split_id = el_id.split("_");
     var postid = split_id[1]; // postid

     // AJAX Request
     $.ajax({
       url: 'rating_ajax.php',
       type: 'post',
       data: {postid:postid,rating:value},
       dataType: 'json',
       success: function(data){
         // Update average
         var average = data['averageRating'];
         $('#avgrating_'+postid).text(average);
       }
     });
   }
  }
 });
});