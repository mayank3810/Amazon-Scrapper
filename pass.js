var websiteurl = window.location.href
$.ajax({
url: Flask.url_for('my_function'),
type: 'POST',
data: JSON.stringify(website),  
})
.done(function(result){     
    console.log(result)     
})